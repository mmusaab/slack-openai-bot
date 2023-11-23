# slack-openai-bot

Signup openai api and put the api key in env file
https://platform.openai.com/usage

Part 1: Slack Setup

Step 1: Create a new Slack app
Choose an existing Slack workspace or create a new one.
Go to https://api.slack.com/apps and sign in with your Slack account. 
Click "Create New App" and provide an app name and select your workspace as the development workspace. Click "Create App".

Step 2: Set up your bot
Under the "Add features and functionality" section, click on "Bots". 
Click "Add a Bot User" and fill in the display name and default username. Save your changes.

Step 3: Add permissions to your bot
In the left sidebar menu, click on "OAuth & Permissions". 
Scroll down to "Scopes" and add the required bot token scopes. For this example, you'll need at least app_mentions:read, chat:write, and channels:history.

Step 4: Install the bot to your workspace
In the left sidebar menu to go basic information and click on "Install App". 
Click "Install App to Workspace" and authorize the app.

Step 5: Retrieve the bot token
After installation, go back to “OAuth & Permissions" page. 
Copy the "Bot User OAuth Access Token" (it starts with xoxb-). You'll need it for your Python script.

Part 2: Python setup

Step 1: Set up your Python environment
Install Python 3.6 or later (if you haven't already). 
Install the required packages: slack-sdk, slack-bolt, and Flask. You can do this using pip:

Create virtual envirment using Conda
conda create --name myenv python=3.8
conda activate myenv
pip install slack-sdk slack-bolt Flask

Add 2 files app.py and functions.py

Step 3: Set the environment variable in the .env file
Create a .env file in your project directory and add the following keys:

SLACK_BOT_TOKEN = "xoxb-your-token"
SLACK_SIGNING_SECRET = "your-secret"
SLACK_BOT_USER_ID = "your-bot-id"
OPENAI_API_KEY= "your-openai-key"
Step 4: Start your local Flask server

Run the Python script in the terminal (macOS/Linux) or Command Prompt (Windows): python app.py The server should start, and you'll see output indicating that it's running on http://127.0.0.1:5001/.

Part 3 — Server Setup (Local)

Step 1: Use ngrok and run it on port 5001

Step 2: Configure your Slack app with the ngrok URL
Go back to your Slack app settings at https://api.slack.com/apps. 
Click on "Event Subscriptions" in the left sidebar menu.
Enable events and enter your ngrok URL followed by /slack/events (e.g., https://yoursubdomain.ngrok.io/slack/events).
Scroll down to "Subscribe to bot events" and click "Add Bot User Event". Add the app_mention event and save your changes.
Please note that every time you restart ngrok in the terminal, you have to update the URL in Slack — this is just for testing.

Step 3: Reinstall your Slack app to update the permissions
In the left sidebar menu, click on "Install App". 
Click "Reinstall App to Workspace" and authorize the app.

Step 4: Add your bot to a Slack channel
Type /invite @bot-name in the channel.
