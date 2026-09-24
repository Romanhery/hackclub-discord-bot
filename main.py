# impo
import asyncio
import json
import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from github import Auth, Github

# This loads the enviornment file
load_dotenv()

# This authorizes the token
auth = Auth.Token(os.getenv("GITHUB_TOKEN"))


# Creates Client class and passes through the bot commands
class Client(commands.Bot):
    # Whenever ready
    async def on_ready(self):
        print(f"logged on as {self.user}!")

        try:
            # Allows only on our discord server
            guild = discord.Object(id=1548789188487417956)
            # Syncs the commands
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
        except Exception as e:
            print(f"Error syncing commands: {e}")


# Intentions/permission set to default
intents = discord.Intents.default()
# allows messages
intents.message_content = True
# depreciated thing but still need to have
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1548789188487417956)


# Slash command for adding a card to the gallery
# function for adding card to gallery takes in parameters title link and img
@client.tree.command(
    name="add-gallery", description="Adds to the gallery!", guild=GUILD_ID
)
async def add_Gallery(
    interaction: discord.Interaction,
    title: str,
    link: str,
    img: str,
    description: str,
):
    # sends confirmation message
    embed = discord.Embed(
        title=title,
        description="This project is added to the gallery!",
        url=link,
        color=discord.Color.red(),
    )

    embed.set_author(name=interaction.user.name)
    embed.add_field(name="Title", value=title)
    embed.add_field(name="Description", value=description)
    embed.set_thumbnail(
        url="https://antelope-hackclub.vercel.app/assets/logo.svg"
    )
    embed.set_image(url=img)
    embed.set_footer(text="Integrated by yours truly 😉")

    await interaction.response.send_message(embed=embed)

    def pushGit():
        g = Github(auth=auth, lazy=True, api_version="2022-11-28")

        # get the repo
        repo = g.get_repo("Romanhery/Antelope-Hackclub-Website")

        # get the current content
        contents = repo.get_contents("assets/JSON/gallery.json", ref="main")

        # decode it into something it can read
        current_content = contents.decoded_content.decode("utf-8")

        # puts the content into a variable
        data = json.loads(current_content) if current_content.strip() else []

        # gallery card template
        new_gallery_card = {"name": title, "link": link, "image": img}

        # add the new card
        data.append(new_gallery_card)

        # parsted content and full finished
        updated_text = json.dumps(data, indent=2)

        # update the repo with the data
        repo.update_file(
            path=contents.path,
            message="feat: update gallery",
            content=updated_text,
            sha=contents.sha,
            branch="main",
        )

    await asyncio.to_thread(pushGit)


@client.tree.command(
    name="add-guide", description="Adds to the guides", guild=GUILD_ID
)
async def addGuide(
    interaction: discord.Interaction, title: str, link: str, img: str
):
    # sends confirmation message
    embed = discord.Embed(
        title=title,
        description="This project is added to the tutorials page!",
        url=link,
        color=discord.Color.red(),
    )

    embed.set_author(name=interaction.user.name)
    embed.add_field(name="Title", value=title)
    embed.set_thumbnail(
        url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRc9rIJuST9RVsvigsumo2Y0gWjeSUL3XxU8UST_mYZ6w&s"
    )
    embed.set_image(url=img)
    embed.set_footer(text="Integrated by yours truly 😉")

    await interaction.response.send_message(embed=embed)

    def pushGit():
        g = Github(auth=auth, lazy=True, api_version="2022-11-28")

        # get the repo
        repo = g.get_repo("Romanhery/Antelope-Hackclub-Website")

        # get the current content
        contents = repo.get_contents("assets/JSON/guides.json", ref="main")

        # decode it into something it can read
        current_content = contents.decoded_content.decode("utf-8")

        # puts the content into a variable
        data = json.loads(current_content) if current_content.strip() else []

        # gallery guide template
        new_guide_card = {"name": title, "link": link, "image": img}

        # add the new card
        data.append(new_guide_card)

        # parsted content and full finished
        updated_text = json.dumps(data, indent=2)

        # update the repo with the data
        repo.update_file(
            path=contents.path,
            message="feat: update guides",
            content=updated_text,
            sha=contents.sha,
            branch="main",
        )

    await asyncio.to_thread(pushGit)


# run the discord bot
client.run(os.getenv("CLIENT_ID"))