import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "MTQ2NzQwOTcwMTM4NDc1MzMwNg.G5Ympf.L3rpxpZRQshZsUwd-bnpEAeORNIKRi0zWP6ioA"  # Pega tu token aquí
GUILD_ID = 1445918416585359443  # ID de tu servidor
ALLOWED_ROLES = ["staff", "Head of Staff", "Administrator", "Management", "Executive", "OWNER"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# ----------------------
# Evento al conectar
# ----------------------
@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)
    print(f"Logged in as {bot.user}")

# ----------------------
# Manejo de errores para permisos
# ----------------------
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingAnyRole):
        await interaction.response.send_message(
            "❌ You don't have permission to use this command!", ephemeral=True
        )

# ----------------------
# Slash Commands
# ----------------------

# /unreg
@bot.tree.command(name="unreg", description="You have 5 minutes to do the UNREG!")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def unreg(interaction: discord.Interaction):
    await interaction.response.send_message("You have 5 minutes to do the UNREG!")

# /fills
@bot.tree.command(name="fills", description="We're looking for some fills")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def fills(interaction: discord.Interaction):
    embed = discord.Embed(
        description="⏰ **We're looking for some fills. Type `f` below to join as a fill!** ⏰",
        color=discord.Color.orange()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1467429030604312598/1467440373499691019/image.png")
    await interaction.response.send_message(embed=embed)

# /fill
@bot.tree.command(name="fill", description="React for the 2nd lobby!")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def fill(interaction: discord.Interaction):
    await interaction.response.send_message("⚡ React below to join the 2nd lobby instantly! ✅")

# /sessionorganizer
@bot.tree.command(name="sessionorganizer", description="Session Organizer info")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def sessionorganizer(interaction: discord.Interaction):
    await interaction.response.send_message("Session Organizer:")

# /firstgame
@bot.tree.command(name="firstgame", description="Set leaderboard and start time of first game")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
@app_commands.describe(leaderboard="Leaderboard name", start_time="Time when first game starts")
async def firstgame(interaction: discord.Interaction, leaderboard: str, start_time: str):
    embed = discord.Embed(title="First Game", color=discord.Color.green())
    embed.add_field(name="Leaderboard", value=leaderboard, inline=False)
    embed.add_field(name="Start Time", value=start_time, inline=False)
    await interaction.response.send_message(embed=embed)

# /game
@bot.tree.command(name="game", description="Start or end a game session")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
@app_commands.describe(option="1 = GAME STARTED, 2 = SESSION FINISHED")
async def game(interaction: discord.Interaction, option: str):
    if option == "1":
        embed = discord.Embed(title="GAME STARTED!", color=discord.Color.green())
        embed.set_image(url="https://cdn.discordapp.com/attachments/1467429032428835000/1467438529553498320/image.png")
        await interaction.response.send_message(embed=embed)
    elif option == "2":
        embed = discord.Embed(title="SESSION FINISHED!", color=discord.Color.red())
        embed.set_image(url="https://cdn.discordapp.com/attachments/1467429032428835000/1467439064788766906/image.png")
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("❌ Invalid option! Use 1 or 2", ephemeral=True)

# /sessioncancel
@bot.tree.command(name="sessioncancel", description="Cancel the session")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def sessioncancel(interaction: discord.Interaction):
    embed = discord.Embed(
        description="❤️ **THE SESSION HAS BEEN CANCELLED. THANKS FOR PLAYING!** ❤️",
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)

# /maprules
@bot.tree.command(name="maprules", description="Show map rules")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def maprules(interaction: discord.Interaction):
    rules = (
        "These are the map rules:\n"
        "- No more than 8 cons on the map.\n"
        "- If a spot is marked for you, you stay there."
    )
    await interaction.response.send_message(rules)

# /maplink
@bot.tree.command(name="maplink", description="Provide the map link")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
@app_commands.describe(link="Link to the map")
async def maplink(interaction: discord.Interaction, link: str):
    embed = discord.Embed(
        title="Map Link",
        description=f"Here is the map link:\n{link}",
        color=discord.Color.purple()
    )
    await interaction.response.send_message(embed=embed)

# /end
@bot.tree.command(name="end", description="End the session")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def end(interaction: discord.Interaction):
    await interaction.response.send_message("This is the end of the session, stay tuned for the next regs!")

# /commands
@bot.tree.command(name="commands", description="List all bot commands")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def commands_list(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Sweaty Customs Commands",
        description=(
            "/unreg - Unregister yourself from the session\n"
            "/fills - Show available fills\n"
            "/fill ⚡ - React to join 2nd lobby instantly\n"
            "/sessionorganizer - Session Organizer info\n"
            "/firstgame <leaderboard> <time> - Set first game info\n"
            "/game 1 / 2 - Start or end a game session\n"
            "/sessioncancel - Cancel the session\n"
            "/maprules - Show map rules\n"
            "/maplink <link> - Provide map link\n"
            "/end - End the session\n"
            "/dash - Open tournament dashboard"
        ),
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

# /dash
@bot.tree.command(name="dash", description="Open the tournament dashboard")
@app_commands.checks.has_any_role(*ALLOWED_ROLES)
async def dash(interaction: discord.Interaction):
    await interaction.response.send_message("https://dash.yunite.xyz/guilds/1445918416585359443/manage/tournaments")

# ----------------------
# Run the bot
# ----------------------
bot.run(TOKEN)








