import discord
import constants as c

def getGuildTextChannels(theGuild):
    textChannels = list()

    for theChannel in theGuild.channels:
        if (str(theChannel.type) == "text"):
            textChannels.append(theChannel)
    return textChannels

def hasThePermissions(msg):
    for role in msg.author.roles:
        if(role.name.upper() == c.ROLE):
            return True
    return False

def hasNotThePermissions(msg):
    return not(hasThePermissionsids(msg))