
'''
This file will take in a dictionary and an output file name. It will create a bloom filter
file (written to the output file)

Inputs are: 
    dictionary filter_name desired_accuracy
'''



import random
import sys
import numpy
import math


SIZE = pow(2 , 1000)
f = open(sys.argv[1], 'r') 
numDictionaryItenms = 0
#space efficent way to read all the lines in the document sometimes the dictionary
for line in f:
    numDictionaryItenms += 1
f.close()

#caluclate ideal ratios for file size based off of desired accuracy
idealRatio = (-1 * numpy.log(float(sys.argv[2]))) / pow(numpy.log(2) , 2)
idealBits = idealRatio*numDictionaryItenms 

#caulcutate size of filter in practice and number of hash functions
size = 8 * math.ceil( idealBits / 8 )
k = round(size * numpy.log(2) / numDictionaryItenms)
FILTER = 0
#write to the filter
f = open(sys.argv[1], 'r') 
for line in f:
    for i in range(k):
        FILTER = FILTER | (pow(2, hash(line.strip() + str(i)) % size))

outputfile = sys.argv[1] + "-" + str(size) + "-" + str(k)+ ".bin"
print(FILTER)
with open(outputfile, 'wb') as file:
    file.write((FILTER).to_bytes(250, byteorder='big', signed=False))


