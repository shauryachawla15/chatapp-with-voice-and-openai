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

🧭 Project Structure
chatapp-with-voice-and-openai/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .env (not uploaded)
└── README.md

🖼️ Screenshots

<img width="1304" height="695" alt="Screenshot 2025-11-13 204812" src="https://github.com/user-attachments/assets/e76a0dd9-62fd-43c0-b741-04e814b3dcc9" />
<img width="1296" height="723" alt="Screenshot 2025-11-13 204930" src="https://github.com/user-attachments/assets/17bf5e20-df14-41bc-8208-0f225db19991" />
<img width="1453" height="794" alt="Screenshot 2025-11-13 204938" src="https://github.com/user-attachments/assets/9cb3055f-5f2c-4106-bc15-2142ca6397e8" />
<img width="1403" height="753" alt="Screenshot 2025-11-13 194213" src="https://github.com/user-attachments/assets/89cae640-07d6-4576-9489-0d9ac046221a" />



Chat Interface	Voice Input

	
📚 Additional Information
💡 Future Enhancements

🔊 Add AI-generated voice replies (text-to-speech).

🧍‍♂️ Support multi-user chat or session tracking.

🌐 Deploy to Render / Vercel / Heroku for public use.

🧩 Integrate with LangChain or RAG for smarter context.

🤝 Contributing

Contributions, ideas, and improvements are welcome!
If you'd like to contribute:

Fork the repo 🍴

Create a new branch (feature-xyz)

Commit your changes

Open a Pull Request 🚀

📬 Contact

👨‍💻 Developer: Shaurya Chawla

📧 Email: (add your email here if comfortable)
🌍 GitHub: @shauryachawla15

🪄 Acknowledgements

OpenAI API
 for powering the language intelligence

Flask
 for the lightweight backend

Web Speech API
 for voice recognition

Inspiration from modern chat UI designs and voice-enabled assistants

