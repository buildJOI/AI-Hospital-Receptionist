from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
from supabase import create_client

# ✅ INIT APP
app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-hospital-receptionist-282g.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ LOAD ENV
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# ✅ SUPABASE CLIENT
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ INPUT MODEL
class PatientInput(BaseModel):
    message: str

# ✅ TEMP MEMORY
patient = {
    "name": None,
    "age": None,
    "query": None,
    "ward": None,
    "step": "ask_query"
}

# ✅ CLASSIFIER
def classify_ward(query: str):
    query = query.lower()

    if any(word in query for word in ["accident", "bleeding", "injury"]):
        return "Emergency"
    elif any(word in query for word in ["depression", "stress", "anxiety"]):
        return "Mental Health"
    else:
        return "General"

# ✅ CHAT ROUTE
@app.post("/chat")
async def chat(data: PatientInput):
    global patient
    msg = data.message

    # STEP 1
    if patient["step"] == "ask_query":
        patient["query"] = msg
        patient["ward"] = classify_ward(msg)
        patient["step"] = "ask_name"
        return {"message": "Please tell your name."}

    # STEP 2
    elif patient["step"] == "ask_name":
        patient["name"] = msg
        patient["step"] = "ask_age"
        return {"message": "Please tell your age."}

    # STEP 3 (FINAL)
    elif patient["step"] == "ask_age":
        patient["age"] = msg

        payload = {
            "patient_name": patient["name"],
            "patient_age": patient["age"],
            "patient_query": patient["query"],
            "ward": patient["ward"],
            "timestamp": str(datetime.now())
        }

        # ✅ SAVE TO SUPABASE
        try:
            supabase.table("patients").insert({
                "patient_name": patient["name"],
                "patient_age": patient["age"],
                "patient_query": patient["query"],
                "ward": patient["ward"]
            }).execute()
        except Exception as e:
            print("Supabase Error:", e)

        # ✅ WEBHOOK
        try:
            requests.post(
                "https://jithinjeevan.app.n8n.cloud/webhook/hospital-ai",
                json=payload
            )
        except Exception as e:
            print("Webhook Error:", e)

        # ✅ RESPONSE FIRST
        response = {
            "message": f"Thank you {patient['name']}. You are assigned to {patient['ward']} ward.",
            "ward": patient["ward"],
            "name": patient["name"]
        }

        # 🔥 RESET AFTER RESPONSE
        patient = {
            "name": None,
            "age": None,
            "query": None,
            "ward": None,
            "step": "ask_query"
        }

        return response

    # ✅ FALLBACK
    patient = {
        "name": None,
        "age": None,
        "query": None,
        "ward": None,
        "step": "ask_query"
    }

    return {"message": "Let's start again. Please describe your problem."}