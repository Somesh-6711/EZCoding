# EZCoding

An LLM-powered code explainer. Paste or upload code → AI tutor explains it line by line.


## 🛠 Tech Stack
- **Frontend:** React (create-react-app), Axios  
- **Backend:** FastAPI, Uvicorn, Pygments, Transformers, OpenAI API  
- **Deployment:** Vercel (FE), Railway.app (BE)  
- **Dockerized** for CI/CD.

## 📦 Features
1. Detect code language via Pygments (with filename hints).  
2. Explain code via OpenAI GPT-3.5-turbo (fallback to Codet5).  
3. Paste code **or** upload a `.py` / `.js` file.  
4. Automatic chunking for large files.  
5. CORS-enabled for web UI.

## ⚙️ Setup

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # add your OPENAI_API_KEY here
uvicorn app.main:app --reload

### Backend
```bash
cd frontend
npm install
cp .env.example .env       # set REACT_APP_API_URL=http://localhost:8000
npm start


## 5️⃣ Deployment

1. **Backend to Railway:**
   - Create a new Railway project → connect your GitHub repo → choose `backend` folder.
   - In Railway Env. Vars, add `OPENAI_API_KEY`.
   - Railway auto-deploys on push to `main`.

2. **Frontend to Vercel:**
   - Import your GitHub repo on Vercel → select `frontend` folder.
   - In Vercel Settings → Environment → add `REACT_APP_API_URL=https://your-railway-url`.
   - Deploy.

Once both are live, link them in your README under “Live Demo.”

---

# 🎉 You’re Now Fully End-to-End!

- ✔️ **Local dev** with file upload, chunking, GPT-3.5 fallback.  
- ✔️ **Docker support** for CI/CD.  
- ✔️ **React UI** that handles paste or upload seamlessly.  
- ✔️ **README** for recruiters & users.  
- ✔️ **Deployment** guide.
```
### I am a student and still learning and trying to be better.
![Screenshot 2025-04-24 160400](https://github.com/user-attachments/assets/6cd26aff-1ceb-4150-904e-f01fb57147ef)
![Screenshot 2025-04-24 160349](https://github.com/user-attachments/assets/51bcd1a4-e6b0-43ac-b02f-81a6530097c8)
![Screenshot 2025-04-24 160208](https://github.com/user-attachments/assets/09e02f4e-6271-474a-b6e3-0e77ff05fbc1)
![Screenshot 2025-04-23 205928](https://github.com/user-attachments/assets/7e5925d7-aeeb-4f9c-b4d5-8f3ce82718b7)


