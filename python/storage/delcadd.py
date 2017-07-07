#!/usr/bin/python
# -*-coding: utf-8 -*-
import os
import re
import random
import MySQLdb
import fileinput
from datetime import datetime
import json
import time
import sys
from random import randint
if len(sys.argv) < 2:
    sys.exit(0)
message = sys.argv[1]
db = MySQLdb.connect("colonel-tech.com","delcsql","D3!C_3duc@ti0n","DELC_DB" )
cur = db.cursor()
def Connection():
    global db,cur
    db = MySQLdb.connect("colonel-tech.com","delcsql","D3!C_3duc@ti0n","DELC_DB" )
#message = "Debugging "

#print (message)
now = datetime.now()
result = ''
valuetopush = True

#tmpres = int(cur.execute("SELECT No FROM `LineUserId` WHERE No=(SELECT MAX(No) FROM `LineUserId`);"))
#print(tmpres)

query = "SELECT COUNT(*) FROM LineUserId WHERE userId = '%s'" % message
try:
    cur.execute(query)
    results = cur.fetchone()[0]
    #print(results)
    #print((results[0]))
    
    if results != 0:
        valuetopush = False
        print('You already Subscribe !')
    else:
        valuetopush = True
    if valuetopush == True:
        now = datetime.now()
        gdate = (now.strftime("%Y-%m-%d"))
        cur.execute("SELECT MAX(No) FROM `LineUserId`")
        result_set = cur.fetchall()
        lastNumber = (int(result_set[0][0]))+1
        #print(lastNumber)
        cur.execute("INSERT INTO LineUserId (No,userId,RegDate) VALUE (%s,%s,%s)",(str(lastNumber),message,gdate))
        
        db.commit()
        db.close()
        
        #print("INSERT INTO LineUserId (No,userId,RegDate) VALUE (%s,%s,%s)"%(str(lastNumber),message,gdate))
        print('Register Subscribe Successful \nWelcome to DELC NEWS')
except Exception as E:
    print ('Error: Cannot Fetch Data')
    print (E)

#with open("userId.txt", "r+") as file:
#for line in file:
#        if message in line:
#           break
#        else: # not found, we are at the eof
#            file.write(message+"\n") # append missing data
#            print('Register Successful')
