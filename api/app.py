import streamlit as st
import requests  
import time


api_url = "http://127.0.0.1:8000/chatbot"

st.title("Medics")

# Initialize the chat history
if "messages" not in st.session_state:
   st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
   with st.chat_message(message["role"]):
      st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help you today?"):
   # Add user message to chat history and display it
   st.session_state.messages.append({"role": "user", "content": prompt})
   with st.chat_message("user"):
      st.markdown(prompt)

   # Send user input to FastAPI for response
   try:
      response = requests.post(api_url, json={"user_input": prompt})
      response_data = response.json()
      bot_response = response_data["response"]

      def stream_response(response_text):
         for word in response_text.split():
            yield word + " "
            time.sleep(0.05)

      # Add assistant response to chat history and display it
      st.session_state.messages.append({"role": "assistant", "content": bot_response})
      with st.chat_message("assistant"):
         response_placeholder = st.empty()
         full_response = ""
         for word in bot_response.split():
            full_response += word + " "
            response_placeholder.markdown(full_response)
            time.sleep(0.05)

         response_placeholder.markdown(bot_response, unsafe_allow_html=True)

   except requests.exceptions.RequestException as e:
      st.error(f"Error: {e}")
