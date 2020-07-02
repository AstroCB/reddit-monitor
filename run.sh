#! /bin/bash

# Run script from BotCore examples

if (node login.js) then
    # Can remove stored JS appstate if Python conversion successful
    rm appstate.json
    # Start up the fbchat bot (stored in bot.py) and pass in any provided args
    python3 bot.py $@
else
    echo "Login/conversion from BotCore failed"
    exit 1
fi