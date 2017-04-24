#!/usr/bin/python
# -*-coding: utf-8 -*-
import gspread
import os
import re
import random
from datetime import datetime
import json
import sys
from random import randint
if len(sys.argv) < 2:
    sys.exit(0)
#print("Done")
#message = "Debugging "
message = sys.argv[1]
#print (message)
now = datetime.now()
result = ''
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
backasgre_w = ['Thx', 'Thank', 'ขอบคุณโคลอี้', 'appreciate', 'ขอบใจโคลอี้','แต้งโคลอี้']
backasgre_f = ['Your welcome', 'With Pleasure :)', 'with Appreciated', 'Ya', 'Okay ^^', 'Welcome', 'Never mind :)']
menu_cmd = ['pen menu', 'pen Menu', 'เปิดเมนู', 'เรียกเมนู', 'show function', 'Show function', 'Show Menu', 'show menu',
            'Show menu']
simq_ask = ['ho are you', 'hat do you do', 'ho is your boss', 'ho am i', 'ell me a joke', 'ell me some joke','โคลอี้ จ๋า','hloe','โคลอิ','โคอี้','โคลอี','โคลอี้จ๋า','ถามได้ตอบได้','งอะแหละ','โบ้ะ','โบ๊ะ','ตึ่งโป้ะ','ตึ่งโปะ','ตึ่งโป๊ะ','อมึงแหละ','ตึงโป','วดฟ','wtf','โนว','ถามอะไรตอบได้','ด่ามึงอ','นั่นแหละ']
simq_ans = ['I am Chloe The Secretary of Colonel',
            'I am Chloe The Secretary of Colonel ^^ Helping My Master & you guys', 'My Boss or my master is Colonel',
            'Some Human in this world', 'Joke ? google it :)', 'Ahh Nope','จ๋า ?','^^','^^','^^','^^','จ๋าาาา','ได้','ตะลึ่งตึ่งโป้ะ','โพ่ง','โพ่ง','พ่าง','พ่าง','พ่าง','ตะลึงตึ่งโป้ะ','พ่าง','วดฟ+1','wtf+1','โนโน้โนโน้','ไมได้ แบร่','ตะลึงตึ่งโป๊ะ!','ตะลึงตึ่งโป๊ะ!']
randomfive = ['555+','5555+','55555+','5555+','55555+','555555+','55555+','555555+','5555555+','5555+','55555+','555555+','55555+',
'555555+','5555555+','555555+','5555555+','55555555+','55555+','555555+','5555555+','555555+','5555555+','55555555+','5555555+','55555555+','555555555+',]
bank_ask = ['eport accounts', 'ccount reports', 'om engr account', 'pdate account', 'heck amout account',
            'heck amout in account']
bank_ans = ['โอเคจ้า จะทำการอัพเดตให้เดี๋ยวนี้เลย', 'จ้า กำลังอัพเดตให้ละน้า', 'ได้เลยจ้า', 'ได้เลยจ้า แปปเดียวก็เสร็จละ',
            'ค่ะ ทำการตัดดอกเบี้ยทันทีค่ะ', 'ไดเลยจ้า ^^']
getint = ['hloe get interest now','โคลอี้ตัดดอกเบี้ย','ตัดดอกเบี้ยสิ']
# execfile('timeahead.py')
tellasc_cmd = ['tell all associate']
tellasc_ans = ['Okay i will update send msg for you', 'Yes, wait a second', 'Let me work on it', 'Here we go',
               'Alright here is it', 'Ya this one ^^']
# Class def
reinsult = ['กะหรี','กระหรี','สัส','สาส','บ้า','เวร','สาสสสส','สาดดด','ผี']
isinsult = '1'
president = ['ท้อ','ท่อ','ทอ','ท๊อ','ท๋อ','ปธ','ประ','ป่ระ','ปร่ะ','ป่ร่ะ','ปะ','ป่ะ','ป้ะ','ป๊ะ','ป๋ะ','ปท','พรหม','พรม','สุร','นท์','ทร์','พุท','พุธ','รรม','วงศ','วงส','วงษ','เมด','เม่ด','ป.ธ','ป,ธ','ป.ท','ปท','ป,ท','โคล','โคโ','โคอ','ท็อ']
special = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-','.',',','/','\\',' ']     
for tmp in president:
    if tmp in message:
        isinsult = '0'
# if you are not the author, echo

