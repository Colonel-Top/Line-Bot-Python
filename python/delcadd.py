#!/usr/bin/python
# -*-coding: utf-8 -*-
import os
import re
import random
import fileinput
from datetime import datetime
import json
import time
import sys
from random import randint
if len(sys.argv) < 2:
    sys.exit(0)

#message = "Debugging "
message = sys.argv[1]
#print (message)
now = datetime.now()
result = ''

line = message
with open("userId.txt", "r+") as myfile:
    if line+"\n" not in myfile:
        myfile.write(line+"\n")
