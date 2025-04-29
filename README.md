# Slack-Chatbot
a slack chatbot follow through tutorial using multiple websites i dont even remember and chatgpt of course and all this + 6 hours to end with the most mid chatbot ever that barely works (it doesn't work). kjsadh laiucnhein5w8yv)fgnjdksgblkdfjhvbsn jkncihlgvkuhgmckshnvmdskcvns humafuckshistsaknkm cthe ufivahmcccjaapievctaofshitshit


# Slack Bot

This is a simple Slack bot that listens for direct mentions and responds to specific commands.

## Tools and Libraries

### os
- **Purpose**: Interacts with the operating system.
- **Usage**: Accesses environment variables to retrieve sensitive information like tokens.

### re
- **Purpose**: Provides support for regular expressions.
- **Usage**: Parses and matches patterns in strings, particularly for extracting direct mentions and commands from messages.

### time
- **Purpose**: Handles time-related tasks.
- **Usage**: Pauses the execution of the program to maintain a connection with Slack.

### slack_sdk
- **Purpose**: Interacts with the Slack API.
- **Components**:
  - **WebClient**: Sends messages and interacts with Slack's Web API.
  - **SocketModeClient**: Establishes real-time communication with Slack using Socket Mode.
  - **SlackApiError**: Handles errors that occur during API calls.

### dotenv
- **Purpose**: Loads environment variables from a `.env` file.
- **Usage**: Manages sensitive information like tokens securely.

## Key Components

- **Environment Variables**:
  - `SLACK_BOT_TOKEN` and `SLACK_APP_TOKEN` are loaded from a `.env` file to authenticate and authorize the bot with Slack.

- **Slack Clients**:
  - **WebClient**: Used to send messages and interact with Slack's Web API.
  - **SocketModeClient**: Used to establish a real-time connection with Slack using Socket Mode.

- **Regular Expressions**:
  - Used to parse direct mentions in messages, identifying when the bot is mentioned and extracting commands.

- **Event Handling**:
  - Functions like `parse_bot_commands`, `parse_direct_mention`, and `handle_command` are used to process incoming events, extract commands, and respond appropriately.

- **Main Loop**:
  - The bot runs in an infinite loop, maintaining a connection to Slack and processing events as they come in.

## Contact

For any questions or issues, please open an issue on this repository or contact the maintainer.

