# LightMyRoom Discord Bot

LightMyRoom is a Discord bot that allows users to control Alexa-compatible smart lights through Discord reactions. It provides a simple, intuitive interface for changing light modes in your room directly from a Discord server.

## Features

- Control smart lights through Discord reactions
- Persistent menu for easy access to light controls
- Multiple light modes: red, blue, rave, normal, and off
- Displays current light mode and duration
- Logging of all light mode changes

## Requirements

- Python 3.7+
- Discord Bot Token
- [Virtual Smart Home](https://www.virtualsmarthome.xyz/url_routine_trigger) account
- Amazon Alexa
- Alexa-compatible smart lights
- Alexa routines set up for each light mode

## Dependencies

- nextcord
- requests

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/lightmyroom-discord-bot.git
   cd lightmyroom-discord-bot
   ```

2. Install the required Python packages:
   ```
   pip install nextcord requests
   ```

3. Set up your Virtual Smart Home account and create URL triggers for each light mode.

4. Create Alexa routines for each light mode, triggered by the Virtual Smart Home URL triggers.

5. Create a `config.json` file in the project root directory with the following structure:
   ```json
   {
    "red": "UUID_FOR_RED_MODE",
    "blue": "UUID_FOR_BLUE_MODE",
    "rave": "UUID_FOR_RAVE_MODE",
    "normal": "UUID_FOR_NORMAL_MODE",
    "off": "UUID_FOR_OFF_MODE"
   }
   ```
   Replace `UUID_FOR_X_MODE` with the corresponding UUID from your Virtual Smart Home URL triggers.
   For example everything after 'trigger=' in the link provided by the site.  

7. Update the `BASE_URL` constant in the `lightmyroom.py` file if necessary:
   ```python
   BASE_URL = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger="
   ```

8. (Optional) Replace the default light icon URL in the `create_lights_embed` function with your own icon:
   ```python
   embed.set_author(name="LightMyRoom", icon_url="https://example.com/your_light_icon.png")
   ```

## Usage

1. Start the bot:
   ```
   python lightmyroom.py
   ```

2. In your Discord server, use the command `!lights` to bring up the light control menu.

3. React to the menu message with the appropriate emoji to change the light mode:
   - 🔴 : Red mode
   - 🔵 : Blue mode
   - 🎉 : Rave mode
   - 💡 : Normal mode
   - 🌙 : Off

4. The bot will update the menu message to show the current mode and how long it's been active.

## Customization

### Adding New Light Modes

1. Add a new UUID to your `config.json` file under the `light_modes` object.

2. Update the `get_emoji_for_mode` and `get_mode_from_emoji` functions in `lightmyroom.py` to include an emoji for your new mode:

   ```python
   def get_emoji_for_mode(mode):
       emoji_map = {
           "red": "🔴",
           "blue": "🔵",
           "rave": "🎉",
           "normal": "💡",
           "off": "🌙",
           "your_new_mode": "🆕"  # Add your new mode here
       }
       return emoji_map.get(mode, "❓")

   def get_mode_from_emoji(emoji):
       emoji_map = {
           "🔴": "red",
           "🔵": "blue",
           "🎉": "rave",
           "💡": "normal",
           "🌙": "off",
           "🆕": "your_new_mode"  # Add your new mode here
       }
       return emoji_map.get(emoji, None)
   ```

3. Create a new Alexa routine for your new mode, triggered by the corresponding Virtual Smart Home URL.

### Changing the Command Prefix

To change the command prefix from `!`, update the `command_prefix` parameter when initializing the `Bot`:

```python
bot = commands.Bot(command_prefix='YOUR_PREFIX_HERE', intents=intents)
```

## Logging

The bot logs all light mode changes and any errors to a file named `lightmyroom.log` in the same directory as the script. You can adjust the logging configuration in the `logging.basicConfig()` call at the beginning of the script.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is not affiliated with Amazon Alexa or Virtual Smart Home. Use at your own risk.

## Support

If you encounter any problems or have any questions, please open an issue in this repository.
```

This README provides a comprehensive guide for setting up and using the LightMyRoom Discord bot. It includes all the necessary information about requirements, setup, usage, and customization.

Remember to update the versions to the latest stable releases when you create your repository.

Lastly, here's an example `config.json` file:

```json
{
    "red": "UUID_FOR_RED_MODE",
    "blue": "UUID_FOR_BLUE_MODE",
    "rave": "UUID_FOR_RAVE_MODE",
    "normal": "UUID_FOR_NORMAL_MODE",
    "off": "UUID_FOR_OFF_MODE"
   }
```

Replace `YOUR_DISCORD_BOT_TOKEN_HERE` with your actual Discord bot token, and each UUID with the actual UUIDs from your Virtual Smart Home URL triggers.
