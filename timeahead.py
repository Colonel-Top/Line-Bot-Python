# -*- coding: utf-8 -*-
import time
import random
import string
import gspread
import os
import sys

from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

gdate = ""
now = datetime.now()

    #line_bot_api.push_message(destination, TextSendMessage(text= "***********************")
    #line_bot_api.push_message(destination, TextSendMessage(text= "Messenger API Connected")
    #print ("Messenger API Connected")
scope = ['https://spreadsheets.google.com/feeds']
state = '0'
credentials = ''
gc = ''
sh = ''
worksheet = ''

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('QWiSqwAAs1/FyPo+Rt+jKoxjjK+LbkQ1pC1zsmCO9s5g2YO9EFUsSKO90ABQpc8h31iecVkjMsG3IZ2J9xCcS5pHL0ph8nc81PIM+gJEFzkJpHIRBWiJQl7sh6dOuuApuPMC+aj1HjkT5iaHCXDJ5AdB04t89/1O/w1cDnyilFU=')

def Login():
    #line_bot_api.push_message(destination, TextSendMessage(text= "***********************")
    #line_bot_api.push_message(destination, TextSendMessage(text= "Messenger API Connected")
    #print ("Messenger API Connected")
    scope = ['https://spreadsheets.google.com/feeds']
    state = '0'
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
    worksheet = sh.worksheet("Account")
#line_bot_api.push_message(destination, TextSendMessage(text= "Google API Connected")
#print ("Google API Connected")
#line_bot_api.push_message(destination, TextSendMessage(text= 'Debug:: Time runner begun')
# Login with your Google account
destination = 'Ufb00beda08083bcf402fbd2160b75574'
bot_status = 0
bot_mode = 0
# define hi or hello
greeting_w = ['Hello', 'Hi ', 'Greeting', 'สวัสดี','hello', 'hi ', 'greetings', 'sup', 'whats up','re you here']
greeting_f = ['May i help you please ?', 'Yes ?', 'Ya Anything you want ?', 'Anything ? ya ?', 'Greeting yes ?','Always here']
backasgre_w = ['Thx','Thank','ขอบคุณ','appreciate','ขอบใจ']
backasgre_f = ['Your welcome','With Pleasure :)','with Appreciated','Ya','Okay ^^','Welcome','Never mind :)']
menu_cmd = ['pen menu','pen Menu','เปิดเมนู','เรียกเมนู','show function','Show function','Show Menu','show menu','Show menu']
simq_ask = ['ho are you','hat do you do','ho is your boss','ho am i','ell me a joke','ell me some joke']
simq_ans = ['I am Chloe The Secretary of Colonel','I am Chloe The Secretary of Colonel ^^ Helping My Master & you guys','My Boss or my master is Colonel','Some Human in this world','Joke ? google it :)','Ahh Nope']
timesay = ['Greeting','Good morning','Enjoy New Day Sir' ,'Begin the day','Fight the day']
bank_ask = ['eport account','ccount report','om engr account','pdate account','heck amout account','heck amout in account']
bank_ans = ['Okay i will update account for you','Yes, wait a second','Let me check account','Here we go','Alright here is it','Ya this one ^^']


tellasc_cmd = ['tell all associate']
tellasc_ans = ['Okay i will update send msg for you','Yes, wait a second','Let me work on it','Here we go','Alright here is it','Ya this one ^^']

