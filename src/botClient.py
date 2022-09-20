import discord as d
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
        print(f"{self.user}" + c.HELLO)

    async def sendMessage(self, txt):
        theGuild = self.getTest0Guild()  #change test guild
        theTxtChannel = 0
        textChannels = dU.getGuildTextChannels(theGuild)

        for textChannel in textChannels:
            if (str(textChannel.id) == str(self.BOT_TXT_CHANNEL_ID)):
                theTxtChannel = textChannel
                break
        if (theTxtChannel != 0):
            await theTxtChannel.send(txt)
        else:
            print(c.CANNOT_FIND_CHANNEL)

    async def checkForValgor(self, msg):
        txt = c.DEUS_VULT
        if (msg.content.lower().startswith(c.TEST)):
            await self.sendMessage(txt)
            txt = msg.author.name

            if (str(msg.author.id) == c.VALGOR_ID):
                txt += c.IS_VALGOR
            else:
                txt += c.IS_NOT_VALGOR

            await self.sendMessage(txt)

    async def setChannel(self, msg):
        if (not (msg.content.startswith(c.SET_CHANNEL))):
            return

        i = len(c.SET_CHANNEL)
        channelName = msg.content[i:].strip()
        theGuild = msg.guild
        textChannels = dU.getGuildTextChannels(theGuild)

        if (textChannels):
            for textChannel in textChannels:
                if (str(textChannel.name) == str(channelName)):
                    self.BOT_TXT_CHANNEL_ID = textChannel.id
                    break
            await self.sendMessage(c.CHANNEL_SET + channelName)

    async def setSearchPattern(self, msg):
        if (not (msg.content.startswith(c.SET_SEARCH_PATTERN))):
            return

        i = len(c.SET_SEARCH_PATTERN)
        searchPattern = msg.content[i:].strip()
        self.SEARCH_PATTERNS[0] = searchPattern
        await self.sendMessage(c.SEARCH_PATTERN_SET + searchPattern)

    async def sendTheThreadsLinksToTheServer(self):
        threads = gT.goodThreads(self.SEARCH_PATTERNS)
        if (threads):
            for thread in threads:
                await self.sendMessage(str(thread.link))
        else:
            print(c.NO_MATCHING_THREADS)
            #await self.sendMessage(str("test41"))

        u.delete(threads)

    async def on_message(self, msg):
        if (msg.author.bot == True):
            return
        
        if (self.BOT_TXT_CHANNEL_ID != 0):
            await self.checkForValgor(msg)

        if (dU.hasThePermissions(msg)):
            await self.setChannel(msg)
            await self.setSearchPattern(msg)
            await self.sendMessage(c.DEUS_VULT)
        else:
            print(msg.author.display_name + c.NO_PERMISSION)
            await self.sendMessage(msg.author.display_name + c.NO_PERMISSION)

    async def doTheTask(self):
        await self.wait_until_ready()

        while not self.is_closed():
            await self.sendTheThreadsLinksToTheServer()
            print(c.SLEEPING_TXT)
            await a.sleep(c.SLEEP_TIME_IN_SECONDS)

    def getGuild(self, guildID):
        for guild in self.guilds:
            if (str(guild.id) == str(guildID)):
                return guild

    def getTest0Guild(self):
        return self.getGuild(c.TEST0_GUILD_ID)

    def getTest1Guild(self):
        return self.getGuild(c.TEST1_GUILD_ID)

    async def setup_hook(self) -> None:
        self.bg_task = self.loop.create_task(self.doTheTask())