# result = result)
# result =  bot_mode)
# result = bot_status)
# result = status)
# result = '-')
if status == 0 :
    if 'โพ่ง' in message:
        result = message.replace('โพ่ง','พ่อง')
    if 'พ่าง' in message:
        result = message.replace('พ่าง','บ้านบึ้ม')
    if 'บ้านบึ้ม' in message:
        result = message.replace('บ้านบึ้ม','บึ้มพ่อง')
    if 'ฟวย' in message:
        result = 'Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas~'
    if 'ด่า'in message:
        if 'สามช่า' in message:
            result = 'ฟวย ฟวยๆ ฟวย ฟวย'
        if 'อจ' in message:
            result = ''
        if 'อาจา' in message :
            result = ''
    if 'เยส' in message or 'เยด' in message :
        result = 'แน่นอน'
        
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
    for tmp in getint:
        if tmp in message:
            scope = ['https://spreadsheets.google.com/feeds']
            result = random.choice(bank_ans)
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
    for tmp in bank_ask:
        if tmp in message:
            scope = ['https://spreadsheets.google.com/feeds']
            result = random.choice(bank_ans)
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
            gc = gspread.authorize(credentials)
            sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
            worksheet = sh.worksheet('Account')
            cell = worksheet.acell('U31').value
            cellavai = worksheet.acell('U32').value
            sendstr = 'ยอดรายรับ : '
            sendstr = sendstr + str(cell) + '\n' + 'ยอดพึงจ่ายได้ : ' + str(cellavai)
            result = sendstr
            status = 1
            # if status == 0:
            # result = "Sorry I don't know that \nYou can try: \nopen menu \nshow menu \nเรียกเมนู \nเปิดเมนู \nshow function"
if status == 0:
    if 'ขอเบอ' in message:
        if (1):
            scope = ['https://spreadsheets.google.com/feeds']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
            gc = gspread.authorize(credentials)
            sh = gc.open_by_key('1aI55l3bs_BnjXpKGeRb4JIKzngnHOq1ZltiIJvxh4Mc')
            worksheet = sh.worksheet('Sheet1')
            for row in range(2, 34):  # Must be 31 in col or last parameter
                tmp = ''
                tmp = (worksheet.cell(row, 6).value)
                tmp = tmp.encode('utf-8')
                if (tmp in message):
                    answer = str(worksheet.cell(row,7).value)
                    result += 'เบอร์'+ tmp +': ' + answer +'\n'
                    status =1
            if 'เมดี้' in message:
                result =  'เบอร์เมดี้: 09498959xx'
            status = 1
if status == 0:
    if 'ขอเลขนศ' in message:
  	    scope = ['https://spreadsheets.google.com/feeds']
  	    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
  	    gc = gspread.authorize(credentials)
  	    sh = gc.open_by_key('1aI55l3bs_BnjXpKGeRb4JIKzngnHOq1ZltiIJvxh4Mc')
  	    worksheet = sh.worksheet('Sheet1')
  	    for row in range(2, 34):  # Must be 31 in col or last parameter
  	      peruser = 0
  	      tmp = ''
  	      tmp = (worksheet.cell(row, 6).value)
  	      tmp = tmp.encode('utf-8')
  	      if (tmp in message):
  	        answer = str(worksheet.cell(row,2).value)
  	        result += 'เลขรหัสนศ. '+ tmp +': ' + answer+'\n'
  	        status = 1
		#break
  	    if 'เมดี้' in message:
                result =  'ไม่ให้ค่ะ'
            status = 1
if status == 0:
    if 'ขอรหัสนศ' in message:
  	    scope = ['https://spreadsheets.google.com/feeds']
  	    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
  	    gc = gspread.authorize(credentials)
  	    sh = gc.open_by_key('1aI55l3bs_BnjXpKGeRb4JIKzngnHOq1ZltiIJvxh4Mc')
  	    worksheet = sh.worksheet('Sheet1')
  	    for row in range(2, 34):  # Must be 31 in col or last parameter
  	      peruser = 0
	      tmp = ''
  	      tmp = (worksheet.cell(row, 6).value)
	      tmp = tmp.encode('utf-8')
  	      if (tmp in message):
  	        answer = str(worksheet.cell(row,2).value)
  	        result += 'เลขรหัสนศ. '+ tmp +' : ' + answer+'\n'
  	        status = 1
		#break
	    if 'เมดี้' in message:
	      result =  'ไม่ให้ค่ะ'
	    status = 1
