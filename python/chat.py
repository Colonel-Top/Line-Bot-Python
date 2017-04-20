#!/usr/bin/python
# -*-coding: utf-8 -*-
import gspread
import os
import random
from datetime import datetime
import json
import sys
if len(sys.argv) < 2:
    sys.exit(0)
#print("Done")
#message = "Debugging "
message = sys.argv[1]
#print (message)
now = datetime.now()
result = ""
from oauth2client.service_account import ServiceAccountCredentials

status = 0
# print ('Google API Connected')
def Login():
    #print ('Messenger API Connected')
    scope = ['https://spreadsheets.google.com/feeds']
    state = '0'
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
    worksheet = sh.worksheet('Account')
    #print ('Google API Connected')


bot_status = 0
bot_mode = 0
# define hi or hello
greeting_w = ['Hello', 'Hi ', 'Greeting', 'สวัสดี', 'hello', 'hi ', 'greetings', 'sup', 'whats up', 're you here',
              'หวัดดี']
greeting_f = ['May i help you please ?', 'Yes ?', 'Ya Anything you want ?', 'Anything ? ya ?', 'Greeting yes ?',
              'Always here']
backasgre_w = ['Thx', 'Thank', 'ขอบคุณ', 'appreciate', 'ขอบใจ']
backasgre_f = ['Your welcome', 'With Pleasure :)', 'with Appreciated', 'Ya', 'Okay ^^', 'Welcome', 'Never mind :)']
menu_cmd = ['pen menu', 'pen Menu', 'เปิดเมนู', 'เรียกเมนู', 'show function', 'Show function', 'Show Menu', 'show menu',
            'Show menu']
simq_ask = ['ho are you', 'hat do you do', 'ho is your boss', 'ho am i', 'ell me a joke', 'ell me some joke']
simq_ans = ['I am Chloe The Secretary of Colonel',
            'I am Chloe The Secretary of Colonel ^^ Helping My Master & you guys', 'My Boss or my master is Colonel',
            'Some Human in this world', 'Joke ? google it :)', 'Ahh Nope']

bank_ask = ['eport account', 'ccount report', 'om engr account', 'pdate account', 'heck amout account',
            'heck amout in account']
bank_ans = ['Okay i will update account for you', 'Yes, wait a second', 'Let me check account', 'Here we go',
            'Alright here is it', 'Ya this one ^^']

# execfile('timeahead.py')
tellasc_cmd = ['tell all associate']
tellasc_ans = ['Okay i will update send msg for you', 'Yes, wait a second', 'Let me work on it', 'Here we go',
               'Alright here is it', 'Ya this one ^^']
# Class def


# if you are not the author, echo

# result = result)
# result =  bot_mode)
# result = bot_status)
# result = status)
# result = '-')
if bot_mode == 1 and bot_status == 1 and status == 0:
    try:
        gdate = message[0:10]
        jobhour = message[11:13]
        jobmin = message[14:16]
        content = message[11:]
        # content.encode('utf-8')
        fo = open(gdate, 'a')
        fo.write(content + '\n')
        fo.close()
        fo = open('serverdate', 'a')
        fo.write(gdate + ',' + jobhour + ',' + jobmin + '\n')
        fo.close()
        result = 'เพิ่มตารางงาน,นัดหมายเรียบร้อยค่ะ'
    except Exception as e:
        result = 'การเพิ่มตารางเวลาล้มเหลว' + e
    bot_mode = 0
    bot_status = 0
    status = 1
if bot_mode == 2 and bot_status == 1 and status == 0:
    try:
        linetoremove = int(message[0])
        gdate = (now.strftime('%d-%m-%Y'))
        f = open(gdate, 'r+')
        d = f.readlines()
        tmpstring = ''
        for line in d:
            if line != linetoremove - 1:
                tmpstring += line
        f.close()
        os.remove(gdate)
        fo = open(gdate, 'a')
        fo.write(tmpstring)
        fo.close()
        result = 'ลบตารางงานดังกล่าวเรียบร้อย'
    except Exception as e:
        result = e
        result = 'การลบตารางเวลาล้มเหลว'
    bot_mode = 0
    bot_status = 0
    status = 1
