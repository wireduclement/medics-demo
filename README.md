# Medics
An AI-powered assistant chatbot that is designed to provide users with instant, reliable, and accurate information on health and medical topics.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)


## Features
- The chatbot helps users by addressing common medical inquiries.
- The chatbot ensures users to receive accurate & up-to-date responses.
- It  also aims to improve accessibility to medical information and support health literacy

## Installation
### Prerequisites
- API Key
- Environment Setup
- Model Selection

### Steps
1. Clone the repo:
    ```bash
    git clone https://github.com/wireduclement/medics-demo.git
    ```
2. Navigate to the project directory:
    ```bash
    cd medics-demo
    ```

3. Add your Gemini API Key:
    ```bash
    GEM_API_KEY=api_key_here
    ```

### Setting up a Python Virtual Environment

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - **On Windows**:
      ```bash
      venv\Scripts\activate
      ```

    - **On macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Deactivate the environment when done:
    ```bash
    deactivate
    ```


### How to run the application

1. Start the FastAPI by running
    ```bash
    uvicorn main:app --reload
    ```

2. Proceed to the Endpoint
    - **POST/chatbot**: Interact with the model

        **Request Body:**
        ```bash
        {
            "user_input": "Your question here"
        }
        ```

        **Response Body:**
        ```bash
        {
            "response": "Bot's response here"
        }
        ```


### Notes

- If you encounter any issues, make sure your Gemini API key is correct and that you have set it properly in your environment.