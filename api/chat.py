import os
import httpx
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Broken AI Chat API",
    description="Simple chat API powered by Groq (Llama 3).",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# KEY ITATOKA ENVIRONMENT VARIABLES
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-8b"  # MODEL MPYA, SAHIHI

@app.get("/")
def home():
    return {
        "message": "Karibu Broken AI Chat API 👑",
        "endpoint": "/chat",
        "example_request": {
            "message": "Habari yako Broken AI?"
        }
    }

@app.post("/chat")
async def chat(message: str = Form(...)):
    if not GROQ_API_KEY:
        return JSONResponse(
            {
                "error": "GROQ_API_KEY haijawekwa.",
                "hint": "Weka GROQ_API_KEY kwenye Environment Variables za Vercel."
            },
            status_code=500
        )

    user_message = message.strip()
    if not user_message:
        return JSONResponse({"error": "Message haiwezi kuwa tupu."}, status_code=400)

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Broken AI, a friendly, smart assistant created by King Broken. "
                    "You answer clearly, helpfully, and respectfully in the language of the user."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": 0.7
    }

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            r = await client.post(GROQ_API_URL, headers=headers, json=payload)

        if r.status_code != 200:
            return JSONResponse(
                {
                    "error": "Groq API imerudisha error.",
                    "status_code": r.status_code,
                    "details": r.text
                },
                status_code=500
            )

        data = r.json()
        reply = data["choices"][0]["message"]["content"]

        return {"reply": reply}

    except Exception as e:
        return JSONResponse(
            {"error": f"Hitilafu wakati wa kuwasiliana na Groq: {str(e)}"},
            status_code=500
        )
