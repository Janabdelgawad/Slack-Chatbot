import os
import re
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

# Initialize Slack clients
web_client = WebClient(token=SLACK_BOT_TOKEN)
socket_mode_client = SocketModeClient(app_token=SLACK_APP_TOKEN, web_client=web_client)

# Constants
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(events):
    for event in events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)
    response = None
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    try:
        web_client.chat_postMessage(channel=channel, text=response or default_response)
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")

def process(client: SocketModeClient, req: SocketModeRequest):
    if req.type == "events_api":
        event = req.payload["event"]
        command, channel = parse_bot_commands([event])
        if command:
            handle_command(command, channel)
        client.send_socket_mode_response(envelope_id=req.envelope_id)

if __name__ == "__main__":
    socket_mode_client.socket_mode_request_listeners.append(process)
    socket_mode_client.connect()
    print("Starter Bot connected and running!")
    while True:
        time.sleep(1)

