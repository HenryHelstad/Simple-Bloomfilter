#!/usr/bin/python
import os
#from Crypto.Cipher import AES
#from Crypto.Util.Padding import pad, unpad
from base64 import b64encode
import sys
from binascii import hexlify
from itertools import cycle
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
#functions
import hashlib
import string
import random
import time

BFSIZE = 100000000
NUMTIME = 0

# set up bloom filters
BF3 = [] 
BF5 = []
BF3 = [0 for i in range(BFSIZE)]
BF5 = [0 for i in range(BFSIZE)]

#BF5 = [0 for i in range(256)]


def get_rand_str():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(0,10))
    return result_str

def get_hash(m,i):
    m = salt_pass(m,i)
    return ((int(hashlib.sha256(m).hexdigest(), 16) % BFSIZE) - 1)

saltList = [get_rand_str(), get_rand_str(), get_rand_str(), get_rand_str(), get_rand_str()] 

#print saltList

def salt_pass(m,i):
    global saltList
    return saltList[i] + m

def add_hash_bf3(i):
    global BF3
    BF3[i] = 1

def add_hash_bf5(i):
    global BF5
    BF5[i] = 1

def add_pass_bf(p):
    for i in range(0,5):
        #print i
        n = (get_hash(p,i))
        if i < 3:
            add_hash_bf3(n)
        add_hash_bf5(n)

def hash_bf3(i):
    global BF3
    return BF3[i]

def hash_bf5(i):
    global BF5
    return BF5[i]


def check_pass(p):
    hashl = []
    bf3 = 0
    bf5 = 0 
    global NUMTIME
    for i in reversed(range(0,5)):
        #print i
        if i == 4 and NUMTIME > 0:
            start_time_bf5 = time.time()
        if i == 2 and NUMTIME > 0:
            start_time_bf3 = time.time()
        hashl.append(get_hash(p,i))
    
    if NUMTIME > 0:
        start_time_bf3check = time.time() 
    
    if hash_bf3(hashl[4]) and  hash_bf3(hashl[3]) and hash_bf3(hashl[2]):
        bf3 = 1
    
    if NUMTIME > 0:
        end_time_bf3 = time.time()
    
    if hash_bf5(hashl[0]) and  hash_bf5(hashl[1]) and hash_bf5(hashl[2]) and  hash_bf5(hashl[3]) and hash_bf5(hashl[4]):
        bf5 = 1
    
    if NUMTIME > 0:
        end_time_bf5 = time.time()
        print "Time BF3: ",(end_time_bf3 - start_time_bf3),"  TimeBF5: ",(end_time_bf5 - ( end_time_bf3 - start_time_bf3check) - start_time_bf5 )
        NUMTIME -= 1
    
    return bf3, bf5



#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

if len(sys.argv) != 8:
    print "not enough arguments need 8"
    exit()

#print 'program continues', sys.argv[2]

# initialize bloom filters
f = open(sys.argv[2], 'rd')
while 1:
    data = f.readline()
    if not data:
        break
    data = data.rstrip("\n")
    data = data.rstrip()
    add_pass_bf(data)
    #print data 
f.close()


#test password list
fINPUT = open(sys.argv[4], 'rd')
if os.path.exists(sys.argv[6]):
    os.remove(sys.argv[6])
if os.path.exists(sys.argv[7]):
    os.remove(sys.argv[7])

fOUTPUT3 = open(sys.argv[6], 'w')
fOUTPUT5 = open(sys.argv[7], 'w')

while 1:
    data = fINPUT.readline()
    if not data:
        break
    data = data.rstrip("\n")
    data = data.rstrip()
    bf3, bf5 = check_pass(data)
#    print bf3, " : ", bf5
    if bf3 == 1:
        fOUTPUT3.write("no\n")
    else:
        fOUTPUT3.write("maybe\n")
    if bf5 == 1:
        fOUTPUT5.write("no\n")
    else:
        fOUTPUT5.write("maybe\n")
    #
    #print data 

fINPUT.close()
fOUTPUT3.close()
fOUTPUT5.close()

#if BF3 == BF5:
#    print "error!!!"
#else:
#    print "looks good"
#print BF3    
 
#store results
