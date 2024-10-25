import os
from fastapi import FastAPI
from models import RequestModel, ResponseModel
from dotenv import load_dotenv
import google.generativeai as genai


app = FastAPI()

load_dotenv()
api_key = os.getenv("GEM_API_KEY")

genai.configure(api_key=api_key)


# Endpoint for the chatbot
@app.post("/chatbot", response_model=ResponseModel)
def chat_interaction(test_request: RequestModel):
   user_input = test_request.user_input

   # Send query to Gemini API for processing
   model = genai.GenerativeModel("gemini-1.5-flash")
   bot_response = model.generate_content(user_input)

   return ResponseModel(response=bot_response.text)


@app.get("/")
def index():
   return {"message": "API Running!"}
