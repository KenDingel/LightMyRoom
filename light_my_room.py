import nextcord
from nextcord.ext import commands
import requests
import json
import datetime
import logging

# Set up logging
logging.basicConfig(filename='lightmyroom.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Bot setup
intents = nextcord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Constants
BASE_URL = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger="

# Load UUIDs from JSON file
with open('light_modes.json', 'r') as f:
    LIGHT_MODES = json.load(f)

# Global variables
last_mode = None
last_activation_time = None
menu_message = None

@bot.event
async def on_ready():
    print(f"LightMyRoom is ready to illuminate! 💡")
    logging.info("Bot started")

@bot.event
async def on_message(message):
    global menu_message
    if message.author == bot.user:
        return

    if message.content.lower() == '!lights':
        if menu_message:
            await menu_message.delete()
        
        embed = create_lights_embed("LightMyRoom Control Panel")
        menu_message = await message.channel.send(embed=embed)
        
        for mode in LIGHT_MODES.keys():
            await menu_message.add_reaction(get_emoji_for_mode(mode))

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    if reaction.message.id == menu_message.id:
        mode = get_mode_from_emoji(str(reaction.emoji))
        if mode:
            await set_light_mode(reaction.message, mode)
        await reaction.remove(user)

async def set_light_mode(message, mode: str):
    global last_mode, last_activation_time

    url = BASE_URL + LIGHT_MODES[mode]
    response = requests.get(url)
    
    if response.status_code == 200:
        last_mode = mode
        last_activation_time = datetime.datetime.now()
        logging.info(f"Activated mode: {mode}")
        
        embed = create_lights_embed("LightMyRoom Control Panel", f"{mode.capitalize()} mode activated!")
        await message.edit(embed=embed)
    else:
        embed = create_lights_embed("LightMyRoom Control Panel", f"Failed to activate {mode} mode")
        await message.edit(embed=embed)
        logging.error(f"Failed to activate mode: {mode}")

def create_lights_embed(title, description=None):
    embed = nextcord.Embed(title=title, description=description, color=0xFFFFFF)
    embed.set_author(name="Moon's Light Bot", icon_url="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGFpcTBtejh2eHFnbGI5d2NxY2U4cHJzcnUxc2ptOGQ4dG95ODNmbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1YcHowZ380eNFmVfUl/giphy.webp")
    embed.set_footer(text="Control Moon's Lights! _ 2024")
    embed.timestamp = datetime.datetime.utcnow()

    if last_mode:
        embed.add_field(name="Current Mode", value=f"{get_emoji_for_mode(last_mode)} {last_mode.capitalize()}", inline=True)
        time_since = datetime.datetime.now() - last_activation_time
        embed.add_field(name="Active for", value=str(time_since).split('.')[0], inline=True)

    embed.add_field(name="Available Modes", value="\n".join([f"{get_emoji_for_mode(mode)} {mode.capitalize()}" for mode in LIGHT_MODES.keys()]), inline=False)

    return embed

def get_emoji_for_mode(mode):
    emoji_map = {
        "red": "🔴",
        "blue": "🔵",
        "rave": "🎉",
        "normal": "💡",
        "off": "🌙"
    }
    return emoji_map.get(mode, "❓")

def get_mode_from_emoji(emoji):
    emoji_map = {
        "🔴": "red",
        "🔵": "blue",
        "🎉": "rave",
        "💡": "normal",
        "🌙": "off"
    }
    return emoji_map.get(emoji, None)

# Run the bot
bot.run('')
