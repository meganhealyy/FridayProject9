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

# Function to clear both input and output text boxes
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Create the GUI application
root = tk.Tk()
root.title("OpenAI Chat Completion App")

# Input text box
input_label = tk.Label(root, text="Enter your prompt:")
input_label.pack()

input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_completion)
submit_button.pack()

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack()

# Output text box
output_label = tk.Label(root, text="Output:")
output_label.pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# Run the GUI application
root.mainloop()
