import discord as d
from discord import app_commands
import discordUtils as dU
import constants as c
import goodThreads as gT
import utils as u
import asyncio as a


class botClient(d.Client):
    BOT_TXT_CHANNEL_ID = "0"
    SEARCH_PATTERNS = ["WW2", "WORLD WAR 2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await self.wait_until_ready()
        print(f"{self.user}" + c.HELLO)

    async def sendMessage(self, txt, guild):
        textChannels = dU.getGuildTextChannels(guild)
        theTxtChannel = dU.getTextChannelById(textChannels,
                                              self.BOT_TXT_CHANNEL_ID)
        if (theTxtChannel is not None):
            await theTxtChannel.send(txt)
        else:
            print(c.CANNOT_FIND_CHANNEL)

    async def checkForValgor(self, msg):
        if (msg.content.lower().startswith(c.TEST)):
            txt = msg.author.display_name
            if (str(msg.author.id) == c.VALGOR_ID):
                txt += c.IS_VALGOR
            else:
                txt += c.IS_NOT_VALGOR
            await self.sendMessage(txt, msg.guild)

    async def setChannel(self, msg):
        if (not (msg.content.startswith(c.SET_CHANNEL))):
            return

        i = len(c.SET_CHANNEL)
        channelName = msg.content[i:].strip()
        textChannels = dU.getGuildTextChannels(msg.guild)
        theTxtChannel = dU.getTextChannelByName(textChannels, channelName)
        self.BOT_TXT_CHANNEL_ID = theTxtChannel.id
        await self.sendMessage(c.CHANNEL_SET + channelName, msg.guild)

    async def setSearchPattern(self, msg):
        if (not (msg.content.startswith(c.SET_SEARCH_PATTERN))):
            return

        i = len(c.SET_SEARCH_PATTERN)
        searchPattern = msg.content[i:].strip()
        self.SEARCH_PATTERNS[0] = searchPattern

        await self.sendMessage(c.SEARCH_PATTERN_SET + searchPattern, msg.guild)

    async def sendTheThreadsLinksToTheServer(self):
        threads = gT.goodThreads(self.SEARCH_PATTERNS)
        if (threads):
            for thread in threads:
                await self.sendMessage(str(thread.link), msg.guild)
        else:
            print(c.NO_MATCHING_THREADS)
        u.delete(threads)

    async def on_message(self, msg):
        if (msg.author.bot == True):
            return

        if (self.BOT_TXT_CHANNEL_ID != "0"):
            await self.checkForValgor(msg)

        if (dU.hasThePermissions(msg)):
            await self.setChannel(msg)
            await self.setSearchPattern(msg)
            await self.sendMessage(c.DEUS_VULT, msg.guild)
        else:
            print(msg.author.display_name + c.NO_PERMISSION)
            await self.sendMessage(msg.author.display_name + c.NO_PERMISSION,
                                   msg.guild)

    async def checkForThreads(self):
        await self.wait_until_ready()
        while not self.is_closed():
            await self.sendTheThreadsLinksToTheServer()
            print(c.SLEEPING_TXT)
            await a.sleep(c.SLEEP_TIME_IN_SECONDS)

    async def setup_hook(self) -> None:
        self.bg_task = self.loop.create_task(self.checkForThreads())