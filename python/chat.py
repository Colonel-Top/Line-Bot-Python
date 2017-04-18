#!/usr/bin/python
#-*-coding: utf-8 -*-
import time
import random
import string
#from requests import requests
from . import gspread
import os
import sys
from . import oauth2client

from datetime import datetime


now = datetime.now()

from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
state = '0'
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
worksheet = sh.worksheet("Account")
print ("Google API Connected")
def Login():
    print ("Messenger API Connected")
    scope = ['https://spreadsheets.google.com/feeds']
    state = '0'
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
    worksheet = sh.worksheet("Account")
    print ("Google API Connected")

bot_status = 0
bot_mode = 0
# define hi or hello
greeting_w = ['Hello', 'Hi ', 'Greeting', 'สวัสดี','hello', 'hi ', 'greetings', 'sup', 'whats up','re you here','หวัดดี']
greeting_f = ['May i help you please ?', 'Yes ?', 'Ya Anything you want ?', 'Anything ? ya ?', 'Greeting yes ?','Always here']
backasgre_w = ['Thx','Thank','ขอบคุณ','appreciate','ขอบใจ']
backasgre_f = ['Your welcome','With Pleasure :)','with Appreciated','Ya','Okay ^^','Welcome','Never mind :)']
menu_cmd = ['pen menu','pen Menu','เปิดเมนู','เรียกเมนู','show function','Show function','Show Menu','show menu','Show menu']
simq_ask = ['ho are you','hat do you do','ho is your boss','ho am i','ell me a joke','ell me some joke']
simq_ans = ['I am Chloe The Secretary of Colonel','I am Chloe The Secretary of Colonel ^^ Helping My Master & you guys','My Boss or my master is Colonel','Some Human in this world','Joke ? google it :)','Ahh Nope']

bank_ask = ['eport account','ccount report','om engr account','pdate account','heck amout account','heck amout in account']
bank_ans = ['Okay i will update account for you','Yes, wait a second','Let me check account','Here we go','Alright here is it','Ya this one ^^']

#execfile("timeahead.py")
tellasc_cmd = ['tell all associate']
tellasc_ans = ['Okay i will update send msg for you','Yes, wait a second','Let me work on it','Here we go','Alright here is it','Ya this one ^^']
# Class def

import json
import sys
'''
BOT_NAME = "Bot"

chatbot = ChatBot(
                    BOT_NAME,
                    storage_adapter='chatterbot.adapters.storage.MongoDatabaseAdapter',
                    database="chatterbot-database",
                    logic_adapters=[
                      "chatterbot.adapters.logic.MathematicalEvaluation",
                      "chatterbot.adapters.logic.TimeLogicAdapter",
                      "chatterbot.adapters.logic.ClosestMatchAdapter"
                    ],
                    filters=[
                      'chatterbot.filters.RepetitiveResponseFilter'
                    ],
                  )

if len(sys.argv) < 2:
  sys.exit(0)

message = sys.argv[1]
result = chatbot.get_response(message)'''
result = "Done"
print ("%s" % result)