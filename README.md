# RASA-Chatbot
Rasa is a context based leading conversational AI platform, I have used rasa to make a chatbot.
I have used rasa webchat (A chat widget to deploy virtual assistants made with Rasa.
![image](https://github.com/user-attachments/assets/fd05bf73-2e21-4731-b54e-7552e8bbb29f)

# Rasa Open Source
![image](https://github.com/user-attachments/assets/3ece1044-173e-45b5-b5cf-0141951bc7fc)

# Rasa is an open source machine learning framework to automate text-and voice-based conversations. With Rasa, you can build contextual assistants on:
- Facebook Messenger
- Slack
- Google Hangouts
- Webex Teams
- Microsoft Bot Framework
- Rocket.Chat
- Mattermost
- Telegram
- Twilio
- Your own custom conversational channels

Rasa helps you build contextual assistants capable of having layered conversations with lots of back-and-forth. In order for a human to have a meaningful exchange with a contextual assistant, the assistant needs to be able to use context to build on things that were previously discussed – Rasa enables you to build assistants that can do this in a scalable way.

# RASA installation guide
Here’s a step-by-step guide to installing Rasa, an open-source conversational AI platform, on your system:

Prerequisites:
Before installing Rasa, ensure you have the following:

1. Python 3.8+: Rasa requires Python 3.8 or above.
2. Pip: Ensure pip (Python's package manager) is installed.
3. Virtual Environment (Recommended): It’s a good idea to install Rasa in a virtual environment to avoid conflicts with other Python packages.

Step 1: Install Python and Pip

Step 2: Set Up a Virtual Environment 
- Create a virtual environment
  - python -m venv .\venv
- Activate the virtual Environment 
  - .\venv\Scripts\activate
    
Step 3: Install Rasa
- pip install rasa

Step 4: Initialize a New Rasa Project
- rasa init
  - This command will:
    - Create a new folder with the default project structure (including files like domain.yml, config.yml, and data/).
    - Provide an example chatbot that you can run immediately.
      
   You will be asked if you want to train the model. Press Y (Yes) to proceed. It will also train a simple NLU model and create example stories.

Step 6: Train the Model
- rasa train
  - This will train the NLU model and the dialogue management model.
 
Step 7: Run the Rasa Server
- Start the Rasa server to handle interactions with the bot. You can run the Rasa server with API capabilities like this:
- rasa run --enable-api --cors "*"
  - --enable-api: Enables the Rasa REST API.
  - -cors "*": Allows cross-origin requests from any domain (important when connecting from a frontend web page).
   
Step 8: Test Your Bot
- To test your bot directly from the command line, run:
  - rasa shell
  - You can then enter text and interact with your chatbot.

