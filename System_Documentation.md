# 🧠 Smart Mini GPT — System Documentation

## 📌 System Overview
**Smart Mini GPT** is a web-based chatbot application that allows users to interact with an AI assistant powered by GPT.  
The goal of this system is to provide a simple and interactive chat interface that connects users to an AI model and stores conversations in a local database for better context and record-keeping.

---

## 🧭 System Flow

Frontend (HTML + JavaScript)
↓
Flask Backend (Python)
↓
SQLite Database
↓
OpenAI API (AI Response Generation)


---

## 🛠️ Tools & Technologies

| Component | Technology Used |
|------------|------------------|
| **Language** | Python 3.13 |
| **Framework** | Flask |
| **Database** | SQLite |
| **Frontend** | HTML / CSS / JavaScript |
| **AI Integration** | OpenAI API |
| **Environment Management** | python-dotenv |

---
Follow these steps to set up and run the project locally:

### 1️⃣ Open PowerShell or Terminal inside the project directory.

### 2️⃣ Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate    # On macOS/Linux
pip install flask openai python-dotenv
  python mydatabase/app.py                                                                                                   
http://127.0.0.1:5000






