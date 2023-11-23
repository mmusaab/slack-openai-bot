import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from dotenv import find_dotenv, load_dotenv
from flask import Flask, request
from functions import openAICall, draftEmail, makeJiraTask, birthdayWish

# # Load environment variables from .env file
load_dotenv(find_dotenv())

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
SLACK_BOT_USER_ID = os.environ["SLACK_BOT_USER_ID"]

# Initialize the Slack app
app = App(token=SLACK_BOT_TOKEN)

# Initialize the Flask app
# Flask is a web application framework written in Python
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@app.event("app_mention")
def handle_mentions(body, say):
    """
    Event listener for mentions in Slack.
    When the bot is mentioned, this function processes the text and sends a response.

    Args:
        body (dict): The event data received from Slack.
        say (callable): A function for sending a response to the channel.
    """
    text = body["event"]["text"]
    user_id = body["event"]["user"]
    channel_id = body["event"]["channel"]

    mention = f"<@{SLACK_BOT_USER_ID}>"
    text = text.replace(mention, "").strip()

    slack_client = WebClient(token=SLACK_BOT_TOKEN)
    slack_client.chat_postEphemeral(
        channel=channel_id,
        user=user_id,
        text="Bot is thinking... :thinking_face:"
    )                   

    if text.find('[email]') == 0:
        response = draftEmail(text.replace('[email]', ''), user_id)
    elif text.find('[jira]') == 0:
        response = makeJiraTask(text.replace('[jira]', ''), user_id)
    elif text.find('[birthday]') == 0:
        response = birthdayWish(text.replace('[birthday]', ''), user_id)
    elif text.find('[list]') == 0:
        response = listCommands()
    elif text.lower() in['hi','hello', 'hey','hii', 'ji'] and len(text) < 6:
        response = helloResponce()
    else:
        response = openAICall(text, user_id)

    say(f"<@{user_id}>, "+response)

def helloResponce():
    template = """ Hi, How can i help you? 

    You can type [list] to get the more ways to work with me.
    
    """
    return template

def listCommands():
    template = """
    These are the list of custom "HOT WORDS" you can use with you question, to ask me specifically with predefined prompts.

    [birthday]
    [email]
    [jira]

    i.e [birthday] makes a funny birthday wish to Aziz
    
    """
    return template

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    """
    Route for handling Slack events.
    This function passes the incoming HTTP request to the SlackRequestHandler for processing.

    Returns:
        Response: The result of handling the request.
    """
    return handler.handle(request)


# Run the Flask app
if __name__ == "__main__":
    flask_app.run(host="localhost", port=5001, debug=False)
