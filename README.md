# Hackclub Discord Bot

This is a discord bot that allows my club's members to easily and seamlessly add their own projects to our gallery in our website without me or them having to touch the code

## How to test my discord bot!

-  To test it out first go to the website and join the discord server at https://discord.gg/8ZpQntd3Y
- Then go to the gallery channel
- After that type in `/add-gallery`
- Then it is going to have some parameters : `title` , `link` the url of the project , `img` the url of the image, and `description` its just for the embed
- When you enter it is going to show something like this ![emebed](https://github.com/Romanhery/hackclub-discord-bot/blob/e4cc407cf9f5b4864fe28a41391ea43a4af166c1/assets/embed.png)
- Now if you checkout the website you are going to see your project! ![emebed](https://github.com/Romanhery/hackclub-discord-bot/blob/master/assets/project.png)




## Features
- Fully Autonomous
- You can add your projects easily into our club's website
- Works only on servers explicity chosen by you!

## Clone the Repo
```bash
git clone https://github.com/Romanhery/hackclub-discord-bot
cd hackclub-discord-bot
```

## Make .env file and populate with credentials
```bash
cat << 'EOF' > .env
CLIENT_ID=""
GITHUB_TOKEN=""
GUILD_ID=
EOF
```

## Run it !
```bash
python3 main.py
```

## Built with
Python 
Discord.js
PyGithub
