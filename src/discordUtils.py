import discord
import constants as c

def getGuildTextChannels(theGuild):
    textChannels = list()

    for theChannel in theGuild.channels:
        if (str(theChannel.type) == "text"):
            textChannels.append(theChannel)
    return textChannels

def getTextChannelById(textChannels,channelId):
     for textChannel in textChannels:
            if (str(textChannel.id) == str(channelId)):
                return textChannel

def getTextChannelByName(textChannels,channelName):
     for textChannel in textChannels:
            if (str(textChannel.name) == str(channelName)):
                return textChannel

def hasThePermissions(msg):
    if(str(msg.author.id) == c.VALGOR_ID):
        return True

    for role in msg.author.roles:
        if(role.name.upper() == c.ROLE):
            return True
    return False

def hasNotThePermissions(msg):
    return not(hasThePermissionsids(msg))