import subprocess
import sys

# Start FastAPI (uvicorn) server
fastapi_process = subprocess.Popen([sys.executable, "-m", "uvicorn", "main:app", "--reload"])

# Start Streamlit server
streamlit_process = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app.py"])