insult = ['ด่าอิ','ด่าแม่ง','ด่าไอ','ด่ามัน','ด่าอีก','ด่าาแม่ง','ด่ามันสิ','ด่ามันซิ','ด่าต่อไป','ด่าอย่าหยุด','ด่าอี','ด่าอิ','ด่ามา']

prefixinsult = ['ไอ้','อี','อิ','ไอ']
reinsult2 = ['อิผี','อิผี','อิดอก','อีบลิซซาร์ดไม่คว่ำถ้วย','อีบลิซซาร์ดไม่คว่ำถ้วย','อีบลิซซาร์ดไม่คว่ำถ้วย','อีบลิซซาร์ดไม่คว่ำถ้วย','อีบลิซซาร์ดไม่คว่ำถ้วย','แหวกกอหญ้า','บ้าห้าร้อยจำพวก','ปลวกใต้หลังคา','หน้าปลาจวด',
'บ้องกัญชา','ปลาไม่กินเบ็ด','เห็ดสามสี','อิเห็ดต้มยำ','อิเห็ดต้มยำ',
'กะโหลกซออู้','กู่ไม่กลับ','ตับย่างเกลือ',
'เชื้ออหิวาต์','ม้าขี้ครอก','หอกขึ้นสนิม','ขิมสายขาด',
'ชาติสุนัข','ตะหวักตะบวย','กล้วยตากแห้ง','แกงฟักทอง',
'คลองเจ็ดคด','ชะมดเช็ด','เกล็ดเต็มตัว','มั่วไม่รู้จบ',
'ศพขึ้นอืด','หืดขึ้นคอ','ปลาหมอแถกเหงือก','เผือกรมควัน',
'มันสำปะหลัง','โกดังเก็บศพ','กบผัดเผ็ด','เป็ดทอดกระเทียม',
'ดีไม่ห่างเหิน','เดินไม่ดูทาง','ก้างติดคอ','หม้อก้นทะลุ',
'หัว***','กระจาดปลาแห้ง',
'ปลาทูแม่กลอง','สององคต','หดหัวในกระฎอง','สมองเท่าเมล็ดถั่ว',
'ตัวกินไก่','ใจปลาซิว','หิวตลอดศก','ซกมกเป็นนิจสิน',
'หินใต้บาดาล','เพลงผิดคีย์','สีทาบ้าน',
'จานเปื้อนคราบ','แมลงสาบทรงเครื่อง','เปลืองข้าวสุก','กระปุกตังไฉ่',
'มารสังคม','ผ้าห่มสีซีด','ศพไม่ฉีดฟอร์มาลิน','กระถินริมรั้ว',
'บัวเต่าถุย','กุ๊ยไร้สังกัด','ผัดผักไฟแดง','แพนงกระดูกหมู',
'สาคูน้ำกะทิ','กะปิค้างคืน','หื่นเป็น...','ขวานผ่าซาก',
'กากสิ่งปฏิกูล','พะยูนตากแดด','แรดสองนอ','จอหนังตะลุง',
'ถุงสองใบ','ไข่ลูกเดียว','เคียวห่วยๆ','ถ้วยสังขยาบูด',
'กระต่ายขูดมะพร้าว','ชาวสวนทุเรียน','ตะเพียนหางยาว','ว่าวหางขาด',
'ฉลาดแต่เรื่องโง่','โมฆบุรุษ','มนุษย์สามานย์','เชี่ยวชาญแต่เรื่องชั่ว',
'แกงคั่วหอยขม','นิยมแต่เรื่องผิด','จิตวิปลาส','ทาสเงินตรา',
'ชฎายอดหัก','ไม้หลักปักขี้เลน','จิ้งเหลนหางไหม้','ตะไคร่ในท่อน้ำ',
'ดำตับเป็ด','พูดเท็จหน้าด้านๆ','คอห่านส้วมซึม','อึมครึมตลอดชาติ',
'หาดจอมเทียน','เชี่ยนตะบันหมาก','ปากปลากะโห้','โถส้วมสาธารณะ',
'กระบะใส่ขี้แมว','เรือแจวยี่สิบฝีพาย','ควายเขาหัก','ปลักโคลนเลน',
'ตาเถรตกใต้ถุน','เนรคุณแผ่นดินเกิด','ระเบิดแสวงเครื่อง','ครกกระเดื่องตำข้าว',
'มะพร้าวห้าวยัดปาก','สากกระเบือยัดก้น','คนไททิ้งแผ่นดิน',
'ไพร่เพื่อทัก','บักหำน้อย','กบฏต่อราชบัลลังก์','อีลานจอดนกเอี้ยง']
member = ['แม็ค','พี่ฟา','พี่น้ำ','พี่จูน','ออมสิน','แพรว','มิน','มิ้น','คิตตxี้','มาย','ปืน','พี่','พี','กาย','ออม','ภูมิ','เบียร์','เบีย','แนน','แฟง','จูน','เอิท','ออมสิน','ปอน','แมค','แมก','เจส','มุก','น้ำ','บูม',
          'นั้ม','ทัยรัตน','ภาสวิชญ์','พีมลทิพย์','วรเดช','หลิน','กิ้ก','เก่ง','นิค','ฟาโล','กิ๊ก','นิก','ฟาโร']
