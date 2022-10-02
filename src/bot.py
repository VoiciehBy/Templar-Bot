import discord as d
import discordUtils as dU

from discord import app_commands

import botClient as bC
import setupLogging as sL
import constants as c
import asyncio as a

theIntents = d.Intents.default()
theIntents.message_content = True
botClient = bC.botClient(intents=theIntents)


async def main():
    await sL.setupLogging()
    await botClient.start(token=c.BOT_TOKEN, reconnect=True)


a.run(main())