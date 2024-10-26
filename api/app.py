import streamlit as st
import requests

# Set the FastAPI URL
api_url = "http://localhost:8000/chatbot"

# Title and input box
st.title("Medics")
user_input = st.text_input("I am a medical assistant, ask a medical question:")

if st.button("Get response"):
   # Send the user question to FastAPI
   response = requests.post(api_url, json={"user_input": user_input})
   if response.status_code == 200:
      bot_response = response.json().get("response", "Sorry, no response.")
      st.write("Chatbot: ", bot_response)
   else:
      st.error("Error in response from the chatbot API")