if status == 0:
    for tmp in insult:
        if tmp in message:
            if isinsult == '1':
                final = ''
                first = ''
                second = ''
                select = randint(0,3)
                if(select == 0):
                    first = random.choice(prefixinsult)
                    second = random.choice(reinsult)
                    final +=  first + second
                elif(select == 1):
                    final = random.choice(reinsult)
                else:
                    final = random.choice(reinsult2)
                for tmpo in member:  # Must be 31 in col or last parameter
                  if (tmpo in message):
                    current = random.choice(prefixinsult)
                    result = current + tmpo + final + 'ค่ะ'
                    status = 1
                    break
                if status == 0:
		    current = random.choice(prefixinsult)
                    result = current+final +'ค่ะ'
                    status = 1
            else:
                result = 'ขอโทษค่ะหนูด่าไม่ได้ แอแฮร่'
                status = 1
if status == 0:
    if 'ด่า' in message:
        if 'มัน' in message or 'สิ' in message or 'ซิ' in message or 'เดะ' in message or 'เซะ' in message or 'ดิ' in message or 'ที' in message or 'ที' in message:
            if isinsult == '1':
                final = ''
                first = ''
                second = ''
                select = randint(0,3)
                if(select == 0):
                    first = random.choice(prefixinsult)
                    second = random.choice(reinsult)
                    final +=  first + second
                elif(select == 1):
                    final = random.choice(reinsult)
                else:
                    final = random.choice(reinsult2)
                for tmpo in member:  # Must be 31 in col or last parameter
                  if (tmpo in message):
                    current = random.choice(prefixinsult)
		    if 'พี่'not  in message :
                    	result = current + tmpo +current+ final + 'ค่ะ'
			status = 1
                        break
		    else:
			result = current+tmpo+final+'ค่ะ'
			status = 1
			break
            else:
                result = 'ขอโทษค่ะหนูด่าไม่ได้ แอแฮร่'
                status = 1
if status == 0:
    if 'ด่า' in message:
        if 'แหละ' in message:
            if isinsult == '1':
                final = ''
                first = ''
                second = ''
                select = randint(0,3)
                for tmpo in member:  # Must be 31 in col or last parameter
                  if (tmpo in message):
                    ran1 = ['ตึ่งตะลึงตึ่งโป๊ะ','ตะลึงตึงโป้ะ','ตะลึง ตะลึงตึงโป้ะ !']
                    result =  random.choice(ran1)
                    status = 1
                    break               
if status == 0:
    if 'แฮร' in message:
        result = random.choice(randomfive)
        status == 1
if status == 0:
    if 'เพิ่มข้อความระบบ' in message:
        if isinsult == '1':
            stringout = message.replace('เพิ่มข้อความระบบ','')
            fo = open('question', 'r+')
            with open('question') as myFile:
                for num,line in enumerate(myFile,1):
                    if stringout in line:
                        f = open(gdate, 'r+')
                        d = f.readlines()
                        tmpstring = ''
                        for line in d:
                            if line != num
                                tmpstring += line
                        f.close()
                        os.remove('question')
                        fo2 = open('question', 'a')
                        fo2.write(tmpstring)
                        fo2.close()
            fo3 = open('question', 'a')
            fo3.write(stringout + '\n')
            fo3.close()
            result = 'เพิ่มข้อความระบบเรียบร้อยค่ะ'
if status == 0:
    for tmp in simq_ask:
        if tmp in message:
            position = simq_ask.index(tmp)
            result = simq_ans[position]
            status = 1
if status == 0:
    with open('question') as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup in line:
                result = line


print ('%s' % result)
