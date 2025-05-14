# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "28473509")
API_HASH = os.getenv("API_HASH", "f56218a21931d5f4ddcf0f0354256816")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://superk7070:DRlvIYSLRSDXzXAL@cluster0.xitnxo7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5698467921").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "lucky")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002658109909")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002593438169")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "cb40d09f525d3c36fe079a471892af98") # for session encryption
IV_KEY = os.getenv("IV_KEY", "ac5b30c7b98a") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
