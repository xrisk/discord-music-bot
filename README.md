# discord-music-bot

**What?**

A bare-bones Discord bot for playing music in voice channels.

*Commands:*

| Command             | Description                          |
| --------------------|-------------------------|
| `]] <youtube link>` | Plays the video         |
| `]] skip`           | Skips the current song  |

## Why?

Why not?

## How?

1. Create a new Discord application at [Discord's developer portal](https://discordapp.com/developers/applications/).
2. Create a bot user for your application and get the bot token (*not the client secret*).
3. Create an OAuth URL for your bot with scope as "bot" and voice-related permissions. (Redirect URL is not necessary)
4. Enable "Developer Mode" in Appearance settings in the Discord application. Right click on the voice channel you want the bot to join and copy its channel ID.
5. Edit `config.py`. `DISCORD_KEY` is the bot token and `DISCORD_CHANNEL` is the channel ID.
6. Clone this repository.
7. Run: `docker built -t musicbot .` from inside this repository.
8. `docker run musicbot` will start your bot.
9. You can use the `-d` option on `docker run` to make it run as a background process.

## Things to do

* Proper queue management
* Permissions system
* Search and suggestions