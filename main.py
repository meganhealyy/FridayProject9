import tkinter as tk
import openai
from dotenv import load_dotenv
import os

# Load the OpenAI API key from the .env file
load_dotenv()
apikey = os.getenv("key")
openai.api_key = apikey  # Ensure you set the API key