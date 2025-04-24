from fastapi import FastAPI
from app.api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()   

app = FastAPI(
    title="CodeWise - Code Explainer API",
    description="Paste code snippet and get detailed explanations using LLMs",
    version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to CodeWise API!"}
