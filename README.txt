

To run the program:
./bloom_filter.py  -d dictionary.txt -i input.txt -o output3.txt output5.txt

///////////////// it may take a couple of seconds for the program to finish /////////////////////

dictionary.txt input.txt output3.txt output5.txt 
	can be any file you want as long as they fill their respective role to the program
	if any of the output files are already created on runtime the program will delete
		 and remake said output file


there shouldn't be any dependency issues but if there are
pip install pycryptodome

you may need to give bloom_filter.py execute privileges
	chmod +x bloom_filter.py

///////////////////////////////////IF YOU WANT TO CHANGE STUFF/////////////////////////////////////

if you want to change the size of the bloom filter change the global variable: BFSIZE 

if you want to print the times for each bloom filter to check a password change: NUMTIME
	NUMTIME is the number of times you want the passwork check time to print 
  
