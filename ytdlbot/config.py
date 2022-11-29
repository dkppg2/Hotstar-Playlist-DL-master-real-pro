#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - config.py
# 8/28/21 15:01
#

__author__ = "Benny <benny.think@gmail.com>"

import os

from dotenv import load_dotenv
load_dotenv()

# general settings
WORKERS: "int" = int(os.getenv("WORKERS", 100))
PYRO_WORKERS: "int" = int(os.getenv("PYRO_WORKERS", 100))
APP_ID: "int" = int(os.getenv("APP_ID", 18274091))
APP_HASH = os.getenv("APP_HASH", "97afe4ab12cb99dab4bed25f768f5bbc")
TOKEN = os.getenv("TOKEN", "5767492492:AAH9lXCuf0N-e8RpUR-8KlhzbNeHMqLv_bk")

REDIS = os.getenv("REDIS")

# quota settings
QUOTA = int(os.getenv("QUOTA", 10 * 1024 * 1024 * 1024))  # 10G
if os.uname().sysname == "Darwin":
    QUOTA = 10 * 1024 * 1024  # 10M

TG_MAX_SIZE = 2 * 1024 * 1024 * 1024 * 0.99
# TG_MAX_SIZE = 10 * 1024 * 1024

EX = os.getenv("EX", 24 * 3600)
MULTIPLY = os.getenv("MULTIPLY", 5)  # VIP1 is 5*5-25G, VIP2 is 50G
USD2CNY = os.getenv("USD2CNY", 6)  # $5 --> ¥30

ENABLE_VIP = os.getenv("VIP", False)
MAX_DURATION = int(os.getenv("MAX_DURATION", 60))
AFD_LINK = os.getenv("AFD_LINK", "https://afdian.net/@BennyThink")
COFFEE_LINK = os.getenv("COFFEE_LINK", "https://www.buymeacoffee.com/bennythink")
COFFEE_TOKEN = os.getenv("COFFEE_TOKEN")
AFD_TOKEN = os.getenv("AFD_TOKEN")
AFD_USER_ID = os.getenv("AFD_USER_ID")
OWNER = os.getenv("OWNER", "2109516065")

# limitation settings
AUTHORIZED_USER: "str" = os.getenv("AUTHORIZED_USER", "2109516065,1823957960,2083503061,1166625664")
# membership requires: the format could be username/chat_id of channel or group
REQUIRED_MEMBERSHIP: "str" = os.getenv("REQUIRED_MEMBERSHIP", "")

# celery related
ENABLE_CELERY = os.getenv("ENABLE_CELERY", False)
ENABLE_QUEUE = os.getenv("ENABLE_QUEUE", False)
BROKER = os.getenv("BROKER", f"redis://{REDIS}:6379/4")

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASS = os.getenv("MYSQL_PASS", "root")

AUDIO_FORMAT = os.getenv("AUDIO_FORMAT")
ARCHIVE_ID = int(os.getenv("ARCHIVE_ID", "0"))

IPv6 = os.getenv("IPv6", False)
ENABLE_FFMPEG = os.getenv("ENABLE_FFMPEG", False)

THUMBNAIL_LOCATION = "thumbnail"
template = "{filename}.{quality}P.HS.WEB-DL.AAC2.0.H.265-{ _Rᴏʟᴇx_ } WEBDL_PRO_BOT.mkv"
