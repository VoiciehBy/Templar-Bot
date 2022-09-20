import discord as d
import logging.handlers as h
import constants as c

async def setupLogging():
    theHandler = h.RotatingFileHandler(
        filename=c.BOT_LOG_FILENAME,
        encoding="utf-8",
        maxBytes=16 * 1024 * 1024, #16 MiB
        backupCount=2 # Rotate throught 2 files
    )
    d.utils.setup_logging(handler=theHandler,root=False)