from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

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

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):

    response = model.generate_content(req.message)

    return {
        "response": response.text
    }
