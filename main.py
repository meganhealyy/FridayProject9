import tkinter as tk
import openai
import sqlite3
from dotenv import load_dotenv
import os

# Load the OpenAI API key from the .env file
load_dotenv()
apikey = os.getenv("key")
openai.api_key = apikey

# Initialize SQLite database
conn = sqlite3.connect("prompts_responses.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt TEXT,
        response TEXT
    )
''')
conn.commit()

# Function to get completion from OpenAI
def get_completion():
    prompt = input_text.get("1.0", tk.END).strip()
    if not prompt:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a prompt.")
        return

    try:
        # Using gpt-3.5-turbo (ChatCompletion API) with increased max_tokens
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,  # Increased max_tokens for longer responses
            temperature=0.7  # Set temperature for response variability
        )
        output = response.choices[0].message.content.strip()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)

        # Save the prompt and response to the database
        save_to_db(prompt, output)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")

# Function to save prompt and response to the database
def save_to_db(prompt, response):
    cursor.execute("INSERT INTO history (prompt, response) VALUES (?, ?)", (prompt, response))
    conn.commit()

# Function to clear both input and output text boxes
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Function to show history of prompts and responses
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Prompt History")

    # Retrieve data from the database
    cursor.execute("SELECT prompt, response FROM history ORDER BY id DESC")
    records = cursor.fetchall()

    if not records:
        history_label = tk.Label(history_window, text="No history found.")
        history_label.pack()
    else:
        for prompt, response in records:
            prompt_label = tk.Label(history_window, text=f"Prompt: {prompt}")
            prompt_label.pack()
            response_label = tk.Label(history_window, text=f"Response: {response}")
            response_label.pack()
            separator = tk.Label(history_window, text="-"*50)
            separator.pack()

# Create the GUI application
root = tk.Tk()
root.title("OpenAI Chat Completion App")

# Input text box
input_label = tk.Label(root, text="Enter your prompt:")
input_label.pack()

input_text = tk.Text(root, height=40, width=200)
input_text.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_completion)
submit_button.pack()

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack()

# History button
history_button = tk.Button(root, text="History", command=show_history)
history_button.pack()

# Output text box
output_label = tk.Label(root, text="Output:")
output_label.pack()

output_text = tk.Text(root, height=40, width=200)
output_text.pack()

# Run the GUI application
root.mainloop()

# Close the database connection when the application is closed
conn.close()
