# 🧠 ChatApp with Voice and OpenAI  

A modern real-time chat application powered by **OpenAI**, featuring **voice input**, **AI-generated responses**, and a clean, responsive web interface.  
Built using **Flask**, **HTML/CSS/JS**, and **OpenAI’s API**, this project demonstrates the integration of conversational AI into an interactive web app.

---

## 🚀 Features

✅ **AI Chat Responses** – Engage in intelligent, context-aware conversations with OpenAI’s LLM.  
🎙️ **Voice Input** – Speak to the app using your microphone (powered by browser speech recognition).  
💬 **Real-time Message Display** – Chat messages appear dynamically without reloading.  
🎨 **Minimal & Modern UI** – Clean, responsive design for both desktop and mobile users.  
⚙️ **Flask Backend** – Lightweight server handling API requests and OpenAI communication.  
🔒 **Environment Variables** – Secure key management via `.env` file.

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Flask (Python) |
| **AI API** | OpenAI GPT API |
| **Voice Recognition** | Web Speech API |
| **Version Control** | Git & GitHub |

---

## 🧠 How It Works

1. The user types or speaks a message.  
2. The Flask backend sends it to the OpenAI API.  
3. The AI’s response is displayed in the chat window.  
4. Voice input and text input can be used interchangeably.

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

```bash
# 1️⃣ Clone this repository
git clone https://github.com/shauryachawla15/chatapp-with-voice-and-openai.git

# 2️⃣ Navigate into the project directory
cd chatapp-with-voice-and-openai

# 3️⃣ Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Create a .env file in the root directory and add your OpenAI key
OPENAI_API_KEY=your_api_key_here

# 6️⃣ Run the Flask app
python3 server.py

# 7️⃣ Open your browser
Visit http://127.0.0.1:8000/

🖼️ Screenshots
<img width="1403" height="753" alt="Screenshot 2025-11-13 194213" src="https://github.com/user-attachments/assets/93e83eb0-b57f-4a84-8ff5-8e0465e5cf32" />
<img width="1430" height="409" alt="Screenshot 2025-11-13 194513" src="https://github.com/user-attachments/assets/b3f56f3b-997e-42ab-89cd-3298d3494cad" />
<img width="1304" height="695" alt="Screenshot 2025-11-13 204812" src="https://github.com/user-attachments/assets/fff1e726-3d1c-4c0d-beb7-485799bba294" />
<img width="1296" height="723" alt="Screenshot 2025-11-13 204930" src="https://github.com/user-attachments/assets/c7978fa1-3631-4eed-aeee-b060fb78689f" />
<img width="1453" height="794" alt="Screenshot 2025-11-13 204938" src="https://github.com/user-attachments/assets/7a70cb18-78b7-403a-8206-513c8da7e3c0" />

🤝 Contributing

Contributions, ideas, and improvements are welcome!
If you'd like to contribute:

Fork the repo 🍴

Create a new branch (feature-xyz)

Commit your changes

Open a Pull Request 🚀



👨‍💻 Developer: Shaurya Chawla
🌍 GitHub: @shauryachawla15

🪄 Acknowledgements

OpenAI API
 for powering the language intelligence

Flask
 for the lightweight backend

Web Speech API
 for voice recognition

Inspiration from modern chat UI designs and voice-enabled assistants

