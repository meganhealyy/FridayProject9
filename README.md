# FridayProject9- Python GUI Prompt App
This Python project features a simple GUI that lets users enter a prompt, submit it, and view the response using an API call. The API key is securely stored in a .env file.

To use this program, clone the repository in your chosen code editor (e.g. Visual Studio Code). You should be able to view the following files:
(1) main.py
(2) README.md
(3) .git.ignore
(4) .env_example.py

The API key is secured in a .env file so other users can not see it. In order to run the code, you must get your own API key and make your own .env file. The title of the file is simply '.env'. To get an API code, go to the OpenAI website. Under the 'Products' dropdown, select 'API Login'. After logging in, select 'Dashboard' and go down to 'API Keys' on the left side of the screen. From there, you should be able to select 'Create A New Key'. After creating it, copy it. If you are unable to copy it, you must create a new key. Follow the template in the '.env_example.py' file.

The user also must have the openai module installed on your machine to run this code. After entering your prompt in the input text box, hit the 'Submit' button, and the response will be shared in the output text box. The user can clear the text boxes and enter a new prompt by hitting the 'Clear' button. The user can also access previous prompts and responses by clicking the 'History' button. 

