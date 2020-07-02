# reddit-monitor
reddit-monitor is a bot that can monitor a list of Reddit accounts and notify you via Facebook Messenger when they post or comment. It's written using [BotCore](https://github.com/AstroCB/BotCore) and [fbchat](https://github.com/carpedm20/fbchat).

## Usage
To use this bot, clone the repo and install the dependencies:

```
git clone https://github.com/AstroCB/reddit-monitor
cd reddit-monitor
npm install
pip install -r requirements.txt
```

Then, edit [the example config file](config.example.py) and fill in your desired information. Look [here](https://fbchat.readthedocs.io/en/stable/intro.html#threads) for information on finding thread IDs. Once you've done this, change the name of the file to `config.py` so that the bot will recognize it.

You'll also have to set up your BotCore environment variables in order to log in; see [the BotCore docs](https://github.com/AstroCB/BotCore/blob/master/DOCS.md#credentialsobj) for details.

To run the bot, use

```
./run
```

This will cause the bot to run infinitely, waiting for new posts/comments and alerting the configured Messenger thread as it finds them. I recommend using a process manager or `screen` to background this process.