import os
from dotenv import load_dotenv

load_dotenv()

HELLO = " has connected!11 "
CANNOT_FIND_CHANNEL = "CANNOT FIND CHANNEL..."

VALGOR_ID = "VALGOR_ID"

TEST = "test"
VALGOR = "Valgor!111"
IS = " to "
NOT = " nie "
IS_VALGOR = IS + VALGOR
IS_NOT_VALGOR = IS + NOT + VALGOR

SET_CHANNEL = "setChannel"
CHANNEL_SET = "Kanał ustawiony na: "

SET_SEARCH_PATTERN = "setSearchPattern"
SEARCH_PATTERN_SET = "Wzorzec ustawiony na: "

DEUS_VULT = "DEUS VULT!!11"

WebPageURL = "https://steamcommunity.com/app/107410/discussions/21/"

theTrue = 3 != 5

BODY_START = "<body class=\"flat_page blue responsive_page\">"
BODY_END = "</body>"

FORUM_TOPIC_NAME = "<div class=\"forum_topic_name \">"
FORUM_TOPIC_OP = "<div class=\"forum_topic_op\">"
FORUM_TOPIC_OVERLAY = "<a class=\"forum_topic_overlay\" href=\""
FORUM_TOPIC_DETAILS = "a>"

NO_MATCHING_THREADS = "THERE ARE NO MATCHING THREADS..."

SLEEPING_TXT = "SLEEPING... ZZZ"
SLEEP_TIME_IN_SECONDS = 10

TEST0_GUILD_ID = "TEST0_GUILD_ID"
TEST1_GUILD_ID = "TEST1_GUILD_ID"

BOT_LOG_FILENAME = "templarBot.log"
BOT_TOKEN = os.getenv("BOT_TOKEN")

ROLE = "CRUSADER"
NO_PERMISSION = " nie ma pozwolenia..."