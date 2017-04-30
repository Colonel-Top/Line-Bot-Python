# -*- coding: utf-8 -*-
import time
import random
import string
import gspread
import os
import sys
import os.path
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
print ("Running")
gdate = ""
now = datetime.now()

    #line_bot_api.push_message(group, TextSendMessage(text= "***********************")
    #line_bot_api.push_message(group, TextSendMessage(text= "Messenger API Connected")
    #print ("Messenger API Connected")
scope = ['https://spreadsheets.google.com/feeds']
state = '0'
credentials = ''
gc = ''
sh = ''
worksheet = ''
index = 6
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('QWiSqwAAs1/FyPo+Rt+jKoxjjK+LbkQ1pC1zsmCO9s5g2YO9EFUsSKO90ABQpc8h31iecVkjMsG3IZ2J9xCcS5pHL0ph8nc81PIM+gJEFzkJpHIRBWiJQl7sh6dOuuApuPMC+aj1HjkT5iaHCXDJ5AdB04t89/1O/w1cDnyilFU=')

def Login():
    #line_bot_api.push_message(group, TextSendMessage(text= "***********************")
    #line_bot_api.push_message(group, TextSendMessage(text= "Messenger API Connected")
    #print ("Messenger API Connected")
    scope = ['https://spreadsheets.google.com/feeds']
    state = '0'
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
    worksheet = sh.worksheet("Account")
#line_bot_api.push_message(group, TextSendMessage(text= "Google API Connected")
#print ("Google API Connected")
#line_bot_api.push_message(group, TextSendMessage(text= 'Debug:: Time runner begun')
# Login with your Google account
fo = open('control','r+')
strws = fo.read()
d =''
if (strws == '1'):
    groups = 'c108bc8c05480d73d978fe4d587bb6288'
elif (strws == '2'):
    groups = 'c511d9b1c8cf3df51dcebc2b905cc6b30'
elif (strws == '3'):
    groups = 'c5a40d9ff4355ab8b9a9a0ceb94fd9fee'
elif (strws == '4'):
    groups = 'ca40a6ceec0f539fcc12e9e5f1ccb2fa3'
elif (strws == '5'):
    groups = 'cd4403585a5c0416cfd0d7e5e1fc6d17b'
elif (strws == '6'):
    groups = 'cfce90616f21ecc8892db0e7e8f90aaf4'

destinationme = 'Ufb00beda08083bcf402fbd2160b75574'
group = 'C5c90aa2273d7093f30ca08a91066cd78'
associateid = 'Cacab1833e4e7009f49c15779e645f66c'
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
timesay = ['สวัสดียามเช้าค่ะ','อรุณสวัสดิ์ค่ะทุกคน','สวัสดีวันใหม่ค่ะ','ขอให้สนุกกับวันใหม่นะค่ะ','สวัสดียามเช้าค่ะทุกคน','อรุณสวัสดิ์ค่ะ','สวัสดีตอนเช้าค่ะ']
bank_ask = ['eport account','ccount report','om engr account','pdate account','heck amout account','heck amout in account']
bank_ans = ['Okay i will update account for you','Yes, wait a second','Let me check account','Here we go','Alright here is it','Ya this one ^^']


tellasc_cmd = ['tell all associate']
tellasc_ans = ['Okay i will update send msg for you','Yes, wait a second','Let me work on it','Here we go','Alright here is it','Ya this one ^^']

