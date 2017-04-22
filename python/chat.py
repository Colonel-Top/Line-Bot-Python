#!/usr/bin/python
# -*-coding: utf-8 -*-
import gspread
import os
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
backasgre_w = ['Thx', 'Thank', 'ขอบคุณ', 'appreciate', 'ขอบใจ','แต้ง']
backasgre_f = ['Your welcome', 'With Pleasure :)', 'with Appreciated', 'Ya', 'Okay ^^', 'Welcome', 'Never mind :)']
menu_cmd = ['pen menu', 'pen Menu', 'เปิดเมนู', 'เรียกเมนู', 'show function', 'Show function', 'Show Menu', 'show menu',
            'Show menu']
simq_ask = ['ho are you', 'hat do you do', 'ho is your boss', 'ho am i', 'ell me a joke', 'ell me some joke','โคลอี้ จ๋า','hloe','โคลอิ','โคอี้','โคลอี','โคลอี้จ๋า','ถามได้ตอบได้','ศราวุธ','งอะแหละ','โบ้ะ','โบ๊ะ','ตึ่งโป้ะ','ตึ่งโปะ','ตึ่งโป๊ะ','อมึงแหละ','ตึงโป','วดฟ','wtf','โนว','ถามอะไรตอบได้','ด่ามึงอ่ะ']
simq_ans = ['I am Chloe The Secretary of Colonel',
            'I am Chloe The Secretary of Colonel ^^ Helping My Master & you guys', 'My Boss or my master is Colonel',
            'Some Human in this world', 'Joke ? google it :)', 'Ahh Nope','จ๋า ?','^^','^^','^^','^^','จ๋าาาา','ได้','ไม่พบศราวุธในสารบบ','ตะลึ่งตึ่งโป้ะ','โพ่ง','โพ่ง','พ่าง','พ่าง','พ่าง','ตะลึงตึ่งโป้ะ','พ่าง','วดฟ+1','wtf+1','โนโน้โนโน้','ไมได้ แบร่','ตะลึงตึ่งโป๊ะ!']
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
isinsult = True
president = ['ท้อ','ท่อ','ทอ','ท๊อ','ท๋อ','ปธ','ประ','ป่ระ','ปร่ะ','ป่ร่ะ','ปะ','ป่ะ','ป้ะ','ป๊ะ','ป๋ะ','ปท','พรหม','พรม','สุร','นท์','ทร์','พุท','พุธ','รรม','วงศ','วงส','วงษ','เมด','เม่ด']
checkfirst = ''.join(e for e in message if e.isalnum())
for tmp in checkfirst:
    if tmp in president:
        isinsult = False
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
	#print (message[0])
	#if (message[0]=='ข') :
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
  	        answer = str(worksheet.cell(row,7).value)
  	        result += 'เบอร์'+ tmp +': ' + answer +'\n'
		#print (result)
  	        status = 1
		#break
	    if 'เมดี้' in message:
	      result =  'เบอร์เมดี้: 09498959xx'
	    if not result:
	      result = 'ไม่พบชื่อหรือเบอร์ที่คุณหา'
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
	    if not result:
	      result = 'ไม่พบชื่อหรือเบอร์ที่คุณหา'
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
	    if not result:
	      result = 'ไม่พบชื่อหรือสิ่งที่คุณหา'
	    status = 1