if bot_status == 1 and status == 0:
    if 'a' in message:
        bot_mode = 1
        result = 'เพิ่มงาน,ตารางเวลานัดหมายได้\nกรุณาใช้รูปแบบดังต่อไปนี้ \n\n31-12-2017:22:00:เนื้อหางาน'
        status = 1
    if 'A' in message:
        bot_mode = 1
        result = 'เพิ่มงาน,ตารางเวลานัดหมายได้\nกรุณาใช้รูปแบบดังต่อไปนี้ \n\n31-12-2017:22:00:เนื้อหางาน'
        status = 1
    if 'b' in message:
        try:
            gdate = (now.strftime('%d-%m-%Y'))
            # Open a file
            fo = open(gdate, 'r+')
            strws = fo.read()
            result = 'รายการตารางงานและการนัดหมายวันนี้\n'+gdate +'\n'+ strws
            # Close opend file
            fo.close()
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
        bot_status = 0
        bot_mode = 0
        status = 1
    if 'B' in message:
        try:
            gdate = (now.strftime('%d-%m-%Y'))
            # Open a file
            fo = open(gdate, 'r+')
            strws = fo.read()
            result = 'รายการตารางงานและการนัดหมายวันนี้\n'+gdate +'\n' + strws
            # Close opend file
            fo.close()
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
        bot_status = 0
        bot_mode = 0
        status = 1
    if 'c' in message:
        try:
            gdate = (now.strftime('%d-%m-%Y'))
            # Open a file
            fo = open(gdate, 'r+')
            strws = fo.read()
            result = 'รายการตารางงานและการนัดหมายวันนี้\n' + gdate +'\n' + strws + '\nกรุณาใส่เลขหัวข้องานที่ต้องการจะลยเช่น 3'
            # Close opend file
            fo.close()
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
        bot_mode = 2
        bot_status = 1
        status = 1
    if 'C' in message:
        try:
            gdate = (now.strftime('%d-%m-%Y'))
            # Open a file
            fo = open(gdate, 'r+')
            strws = fo.read()
            result = 'รายการตารางงานและการนัดหมายวันนี้\n' + gdate+'\n' + strws + '\nกรุณาใส่เลขหัวข้องานที่ต้องการจะลยเช่น 3'
            # Close opend file
            fo.close()
        except:
            result = 'ไม่พบตารางเวลาหรือการอ่านล้มเหลว'
        bot_mode = 2
        bot_status = 1
        status = 1
    if 'D' in message:
        bot_mode = 0
        bot_status = 0
        status = 1
    if 'd' in message:
        bot_mode = 0
        bot_status = 0
        status = 1
if status == 0:
    for tmp in tellasc_cmd:
        if tmp in message:
            going = tmp.replace('tell all associate', '')
            stringtosend = 'result From Colonel : '
            stringtosend += strs(going)
            result = random.choice(tellasc_ans)
            # self.send(100002210119100,'result From Colonel : ' + going) #Aomsin
            # self.send(100001717587402,'result From Colonel : ' + going) #Beer
            # self.send(100000337186822,'result From Colonel : ' + going) #Pond
            result = stringtosend  # me
            status = 1
if status == 0:
    for tmp in greeting_w:
        if tmp in message:
            result = random.choice(greeting_f)
            status = 1
if status == 0:
    for tmp in menu_cmd:
        if tmp in message:
            result = 'กรุณาเลือกฟังก์ชัน\n'+'a.เพิ่มงาน,ตารางนัดหมาย\nb.ตรวจสอบตารางเวลางาน\nc.ลบตารางเวลานัดหมาย\nd.เพื่อย้อนกลับ/ยกเลิก'
        bot_status = 1
        status = 1
if status == 0:
    if 'Ok' in message:
        result = '^^'
        status = 1
    elif 'ok' in message:
        result = '^^'
        status = 1
if status == 0:
    if 'Get Interest Now' in message:
        result = random.choice(bank_ans)+( 'AI has Awaken and Collecting Interest')
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
        gc = gspread.authorize(credentials)
        sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
        worksheet = sh.worksheet('Account')
        cell = worksheet.acell('U31').value
        cell = cell.encode('utf-8')
        monthcell = now.month
        monthcell += 9
        # onthcell += 10
        for row in range(2, 31):  # Must be 31 in col or last parameter
            peruser = 0
            for col in range(8, 20):
                tmp = worksheet.cell(row, col).value
                #print(tmp)
                if (tmp == '0'):
                    peruser += 1
            # print('Done Per loop')
            # print (peruser)
            if peruser >= 2 and worksheet.cell(row, monthcell).value == '':
                interest = int(worksheet.cell(row, 22).value)
                interest += 1
            # print (interest)
                worksheet.update_cell(row, 22, interest)
            if worksheet.cell(row, monthcell).value == '':
                worksheet.update_cell(row, monthcell, 0)
            if row == 8:
                #print('Skip Safe')
                continue
        status = 1
if status == 0:
    for tmp in backasgre_w:
        if tmp in message:
            result = random.choice(backasgre_f)
            status = 1
if status == 0:
    for tmp in simq_ask:
        if tmp in message:
            position = simq_ask.index(tmp)
            result = simq_ans[position]
            status = 1
if status == 0:
    for tmp in bank_ask:
        if tmp in message:
            result = random.choice(bank_ans)
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
            gc = gspread.authorize(credentials)
            sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
            worksheet = sh.worksheet('Account')
            cell = worksheet.acell('U31').value
            sendstr = 'Current Amount in Account : '
            sendstr = sendstr + str(cell)
            result = sendstr
            status = 1
            # if status == 0:
            # result = "Sorry I don't know that \nYou can try: \nopen menu \nshow menu \nเรียกเมนู \nเปิดเมนู \nshow function"

print ('%s' % result)
