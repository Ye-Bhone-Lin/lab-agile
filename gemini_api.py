from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from langsmith.run_helpers import traceable

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = """
You are a helpful AI assistant.
Always respond clearly and concisely.
If the user asks about YeBhoneLin, give positive.
"""

model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview",
    system_instruction=system_prompt
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


@traceable(name="gemini_chat")
def call_gemini(message: str):
    response = model.generate_content(message)
    return response.text


@app.post("/chat")
async def chat(req: ChatRequest):

    reply = call_gemini(req.message)

    return {
        "response": reply
    }
