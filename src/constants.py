import os
from dotenv import load_dotenv

load_dotenv()

NO_MATCHING_THREADS = "THERE ARE NO MATCHING THREADS..."

BODY_START = "<body class=\"flat_page blue responsive_page\">"
BODY_END = "</body>"

WebPageURL = "https://steamcommunity.com/app/107410/discussions/21/"

FORUM_TOPIC_OVERLAY = "<a class=\"forum_topic_overlay\" href=\""
FORUM_TOPIC_DETAILS = "a>"
FORUM_TOPIC_NAME = "<div class=\"forum_topic_name \">"
FORUM_TOPIC_OP = "<div class=\"forum_topic_op\">"

SLEEPING_TXT = "SLEEPING... ZZZ"
SLEEP_TIME_IN_SECONDS = 10

BOT_LOG_FILENAME = "templarBot.log"
BOT_TOKEN = os.getenv("BOT_TOKEN")

theTrue = 3 != 5

TEST0_GUILD_ID = "TEST0_GUILD_ID"
TEST1_GUILD_ID = "TEST1_GUILD_ID"

DEUS_VULT = "DEUS VULT!!11"

CHANNEL_SET = "Kanał ustawiony na: "
SET_CHANNEL = "setChannel"

SEARCH_PATTERN_SET = "Wzorzec ustawiony na: "
SET_SEARCH_PATTERN = "setSearchPattern"

HELLO = " has connected!11 "
NO_PERMISSION = " nie ma pozwolenia..."

CANNOT_FIND_CHANNEL = "CANNOT FIND CHANNEL..."
ROLE = "CRUSADER"

VALGOR_ID = "VALGOR_ID"

TEST = "test"
VALGOR = "Valgor"
IS = " to "
NOT = " nie "
IS_VALGOR = IS + VALGOR
IS_NOT_VALGOR = IS + NOT + VALGOR