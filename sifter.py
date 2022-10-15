import sys
'''
comandline arguments:
    bloomfilter.bin size num_hashes checked_data
'''


#reads in the filter
with open(sys.argv[1], 'rb') as file:
        FILTER = int.from_bytes(file.read(), byteorder='big')

size = int(sys.argv[2])
k = int(sys.argv[3])
b = 1

#checks the hashes against the filter
for i in range(k):
    if not (pow(2, hash(sys.argv[4] + str(i)) % size) & FILTER == pow(2, hash(sys.argv[4] + str(i)) % size)):
        print(sys.argv[4] + " is not in the list")
        quit()

print(sys.argv[4] + " is likely in the list")


