import json
import os

import discord

client = discord.Client()

# Load data from JSON file
if os.path.exists('levels.json'):
    with open('levels.json', 'r') as f:
        levels = json.load(f)
else:
    levels = {}

# Save data to JSON file
def save_levels():
    with open('levels.json', 'w') as f:
        json.dump(levels, f)

# Increment the user's level and return whether or not the user advanced a level
def add_exp(user_id, exp):
    if user_id not in levels:
        levels[user_id] = {'exp': 0, 'level': 1}
    levels[user_id]['exp'] += exp
    if levels[user_id]['exp'] >= levels[user_id]['level'] * 100:
        levels[user_id]['exp'] = 0
        levels[user_id]['level'] += 1
        return True
    return False

# Give the user a role based on their level
def give_role(user, role_levels):
    for role, level in role_levels.items():
        if levels[user.id]['level'] >= level and role not in [r.name for r in user.roles]:
            await user.add_roles(role)

# Level up message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.guild is None:
        return
    if message.content.startswith('/'):
        return

    # Add exp to user and check if they advanced a level
    advanced_level = add_exp(message.author.id, 1)
    if advanced_level:
        await message.channel.send(f'{message.author.mention} has advanced to level {levels[message.author.id]["level"]}!')

        # Give role based on level
        role_levels = {
            'Role 1': 5,
            'Role 2': 10,
            'Role 3': 15,
            'Role 4': 20
        }
        give_role(message.author, role_levels)

        save_levels()

    await client.process_commands(message)
