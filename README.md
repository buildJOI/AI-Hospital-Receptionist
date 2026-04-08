# 🏥 AI Hospital Receptionist

An intelligent full-stack AI system that simulates a hospital receptionist by collecting patient details, classifying medical conditions, and automating backend workflows.

---

## 🚀 Features

* 💬 Interactive chatbot interface
* 🧠 AI-based ward classification
* 🏥 Supports:

  * General Ward
  * Emergency Ward
  * Mental Health Ward
* 🗂️ Stores patient data in database
* 🔗 Webhook automation integration
* 🎨 Clean and modern UI

---

## 🧠 How It Works

1. User describes their medical issue
2. System collects:

   * Name
   * Age
3. AI classifies patient into appropriate ward
4. Data is stored in database
5. Webhook triggers automation workflow

---

## 🏗️ System Architecture

```
Frontend (React + Vite)
        ↓
Backend (FastAPI)
        ↓
AI Logic (Ward Classification)
        ↓
Database (Supabase)
        ↓
Automation (n8n Webhook)
```

---

## 🛠️ Tech Stack

* **Frontend:** React (Vite)
* **Backend:** FastAPI
* **Database:** Supabase
* **Automation:** n8n
* **Styling:** CSS

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Hospital-Receptionist.git
cd AI-Hospital-Receptionist
```

---

### 2️⃣ Backend Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 3️⃣ Frontend Setup

```bash
cd ai-receptionist
npm install
npm run dev
```

---

## 🔐 Environment Variables

Create a `.env` file in root:

```
SUPABASE_URL=your_url_here
SUPABASE_KEY=your_key_here
```

---

## 🧪 Example Flow

```
User: I have fever
Bot: Please tell your name
User: Jithin
Bot: Please tell your age
User: 20

Result: Assigned Ward → General
```

---

## 📸 Screenshots

> Add screenshots here (UI, Supabase, n8n workflow)

---

## 🔮 Future Scope

* 🎤 Voice-based interaction
* 🌐 Multilingual support
* 📊 Admin dashboard
* 📱 Mobile app

---

## 🎯 Use Case

This system demonstrates how AI and automation can:

* Improve hospital efficiency
* Reduce manual workload
* Enable faster patient triage

---

## 👨‍💻 Author

**Jithin Jeevan**

---

## ⭐ Acknowledgements

* FastAPI
* React
* Supabase
* n8n

---

## 📌 License

This project is for educational purposes.
