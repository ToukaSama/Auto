from bot.get_cfg import get_config
class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "Encode")
    # AHCompressBot....
    # sucks Dude
    APP_ID = int(get_config("APP_ID", "22606849"))
    API_HASH = get_config("API_HASH", "ef85493cd32eadcb5309b5957d8d1b86")
    LOG_CHANNEL = get_config("LOG_CHANNEL", "Hindi_Kochikame")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without `@` LOL
     # Get these values from my.telegram.org
    AUTH_USERS = set(
        int(x) for x in get_config(
            "AUTH_USERS", "-1002310304236").split()
    )
# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(1002310304236) 🤣
    # array to store the channel ID who are authorized to use the bot
    # dont u fucking remove this id 😤
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "6773470262:AAFTwMuxwtHt3q-aa--opcOF3b9QC9NGhIg")
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = get_config("BOT_USERNAME", "Nya_Rename_bot")
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/8c5cc55313e0e984a8f95-b79cb378627738b0c6.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "▣")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "▢")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
