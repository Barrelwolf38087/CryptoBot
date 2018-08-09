# CryptoBot
A Discord bot for comparing cryptocurrency values.
Data from [CryptoCompare](https://www.cryptocompare.com/)


## Dependencies
- Python 3.6 (or newer)
    - [Get it here](https://www.python.org/downloads/)
- Discord.py (obviously)
    - `python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip`
- Requests
    - `python3 -m pip install requests`


## Self-Hosting Instructions
1. Create a bot [here](https://discordapp.com/developers/applications/me).
2. Paste your bot's token into a file called "token.txt".
    * Ensure there is no newline at the end of the file.
    * On *NIX, try `tr -d '\n' < token.txt`
    * If there is a newline at the end, the bot will fail to log in and you will get a cryptic error.
3. Run the bot.
4. Invite the bot to your server using your generated OAuth2 URL.
    * Make sure the bot has the permissions to send messages and embed links.
