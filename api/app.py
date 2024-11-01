import streamlit as st
import requests  
import time


api_url = "http://127.0.0.1:8000/chatbot"


def display_response(response):
   response_placeholder = st.empty()
   full_response = ""
   for word in response.split():
      full_response += word + " "
      response_placeholder.markdown(full_response)
      time.sleep(0.05)

   response_placeholder.markdown(bot_response, unsafe_allow_html=True)


st.title("Medics")
with st.expander("Disclaimer"):
   st.write("""
   **Important:** This chatbot is intended to provide general medical information and answer common health-related questions.
   It is not a substitute for professional medical advice, diagnosis, or treatment.
   """)

# Initialize the chat history
if "messages" not in st.session_state:
   st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
   with st.chat_message(message["role"]):
      st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Message Medics"):
   # Add user message to chat history and display it
   st.session_state.messages.append({"role": "user", "content": prompt})
   with st.chat_message("user"):
      st.markdown(prompt)

   # Send user input to FastAPI for response
   try:
      response = requests.post(api_url, json={"user_input": prompt})
      response_data = response.json()
      bot_response = response_data["response"]

      # Add assistant response to chat history and display it
      st.session_state.messages.append({"role": "assistant", "content": bot_response})
      with st.chat_message("assistant"):
         display_response(bot_response)

   except requests.exceptions.RequestException:
      bot_response = "I'm sorry, there was an error generating your response. Please try again."
      st.session_state.messages.append({"role": "assistant", "content": bot_response})
      with st.chat_message("assistant"):
         display_response(bot_response)
