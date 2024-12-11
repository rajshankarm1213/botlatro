import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import app_commands
import os
import makefun
import re
import asyncio
import api # Import the API script
import util # Import the utility script

RARITY_COLORS = util.RARITY_COLORS
MIN_DISTANCE = 0 # Minimum Levenshtein distance for a match
MAX_DISTANCE = 3 # Maximum Levenshtein distance for a match
SUB_URLS = {
    'jokers': 'Jokers',
    'decks': 'Decks',
    'tarot': 'Tarot_Cards',
    'spectral': 'Spectral_Cards',
    'planets': 'Planet_Cards',
    'vouchers': 'Vouchers',
    'enhancements': 'Card_Modifiers#Enhancements',
    'editions': 'Card_Modifiers#Editions',
    'seals': 'Card_Modifiers#Seals',
    'stakes': 'Stakes',
    'blinds': 'Blinds_and_Antes',
    'tags': 'Tags'
}
EMOJI_LIST = [f'{i}\u20e3' for i in range(1,6)] # List of number emojis
# Initialize bot
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.messages = True
bot = commands.Bot(command_prefix="$", intents=intents)

def find_closest_match(search_term):
        # Calculate the Levenshtein distance for each item in the dataframe
        category_names = SUB_URLS.keys()
        closest_matches = []
        for category in category_names:
            closest_matches.extend(util.find_closest_match(category, search_term))
        # Filter out matches with a distance greater than MAX_DISTANCE
        closest_matches = [(id, item, distance, category) for id, item, distance, category in closest_matches if distance <= MAX_DISTANCE]
        # Sort the matches by distance
        closest_matches = sorted(closest_matches, key=lambda x: x[2])
        # If distance of the first match is 0, return the match
        if closest_matches and closest_matches[0][2] == 0:
            return [closest_matches[0]]
        return closest_matches[:min(5, len(closest_matches))] # Return the top 5 matches or less



@bot.event
async def on_ready():
    print(f'Bot has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        # Define the regex patterns for the custom commands
    pattern = re.compile(r'<<(.+?)>>') # Pattern for custom commands

    match = pattern.search(message.content)
    if match:
        async with message.channel.typing():
            search_term = match.group(1)
            items = find_closest_match(search_term)
            if len(items) == 1:
                item = items[0]
                id = item[0]
                name = item[1]
                category = item[3]
                data = util.fetch_data(category+'_id', id)
                if category == 'jokers':
                    rarity = data['rarity'].values[0]
                else:
                    rarity = category
                img = data['image'].values[0]
                try:
                    desc = data['description'].values[0] # All but planets and jokers
                except:
                    if category == 'jokers':
                        desc = f'**Effect**: {data["effect"].values[0]}\n**Cost**: {data['cost'].values[0]}\n**Rarity**: {rarity}\n **Type**: {data["type"].values[0]}'
                    elif category == 'planets':
                        desc = f'**Addition**: {data["addition"].values[0]}\n**Hand**: {data["hand"].values[0]}\n**Hand Base Score**: {data["hand_base_score"].values[0]}'
                print(rarity)
                color = RARITY_COLORS.get(rarity.lower(), None)
                print(color)
                embed = discord.Embed(title=f"Item Details: {data['name'].values[0]}", color=color)
                embed.add_field(name="Name", value=name, inline=False)
                embed.add_field(name="Category", value=category.title(), inline=False)
                embed.add_field(name="Description", value = desc, inline=False)
                embed.set_thumbnail(url=img)
            else:
                embed = discord.Embed(title="Search Results",
                                    description=f"Found {len(items)} items matching '{search_term}'",
                                    color=discord.Color.blue())
                for _, name, _, category in items:
                    embed.add_field(name=name, value=f"Category: {category.title()}", inline=False)

        # Send the embed
        sent_message = await message.channel.send(embed=embed)

        # Add number reactions
        if len(items) > 1:
            for i in range(1, len(items) + 1):
                await sent_message.add_reaction(f"{i}\u20e3")


@bot.event
async def on_reaction_add(reaction, user):
    """
    Handles the interaction when a user reacts to a message.

    Parameters:
        reaction (discord.Reaction): The reaction added to a message.
        user (discord.User): The user who added the reaction.
    """
    # Ignore bot reactions
    if user.bot:
        return

    message = reaction.message
    if not message.embeds:
        return
    async with message.channel.typing():
        embed = message.embeds[0]
        emoji = reaction.emoji
        search_term = embed.description.split(" ")[-1].strip().replace("'", "")
        items = find_closest_match(search_term)
        if emoji in EMOJI_LIST:
            index = EMOJI_LIST.index(emoji)
            selected_item = items[index]
        # Create a new embed for the selected item
        id = selected_item[0]
        name = selected_item[1]
        category = selected_item[3]
        data = util.fetch_data(category+'_id', id)
        if category == 'jokers':
            rarity = data['rarity'].values[0]
        else:
            rarity = category
        img = data['image'].values[0]
        try:
            desc = data['description'].values[0] # All but planets and jokers
        except:
            if category == 'jokers':
                desc = f'**Effect**: {data["effect"].values[0]}\n**Cost**: {data['cost'].values[0]}\n**Rarity**: {rarity}\n **Type**: {data["type"].values[0]}'
            elif category == 'planets':
                desc = f'**Addition**: {data["addition"].values[0]}\n**Hand**: {data["hand"].values[0]}\n**Hand Base Score**: {data["hand_base_score"].values[0]}'
        color = RARITY_COLORS.get(rarity.lower(), None)
        new_embed = discord.Embed(title=f"Item Details: {data['name'].values[0]}", color=color)
        new_embed.add_field(name="Name", value=name, inline=False)
        new_embed.add_field(name="Category", value=category.title(), inline=False)
        new_embed.add_field(name="Description", value = desc, inline=False)
        new_embed.set_thumbnail(url=img)

    # Edit the original message with the new embed
    await message.edit(embed=new_embed)
    await reaction.message.remove_reaction(reaction.emoji, user)



@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def jeebie(ctx):
    await ctx.send("Hello Jeebie!")

@bot.tree.command(
    name="jeebie",
    description="My first application Command"
)
async def jeebie(interaction:discord.Interaction):
    await interaction.response.send_message("Hello Jeebie!")

# Helper function to create text commands
def create_text_command(command_name, description):
    @bot.command(name=command_name)
    async def text_command(ctx):
        func = getattr(api, f"{command_name}", None)
        if func:
            items = func()
            await ctx.send(f"{description}: {', '.join(items)}")
        else:
            await ctx.send(f"Fetching {description}...")

# Helper function to create slash commands
""" TODO: Slash commands in v2.0"""
def create_slash_command(command_name, description):
    @bot.tree.command(
        name=command_name,
        description=f"Fetch the latest {description}"
    )
    @makefun.with_signature(None, func_name=command_name)
    async def slash_command(interaction: discord.Interaction):
        await interaction.response.send_message(f"Fetching {description}...")


# Function to create text and slash commands dynamically
def create_commands():
    for command_name, description in SUB_URLS.items():
        create_text_command(command_name, description)
        #create_slash_command(command_name, description)

create_commands()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')   # Get the bot token from the environment
# Run the bot
bot.run(TOKEN)
