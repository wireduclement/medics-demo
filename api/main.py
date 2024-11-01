import os
from fastapi import FastAPI, HTTPException
from models import RequestModel
from dotenv import load_dotenv
import google.generativeai as genai


# Load environment variables
load_dotenv()
api_key = os.getenv("GEM_API_KEY")
genai.configure(api_key=api_key)


# Initial the FastAPI app
app = FastAPI()


# Define the chat response function
def chat_response(user_input: str):
   # Initializing the generative model
   model = genai.GenerativeModel(model_name="gemini-1.5-flash")

   # System prompt guiding the response to medical questions only 
   prompt = (
      "This is a following conversation with you as a medical expert assistant. Only respond to medical-related questions and politely decline to answer any other type of questions.\n\nUser: "
      f"{user_input}\nAI:"
   )

   # Generate response based on the user input
   response = model.generate_content(prompt)
   return response.text.strip()


# Endpoint for the chatbot
@app.post("/chatbot")
async def chat_interaction(test_request: RequestModel):
   try:
      response_msg = chat_response(test_request.user_input)
      return {"response": response_msg}
   except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def index():
   return {"message": "API Running!"}
