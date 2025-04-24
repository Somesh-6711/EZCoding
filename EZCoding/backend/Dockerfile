FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY main.py .  # if you have it at root
# ensure .env (with OPENAI_API_KEY) is not checked in
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
