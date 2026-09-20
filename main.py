import discord
from discord.ext import commands
from discord import app_commands
from github import Github
from github import Auth
import os
import json
from dotenv import load_dotenv
load_dotenv()

auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

class Client(commands.Bot):
    async def on_ready(self):
        print(f'logged on as {self.user}!')

        try:
            guild = discord.Object(id=1548789188487417956)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}') 
    

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1548789188487417956)

@client.tree.command(name="add-gallery", description="Adds to the gallery!",guild=GUILD_ID)
async def add_Gallery(interaction: discord.Interaction, title:str , link:str , img: str):
    await interaction.response.send_message(f'Adding {title} to the gallery!')

    g = Github(auth=auth, lazy=True, api_version="2022-11-28")
    repo = g.get_repo("Romanhery/Antelope-Hackclub-Website")

    contents = repo.get_contents("assets/gallery.json", ref="main")
    current_content = contents.decoded_content.decode('utf-8')

    data = json.loads(current_content) if current_content.strip() else []

    new_gallery_card = {
        "name": title,
        "link" : link,
        "image" : img
    }

    data.append(new_gallery_card)

    updated_text = json.dumps(data, indent=2)

    repo.update_file(
            path=contents.path,
            message="feat: update gallery",
            content=updated_text,
            sha=contents.sha,
            branch="main"
    )
 
client.run(os.getenv("CLIENT_ID"))