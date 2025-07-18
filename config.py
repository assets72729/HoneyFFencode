import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "24890303")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "94cf78d1e6883ecb10f32e31fc23cfe0") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002705791364') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL","")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","Cluster0") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "7289855833")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002704166324')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()


    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
