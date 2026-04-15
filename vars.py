

from os import environ

API_ID = int(environ.get("API_ID", "29020892"))
API_HASH = environ.get("API_HASH", "15bfac43cfbeb3993c942ce2f11ec3f8")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "shem_2_u")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/shem_2_u")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "7068000043").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "7068000043"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "-1003921211259")