while (True):
    #line_bot_api.push_message('Ufb00beda08083bcf402fbd2160b75574, TextSendMessage(text='Hello World!'))  "Debug: Looping #")
    # print('loop begin')
    now = datetime.now()
    gdates = (now.strftime("%d-%m-%Y"))
    if not os.path.isfile(gdates) :
        time.sleep(1)
        continue
    if(now.hour == 7 and now.minute == 59 and now.second == 0):
        print("-------------")
        print ("Begin new Day")
        print("* "+gdates+" Running Morning 8:00 AM Properly")
    elif(now.hour == 17 and now.minute == 59 and now.second == 0):
        print("* "+gdates+" Running Evening 18:00 PM Properly")
    elif(now.hour == 23 and now.minute == 59 and now.second == 0):
        print("* "+gdates+" Running MIDNIGHT 23:59 PM Properly")
        print("-End Day-")
        print("-------------")
    # statuschk = ''
    if (now.day == 16 and now.hour == 0 and now.minute == 0 and now.second == 1 ):  # Get Interest
        # if(1):
        #line_bot_api.push_message(group, TextSendMessage(text= "Chloe has Awaken and Collecting Interest"))
        #print("AI has Awaken and Collecting Interest")
        line_bot_api.push_message(associateid, TextSendMessage(text="เริ่มทำการตัดดอกเบี้ยค่ะ"))
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
        line_bot_api.push_message(associateid, TextSendMessage(text="การตัดดอกเบี้ยเสร็จเรียบร้อยค่ะ"))
    if (now.day == 16):
        if(now.hour == 20 and now.minute == 00 and now.second == 0):
            namepush = ''
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
            gc = gspread.authorize(credentials)
            sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
            worksheet = sh.worksheet("Account")
            for num in range(2, 31):  # Must be 31 in col or last parameter
                tmp = str(worksheet.cell(num, 22).value)
                if (tmp >= 1 ):
                    name = worksheet.cell(num,7).value
                    if num == 8:
                        continue
                    name = name.encode("utf-8")
                    namepush += name+' - '+tmp+' ครั้ง \n'
            result = 'รายงานจำนวนครั้งการค้างชำระถึงเดือนนี้\n'+namepush
            line_bot_api.push_message(group, TextSendMessage(result))
            print("Push Report Stuck Big group")
        if(now.hour == 0 and now.minute == 15 and now.second == 0):
            namepush = ''
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
            gc = gspread.authorize(credentials)
            sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
            worksheet = sh.worksheet("Account")
            for num in range(2, 31):  # Must be 31 in col or last parameter
                tmp = str(worksheet.cell(num, 22).value)
                if (tmp >= 1 ):
                    name = worksheet.cell(num,7).value
                    if num == 8:
                        continue
                    name = name.encode("utf-8")
                    namepush += name+' - '+tmp+' ครั้ง \n'
            result = 'รายงานจำนวนครั้งการค้างชำระถึงเดือนนี้\n'+namepush
            line_bot_api.push_message(associateid, TextSendMessage(result))
            print("Push Report Stuck Assoc")
    if(now.minute == 0 and now.second==0 ):
    #if(now.second == 0) or now.second == 30 :
        try:
            result= ''
            #print("Checking Schedule\n")
                #client.send(colonelid,'Second = 0 in function loop')
            gdate = ""
                # Open a file
            f = open("serverdate", "r+")
            text = f.readlines()
                #line_bot_api.push_message(group, TextSendMessage(text=  "Debug: Printing read line at hour")
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
                #line_bot_api.push_message(group, TextSendMessage(curday))
                    #line_bot_api.push_message(group, TextSendMessage(text=now.date)
                   #print (str(curday)+" " + str(curmin) + " " + str(now.min))
                    #print("*")
                if curhour >= 1:
                    tmphour = curhour-1
                    #line_bot_api.push_message(group, TextSendMessage(tmphour)) #22
                    #line_bot_api.push_message(group, TextSendMessage(curhour)) #23
                    #line_bot_api.push_message(group, TextSendMessage(text = "Done"))
                if (curday == now.day and curmonth == now.month and curyear == now.year and tmphour == now.hour):
                #if(1):
                    try:
                        #now = datetime.now()
                        gdate =  (now.strftime("%d-%m-%Y"))
                        printhour = curhour-now.hour
                        result = "กำหนดการแจ้งเตือน \nวันที่ : " +gdate+"\n" +"เวลาถึงในอีก "+str(printhour)+"ชม.\n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if str(curhour) in lines:
                                if '*' not in lines and '$' not in lines:
                                #if str(curmin) in lines:
                                    result += lines
                        # Close opend file
                        fo.close()
			if '*' not in result and '$' not in result:
	                        line_bot_api.push_message(group, TextSendMessage(result))
                        break
                    except Exception as es:
                        print (es)
                
                # Close opend file
            f.close()
            
            print ("Push Notification"+ str(now.hour) + ":"+str(now.minute) )
        except Exception as e:
            print (e)
    if now.hour == 6 and now.minute == 0 and now.second==0:
    #if now.hour == 0 and now.minute == 55 and now.second==0:
    #if((now.second==0 or now.second == 30)):
        #print('in condition')
        try:
            result = ''
            #client.send(colonelid,'Second = 0 in function loop')
            #print ('get in try')
            gdate = ""
            
            # Open a file
            f = open("serverdate", "r+")
            text = f.readlines()
            #print ('readlinedone')
            #line_bot_api.push_message(group, TextSendMessage(text=  "Debug: Printing read line")
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
                #line_bot_api.push_message(group, TextSendMessage(text= curday)
                #line_bot_api.push_message(group, TextSendMessage(text=now.date)
                #print (curday+curmonth+curyear+curhour+curmin)
                #print (now.date)
                if(curday == now.day and curmonth == now.month and curyear == now.year):
                #if(1):
                    
                    #print ('correct rolling in')
                    try:
                        result += random.choice(timesay)
                        gdate = (now.strftime("%d-%m-%Y"))
                        result += "\nกำหนดการแจ้งเตือน \nวันนี้ : \n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if '*' not in lines and '$' not in lines:
                                #if str(curmin) in lines:
                                result += lines
                        # Close opend file
                        fo.close()
			if '*' not in result and '$' not in result:
	                        line_bot_api.push_message(group, TextSendMessage(result))
                        break
                    except Exception as e:
                        print (e)
                # Close opend file
                f.close()
                #line_bot_api.push_message(group, TextSendMessage(result))
        except Exception as e:
            print (e)
        
    if now.hour == 18 and now.minute == 0 and now.second==0:
    #if((now.second==0 or now.second == 30)):
        #print('in condition')
        try:
            result = ''
            #client.send(colonelid,'Second = 0 in function loop')
            #print ('get in try')
            gdate = ""
            
            # Open a file
            f = open("serverdate", "r+")
            text = f.readlines()
            #print ('readlinedone')
            #line_bot_api.push_message(group, TextSendMessage(text=  "Debug: Printing read line")
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
                #line_bot_api.push_message(group, TextSendMessage(text= curday)
                #line_bot_api.push_message(group, TextSendMessage(text=now.date)
                #print (curday+curmonth+curyear+curhour+curmin)
                #print (now.date)
                if(curday-1 == now.day and curmonth == now.month and curyear == now.year):
                #if(1):
                    
                    #print ('correct rolling in')
                    try:
                        result += random.choice(timesay)
                        gdate = str(curday-1)+'-'+str(curmonth)+'-'+str(curyear)
                        #gdate = (now.strftime("%d-%m-%Y"))
                        result += "\nกำหนดการแจ้งเตือน \nถึงในวันพรุ่งนี้ : \n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if True:
                                if '*' not in lines and '$' not in lines:
                                #if str(curmin) in lines:
                                    result += lines
                        # Close opend file
                        fo.close()
			if '*' not in result and '$' not in result:
                        	line_bot_api.push_message(group, TextSendMessage(result))
                        break
                    except Exception as e:
                        print (e)
                # Close opend file
                f.close()
                #line_bot_api.push_message(group, TextSendMessage(result))
        except Exception as e:
            print (e)
    if now.hour == 23 and now.minute == 59 and now.second == 0:
        try:
            gdate = (now.strftime("%d-%m-%Y"))
            f = open('serverdate','r')
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != gdate:
                    f.write(i)
            f.truncate()
            f.close()
            try:
                if(os.path.isfile(gdate)):
                    os.remove(gdate)
            except Exception as o:
                print (o)
        except Exception as e:
            print (e)
    #############################
    ########
    ###
    
    ####
    #####
    if(now.minute == 0 and now.second==0 ):
    #if(now.second == 0) or now.second == 30 :
        try:
            result= ''
            #print("Checking Schedule\n")
                #client.send(colonelid,'Second = 0 in function loop')
            gdate = ""
                # Open a file
            f = open("customerdate", "r+")
            text = f.readlines()
                #line_bot_api.push_message(group, TextSendMessage(text=  "Debug: Printing read line at hour")
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
                #line_bot_api.push_message(group, TextSendMessage(curday))
                    #line_bot_api.push_message(group, TextSendMessage(text=now.date)
                   #print (str(curday)+" " + str(curmin) + " " + str(now.min))
                    #print("*")
                if curhour >= 1:
                    tmphour = curhour-1
                    #line_bot_api.push_message(group, TextSendMessage(tmphour)) #22
                    #line_bot_api.push_message(group, TextSendMessage(curhour)) #23
                    #line_bot_api.push_message(group, TextSendMessage(text = "Done"))
                if (curday == now.day and curmonth == now.month and curyear == now.year and tmphour == now.hour):
                #if(1):
                    try:
                        #now = datetime.now()
                        gdate =  (now.strftime("%d-%m-%Y"))
                        printhour = curhour-now.hour
                        result = "กำหนดการแจ้งเตือน \nวันที่ : " +gdate+"\n" +"เวลาถึงในอีก "+str(printhour)+"ชม.\n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if str(curhour) in lines:
                                if '*' in lines:
                                #if str(curmin) in lines:
                                    result += lines
                        # Close opend file
                        fo.close()
                        line_bot_api.push_message(destinationme, TextSendMessage(result))
                        break
                    except Exception as es:
                        print (es)
                
                # Close opend file
            f.close()
            
            print ("Push Notification"+ str(now.hour) + ":"+str(now.minute) )
        except Exception as e:
            print (e)
    if now.hour == 6 and now.minute == 0 and now.second==0:
    #if((now.second==0 or now.second == 30)):
    #if (1):
        #print('in condition')
        try:
            result = ''
            #client.send(colonelid,'Second = 0 in function loop')
            #print ('get in try')
            gdate = ""
            
            # Open a file
            f = open("customerdate", "r+")
            text = f.readlines()
            #print ('readlinedone')
            #line_bot_api.push_message(group, TextSendMessage(text=  "Debug: Printing read line")
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
                #line_bot_api.push_message(group, TextSendMessage(text= curday)
                #line_bot_api.push_message(group, TextSendMessage(text=now.date)
                #print (curday+curmonth+curyear+curhour+curmin)
                #print (now.date)
                if(curday == now.day and curmonth == now.month and curyear == now.year):
                    try:
                        result += random.choice(timesay)
                        gdate = (now.strftime("%d-%m-%Y"))
                        result += "\nกำหนดการแจ้งเตือน \nวันนี้ : \n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if '*' in lines:
                                #if str(curmin) in lines:
                                result += lines
                        # Close opend file
                        fo.close()
                        line_bot_api.push_message(destinationme, TextSendMessage(result))
                        break
                    except Exception as e:
                        print (e)
                # Close opend file
                f.close()
            #print (result)
            #line_bot_api.push_message(destinationme, TextSendMessage(result))
        except Exception as e:
            print (e)
        
    if now.hour == 18 and now.minute == 0 and now.second==0:
    #if((now.second==0 or now.second == 30)):
        #print('in condition')
        try:
            result = ''
            #client.send(colonelid,'Second = 0 in function loop')
            #print ('get in try')
            gdate = ""
            
            # Open a file
            f = open("customerdate", "r+")
            text = f.readlines()
            #print ('readlinedone')
            #line_bot_api.push_message(group, TextSendMessage(text=  "Debug: Printing read line")
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
                #line_bot_api.push_message(group, TextSendMessage(text= curday)
                #line_bot_api.push_message(group, TextSendMessage(text=now.date)
                #print (curday+curmonth+curyear+curhour+curmin)
                #print (now.date)
                if(curday-1 == now.day and curmonth == now.month and curyear == now.year):
                #if(1):
                    
                    #print ('correct rolling in')
                    try:
                        result += random.choice(timesay)
                        gdate = str(curday-1)+'-'+str(curmonth)+'-'+str(curyear)
                        #gdate = (now.strftime("%d-%m-%Y"))
                        result += "\nกำหนดการแจ้งเตือน \nถึงในวันพรุ่งนี้ : \n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if True:
                                if '*' in lines:
                                #if str(curmin) in lines:
                                    result += lines
                        # Close opend file
                        fo.close()
                        line_bot_api.push_message(destinationme, TextSendMessage(result))
                        break
                    except Exception as e:
                        print (e)
                # Close opend file
                f.close()
                #line_bot_api.push_message(destinationme, TextSendMessage(result))
        except Exception as e:
            print (e)
    if(now.minute == 0 and now.second==0 ):
    #if(now.second == 0) or now.second == 30 :
        try:
            result= ''
            #print("Checking Schedule\n")
                #client.send(colonelid,'Second = 0 in function loop')
            gdate = ""
                # Open a file
            f = open("scheduledate", "r+")
            text = f.readlines()
                #line_bot_api.push_message(destinationme, TextSendMessage(text=  "Debug: Printing read line at hour")
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
                #line_bot_api.push_message(destinationme, TextSendMessage(curday))
                    #line_bot_api.push_message(destinationme, TextSendMessage(text=now.date)
                   #print (str(curday)+" " + str(curmin) + " " + str(now.min))
                    #print("%")
                if curhour >= 1:
                    tmphour = curhour-1
                    #line_bot_api.push_message(destinationme, TextSendMessage(tmphour)) #22
                    #line_bot_api.push_message(destinationme, TextSendMessage(curhour)) #23
                    #line_bot_api.push_message(destinationme, TextSendMessage(text = "Done"))
                if (curday == now.day and curmonth == now.month and curyear == now.year and tmphour == now.hour):
                #if(1):
                    try:
                        #now = datetime.now()
                        gdate =  (now.strftime("%d-%m-%Y"))
                        printhour = curhour-now.hour
                        result = "กำหนดการตารางงาน \nวันที่ : " +gdate+"\n" +"เวลาถึงในอีก "+str(printhour)+"ชม.\n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if str(curhour) in lines:
                                if '$' in lines:
                                #if str(curmin) in lines:
                                    result += lines
                        # Close opend file
                        fo.close()
                        line_bot_api.push_message(destinationme, TextSendMessage(result))
                        break
                    except Exception as es:
                        print (es)
                
                # Close opend file
            f.close()
            
            print ("Push Notification"+ str(now.hour) + ":"+str(now.minute) )
        except Exception as e:
            print (e)
    if now.hour == 6 and now.minute == 0 and now.second==0:
    #if((now.second==0 or now.second == 30)):
        #print('in condition')
        try:
            result = ''
            #client.send(colonelid,'Second = 0 in function loop')
            #print ('get in try')
            gdate = ""
            
            # Open a file
            f = open("scheduledate", "r+")
            text = f.readlines()
            #print ('readlinedone')
            #line_bot_api.push_message(destinationme, TextSendMessage(text=  "Debug: Printing read line")
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
                #line_bot_api.push_message(destinationme, TextSendMessage(text= curday)
                #line_bot_api.push_message(destinationme, TextSendMessage(text=now.date)
                #print (curday+curmonth+curyear+curhour+curmin)
                #print (now.date)
                if(curday == now.day and curmonth == now.month and curyear == now.year):
                #if(1):
                    
                    #print ('correct rolling in')
                    try:
                        result += random.choice(timesay)
                        gdate = (now.strftime("%d-%m-%Y"))
                        result += "\nกำหนดการตารางงาน \nวันนี้ : \n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if '$' in lines:
                                #if str(curmin) in lines:
                                result += lines
                        # Close opend file
                        fo.close()
                        line_bot_api.push_message(destinationme, TextSendMessage(result))
                        break
                    except Exception as e:
                        print (e)
                # Close opend file
                f.close()
                #line_bot_api.push_message(destinationme, TextSendMessage(result))
        except Exception as e:
            print (e)
    if now.hour == 18 and now.minute == 0 and now.second==0:
    #if((now.second==0 or now.second == 30)):
        #print('in condition')
        try:
            result = ''
            #client.send(colonelid,'Second = 0 in function loop')
            #print ('get in try')
            gdate = ""
            
            # Open a file
            f = open("scheduledate", "r+")
            text = f.readlines()
            #print ('readlinedone')
            #line_bot_api.push_message(destinationme, TextSendMessage(text=  "Debug: Printing read line")
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
                #line_bot_api.push_message(destinationme, TextSendMessage(text= curday)
                #line_bot_api.push_message(destinationme, TextSendMessage(text=now.date)
                #print (curday+curmonth+curyear+curhour+curmin)
                #print (now.date)
                if(curday-1 == now.day and curmonth == now.month and curyear == now.year):
                #if(1):
                    
                    #print ('correct rolling in')
                    try:
                        result += random.choice(timesay)
                        gdate = str(curday-1)+'-'+str(curmonth)+'-'+str(curyear)
                        #gdate = (now.strftime("%d-%m-%Y"))
                        result += "\nกำหนดการตารางงาน \nถึงในวันพรุ่งนี้ : \n--------\n"
                        # Open a file
                        fo = open(gdate, "r+")
                        for lines in fo:
                            #print (lines)
                            if True:
                                if '$' in lines:
                                #if str(curmin) in lines:
                                    result += lines
                        # Close opend file
                        fo.close()
                        line_bot_api.push_message(destinationme, TextSendMessage(result))
                        break
                    except Exception as e:
                        print (e)
                # Close opend file
                f.close()
                #line_bot_api.push_message(destinationme, TextSendMessage(result))
        except Exception as e:
            print (e)
    time.sleep(1)
    
    #print (now.second)
