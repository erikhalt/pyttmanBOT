import logging
import os
from pathlib import Path

import chatbot.abilities.hello_world.ability
#from enviroment import DISCORD_TOKEN, DISCORD_GUILD

"""
    Welcome to the settings module! Please take a minute to read
    this little introduction, if it's your first time here.
    
    If you've used Django before, this is familiar to you and 
    you can stop reading now. If you haven't, that's okay too. 
    
    Everything in this file is available to you in your app 
    through 'pyttman.settings'. You can store things here, but
    be >>> very careful <<< not to push API tokens, 
    passwords or other sensitive details to version control. 
    This is why it's recommended to use .env or another form 
    of storing these sensitive credentials in your app, and 
    then using them here in this file with `os.getenv("my_api_token")` 
    for example.
"""

# Use this flag as 'if pyttman.settings.DEV_MODE:' for debugging purposes.
DEV_MODE = False


# Create a new log file for each time your app starts,
# or append the most recent one.
APPEND_LOG_FILES = True

# Configure the behavior of the MessageRouter here
MIDDLEWARE = {

    # The MessageRouter routes messages to your app's Intent classes.
    # To see the available classes and choose on that fits your app,
    # check out the documentation on GitHub.
    "ROUTER_CLASS": "pyttman.core.middleware.routing.FirstMatchingRouter",

    # Define a collection of strings to return to the user if no intent matched
    # the user's message. One is randomly chosen by the Router and returned to
    # the user.
    "COMMAND_UNKNOWN_RESPONSES": [
        "I'm sorry, I didn't understand. Try again! ",
        "Hmm.. I don't think I follow?"
    ],

    # Define the keyword for Pyttman's auto-generated help pages to be
    # displayed for a user, if they type this word in the beginning of
    # a message. The keyword is case insensitive and has to occur as
    # first string in the message from the user.
    "HELP_KEYWORD": "help",
    
    # This text is what will be returned to users if your app runs in to
    # a fatal error from which no Reply object could be returned to the client.
    # That is - in the worst thinkable scenario, this message should still
    # reach your users and hint to them that an error occurred, and your
    # app isn't simply ignoring them by keeping quiet.
    # In the log files of your Pyttman app, you can track down the error
    # by searching for the Error UUID written in chat when the error occurred.
    "FATAL_EXCEPTION_AUTO_REPLY": "I'm sorry, something went wrong. Try again" \
                                  " in a few moments."
}

# Define your Ability classes here, with path starting from your project
# directory.
# TIP! If you use PyCharm, you can right-click your Ability's class name
# and select "Copy / Paste Special" -> "Copy Reference" and paste it below.

# ABILITIES = ["my_app.abilities.filename.AbilityClassName"]
ABILITIES = ['chatbot.abilities.hello_world.ability.HelloWorld',
             ]


# Define the client which your Pyttman app uses as its front end here.
# There are Client classes available to use which Pyttman provides for you,
# and it's easy to develop a custom Client for your platform by subclassing
# the BaseClient class, and using it here. Provide the full reference to the
# client class under the 'class' key. Any other data in the dict will be
# passed as kwargs to your client.
#
# TIP! Unsure of what to put here?
# Check out the documentation:
# https://github.com/dotchetter/Pyttman/wiki/Clients
CLIENT = {
    "class": "pyttman.clients.community.discord.client.DiscordClient",
    "token": 'DISCORD_TOKEN',
    "guild": 'DISCORD_GUILD',
    "discord_intent_flags": {
        "message_content": True,
        "dm_messages": True,
        "guild_messages": True,
        "messages": True
    }
}
DATABASE = {
    ""
}
# No need to change this setting
APP_BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))

# No need to change this setting
LOG_FILE_DIR = APP_BASE_DIR / Path("logs")

# Set desired logging format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

LOG_TO_STDOUT = False

# This setting is set by pyttman-cli when you create your project.
# Do not change it afterwards without also renaming the directory
# for your app.

APP_NAME = "chatbot"