insult = ['ด่าอิ','ด่าแม่ง','ด่าไอ']
reinsult = ['กะหรี','กระหรี','สัส','สาส','บ้า','เวร','สาสสสส','สาดดด']
prefixinsult = ['ไอ้','อี','อิ','ไอ']
reinsult2 = ['อิผี','อิดอก','อีบลิซซาร์ดไม่คว่ำถ้วย','ไอ้แหวกกอหญ้า','ไอ้บ้าห้าร้อยจำพวก','ไอ้ปลวกใต้หลังคา','ไอ้หน้าปลาจวด',
'ไอ้บ้องกัญชา','ไอ้ปลาไม่กินเบ็ด','ไอ้เห็ดสามสี',
'ไอ้กะโหลกซออู้','ไอ้กู่ไม่กลับ','ไอ้ตับย่างเกลือ',
'ไอ้เชื้ออหิวาต์','ไอ้ม้าขี้ครอก','ไอ้หอกขึ้นสนิม','ไอ้ขิมสายขาด',
'ไอ้ชาติสุนัข','ไอ้ตะหวักตะบวย','ไอ้กล้วยตากแห้ง','ไอ้แกงฟักทอง',
'ไอ้คลองเจ็ดคด','ไอ้ชะมดเช็ด','ไอ้เกล็ดเต็มตัว','ไอ้มั่วไม่รู้จบ',
'ไอ้ศพขึ้นอืด','ไอ้หืดขึ้นคอ','ไอ้ปลาหมอแถกเหงือก','ไอ้เผือกรมควัน',
'ไอ้มันสำปะหลัง','ไอ้โกดังเก็บศพ','ไอ้กบผัดเผ็ด','ไอ้เป็ดทอดกระเทียม',
'ไอ้ดีไม่ห่างเหิน','ไอ้เดินไม่ดูทาง','ไอ้ก้างติดคอ','ไอ้หม้อก้นทะลุ',
'ไอ้หัว***','ไอ้กระจาดปลาแห้ง',
'ไอ้ปลาทูแม่กลอง','ไอ้สององคต','ไอ้หดหัวในกระฎอง','ไอ้สมองเท่าเมล็ดถั่ว',
'ไอ้ตัวกินไก่','ไอ้ใจปลาซิว','ไอ้หิวตลอดศก','ไอ้ซกมกเป็นนิจสิน',
'ไอ้หินใต้บาดาล','ไอ้เพลงผิดคีย์','ไอ้สีทาบ้าน',
'ไอ้จานเปื้อนคราบ','ไอ้แมลงสาบทรงเครื่อง','ไอ้เปลืองข้าวสุก','ไอ้กระปุกตังไฉ่',
'ไอ้มารสังคม','ไอ้ผ้าห่มสีซีด','ไอ้ศพไม่ฉีดฟอร์มาลิน','ไอ้กระถินริมรั้ว',
'ไอ้บัวเต่าถุย','ไอ้กุ๊ยไร้สังกัด','ไอ้ผัดผักไฟแดง','ไอ้แพนงกระดูกหมู',
'ไอ้สาคูน้ำกะทิ','ไอ้กะปิค้างคืน','ไอ้หื่นเป็น...','ไอ้ขวานผ่าซาก',
'ไอ้กากสิ่งปฏิกูล','ไอ้พะยูนตากแดด','ไอ้แรดสองนอ','ไอ้จอหนังตะลุง',
'ไอ้ถุงสองใบ','ไอ้ไข่ลูกเดียว','ไอ้เคียวห่วยๆ','ไอ้ถ้วยสังขยาบูด',
'ไอ้กระต่ายขูดมะพร้าว','ไอ้ชาวสวนทุเรียน','ไอ้ตะเพียนหางยาว','ไอ้ว่าวหางขาด',
'ไอ้ฉลาดแต่เรื่องโง่','ไอ้โมฆบุรุษ','ไอ้มนุษย์สามานย์','ไอ้เชี่ยวชาญแต่เรื่องชั่ว',
'ไอ้แกงคั่วหอยขม','ไอ้นิยมแต่เรื่องผิด','ไอ้จิตวิปลาส','ไอ้ทาสเงินตรา',
'ไอ้ชฎายอดหัก','ไอ้ไม้หลักปักขี้เลน','ไอ้จิ้งเหลนหางไหม้','ไอ้ตะไคร่ในท่อน้ำ',
'ไอ้ดำตับเป็ด','ไอ้พูดเท็จหน้าด้านๆ','ไอ้คอห่านส้วมซึม','ไอ้อึมครึมตลอดชาติ',
'ไอ้หาดจอมเทียน','ไอ้เชี่ยนตะบันหมาก','ไอ้ปากปลากะโห้','ไอ้โถส้วมสาธารณะ',
'ไอ้กระบะใส่ขี้แมว','ไอ้เรือแจวยี่สิบฝีพาย','ไอ้ควายเขาหัก','ไอ้ปลักโคลนเลน',
'ไอ้ตาเถรตกใต้ถุน','ไอ้เนรคุณแผ่นดินเกิด','ไอ้ระเบิดแสวงเครื่อง','ไอ้ครกกระเดื่องตำข้าว',
'ไอ้มะพร้าวห้าวยัดปาก','ไอ้สากกระเบือยัดก้น','ไอ้คนไททิ้งแผ่นดิน',
'ไอ้ไพร่เพื่อทัก','ไอ้บักหำน้อย','ไอ้กบฏต่อราชบัลลังก์','อีลานจอดนกเอี้ยง']
member = ['แพรว','มิน','มิ้น','คิตตี้','มาย','ปืน','พี','กาย','ออม','ภูมิ','เบียร์','เบีย','แนน','แฟง','จูน','เอิท','ออมสิน','ปอน','แมค','แมก','เจส','มุก','น้ำ','บูม',
          'นั้ม','ทัยรัตน','ภาสวิชญ์','พีมลทิพย์','วรเดช','หลิน','กิ้ก','เก่ง','นิค','ฟาโล','กิ๊ก','นิก']
if status == 0:
    for tmp in insult:
        if tmp in message:
            if isinsult == True:
                final = ''
                first = ''
                second = ''
                select = randint(0,2)
                if(select == 0):
                    first = random.choice(prefixinsult)
                    second = random.choice(reinsult)
                    final +=  first + second
                elif(select == 1):
                    final = random.choice(reinsult)
                elif(select == 2):
                    final = random.choice(reinsult2)
                for tmpo in member:  # Must be 31 in col or last parameter
                  if (tmpo in message):
                    current = random.choice(prefixinsult)
                    result = current + tmpo + ' '+ final + 'ค่ะ'
                    status = 1
                    break
                if status == 0:
                    result = final
                    status = 1
            else:
                result = 'ขอโทษค่ะหนูด่าไม่ได้ แอแฮร่'
                status = 1
if status == 0:
    if 'ด่า' in message:
        if 'มัน' in message:
            if isinsult == True:
                final = ''
                first = ''
                second = ''
                select = randint(0,2)
                if(select == 0):
                    first = random.choice(prefixinsult)
                    second = random.choice(reinsult)
                    final +=  first + second
                elif(select == 1):
                    final = random.choice(reinsult)
                elif(select == 2):
                    final = random.choice(reinsult2)
                for tmpo in member:  # Must be 31 in col or last parameter
                  if (tmpo in message):
                    current = random.choice(prefixinsult)
                    result = current + tmpo + ' '+ final + 'ค่ะ'
                    status = 1
                    break
            else:
                result = 'ขอโทษค่ะหนูด่าไม่ได้ แอแฮร่'
                status = 1
if status == 0:
    if 'แฮร' in message:
        result = random.choice(randomfive)
        status == 1
if status == 0:
    for tmp in simq_ask:
        if tmp in message:
            position = simq_ask.index(tmp)
            result = simq_ans[position]
            status = 1
print ('%s' % result)