while (True):
    #line_bot_api.push_message('Ufb00beda08083bcf402fbd2160b75574, TextSendMessage(text='Hello World!'))  "Debug: Looping #")
    # print('loop begin')
    now = datetime.now()
    # statuschk = ''
    if(now.hour == 1 and now.minute == 0 and now.second == 1):
        Login()
    if (now.day == 16 and now.hour == 0 and now.minute == 0 and now.second == 1 ):  # Get Interest
        # if(1):
        #line_bot_api.push_message(destination, TextSendMessage(text= "Chloe has Awaken and Collecting Interest"))
        print("AI has Awaken and Collecting Interest")
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
        gc = gspread.authorize(credentials)
        sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
        worksheet = sh.worksheet("Account")
        cell = worksheet.acell('U31').value
        cell = cell.encode("utf-8")
        monthcell = now.month
        monthcell += 9
        # monthcell += 10
        for row in range(2, 31):  # Must be 31 in col or last parameter
            peruser = 0
            for col in range(8, 20):
                tmp = worksheet.cell(row, col).value
                print(tmp)
                if (tmp == '0'):
                    peruser += 1
            # print("Done Per loop")
            # print (peruser)
            if peruser >= 2 and worksheet.cell(row, monthcell).value == '':
                interest = int(worksheet.cell(row, 22).value)
                interest += 1
                # print (interest)
                worksheet.update_cell(row, 22, interest)
            if worksheet.cell(row, monthcell).value == '':
                worksheet.update_cell(row, monthcell, 0)
            if row == 8:
                print("Skip Safe")
                continue
    #if(now.min == 0 and now.second==0 ):
    if(now.second == 0) or now.second == 30 :
        try:
            print("Checking Schedule\n")
                #client.send(colonelid,'Second = 0 in function loop')
            gdate = ""
                # Open a file
            f = open("serverdate", "r+")
            text = f.readlines()
                #line_bot_api.push_message(destination, TextSendMessage(text=  "Debug: Printing read line at hour")
            for line in text:
                now = datetime.now()
                try:
                    curday = int(line[0:2])
                except ValueError:
                    continue;
                    #print curday
                curmonth = int(line[3:5])
                    #print curmonth
                curyear =  int(line[6:10])
                #print curyear
                curhour = int(line[11:13])
                #print curhour
                curmin =  int(line[14:16])
                #print curmin
                #line_bot_api.push_message(destination, TextSendMessage(curday))
                    #line_bot_api.push_message(destination, TextSendMessage(text=now.date)
                   #print (str(curday)+" " + str(curmin) + " " + str(now.min))
                    #print("*")
                if curhour >= 1:
                    tmphour = curhour-1
                    line_bot_api.push_message(destination, TextSendMessage(tmphour))
                    line_bot_api.push_message(destination, TextSendMessage(curhour))
                    line_bot_api.push_message(destination, TextSendMessage(text = "Done"))
                if(curday == now.day and curmonth == now.month and curyear == now.year and tmphour == now.hour):
                #if(1):
                    try:
                        #now = datetime.now()
                        gdate =  (now.strftime("%d-%m-%Y"))
                        line_bot_api.push_message(destination, TextSendMessage("กำหนดการแจ้งเตือน \nวันที่ :" +gdate))
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            print (lines)
                            if str(tmphour+2) in lines:
                                #if str(curmin) in lines:
                                line_bot_api.push_message(destination, TextSendMessage(lines))
                        # Close opend file
                        fo.close()
                        break
                    except Exception as es:
                        print (es)
                # Close opend file
            f.close()
        except Exception as e:
            print (e)
    if now.hour == 6 and now.minute == 0 and now.second==0:
    #if((now.second==0 or now.second == 30)):
        #print('in condition')
        try:
            #client.send(colonelid,'Second = 0 in function loop')
            #print ('get in try')
            gdate = ""
            line_bot_api.push_message(destination, TextSendMessage(text=random.choice(timesay)))
            # Open a file
            f = open("serverdate", "r+")
            text = f.readlines()
            #print ('readlinedone')
            #line_bot_api.push_message(destination, TextSendMessage(text=  "Debug: Printing read line")
            for line in text:
                curday = int(line[0:2])
                #print curday
                curmonth = int(line[3:5])
               # print curmonth
                curyear =  int(line[6:10])
                #print curyear
                curhour = int(line[11:13])
                #print curhour
                curmin =  int(line[14:16])
                #print curmin
                #line_bot_api.push_message(destination, TextSendMessage(text= curday)
                #line_bot_api.push_message(destination, TextSendMessage(text=now.date)
                #print (curday+curmonth+curyear+curhour+curmin)
                #print (now.date)
                if(curday == now.day and curmonth == now.month and curyear == now.year):
                #if(1):
                    
                    #print ('correct rolling in')
                    try:
                        gdate = (now.strftime("%d-%m-%Y"))
                        line_bot_api.push_message(destination, TextSendMessage(text= "Date:"+gdate))
                        # Open a file
                        fo = open(gdate, "r+")
                        strws = fo.read()
                        line_bot_api.push_message(destination, TextSendMessage(text=strws))
                        # Close opend file
                        fo.close()
                        break
                    except Exception as e:
                        client.send(colonelid,e)
                # Close opend file
                f.close()
                
        except Exception as e:
            print (e)
    time.sleep(1)
    #print (now.second)
