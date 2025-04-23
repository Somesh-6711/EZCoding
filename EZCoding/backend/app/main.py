from fastapi import FastAPI
from app.api.routes import router as api_router

from dotenv import load_dotenv
load_dotenv()   # read .env into os.environ

app = FastAPI(
    title="CodeWise - Code Explainer API",
    description="Paste code snippet and get detailed explanations using LLMs",
    version="0.1.0",
)

# Include API routes
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to CodeWise API!"}
