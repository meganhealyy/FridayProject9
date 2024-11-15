import tkinter as tk
import openai
from dotenv import load_dotenv
import os

# Load the OpenAI API key from the .env file
load_dotenv()
apikey = os.getenv("key")
openai.api_key = apikey  # Ensure you set the API key

# Function to get completion from OpenAI
def get_completion():
    prompt = input_text.get("1.0", tk.END).strip()
    if not prompt:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a prompt.")
        return

    try:
        # Using gpt-3.5-turbo (ChatCompletion API)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        output = response.choices[0].message.content.strip()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")