#!/usr/bin/python
import urllib

## http://stackoverflow.com/questions/1726402/in-python-how-do-i-use-urllib-to-see-if-a-website-is-404-or-200

print " * * * This programs checks if a given URL list (input.txt) haves broken URLs * * *"
print "\tEach line should contain a single url to check "

strFile = raw_input("What is the input file?: ")
fh = open (strFile , 'r')
strData = fh.read()
fh.close()

listData = []
for row in strData.split("\n"):
	if row.strip() != '' :
		listData.append(row.strip())
		
nCorrect = 0
nBroken = 0
		
for strUrl in listData:	
	req = urllib.urlopen(strUrl)
	nStatusCode = req.getcode()
	if nStatusCode == 200:
		nCorrect += 1
	else:
		nBroken += 1
		print "%s\t[%s]" % (strUrl, nStatusCode)

print " #### %d broken URLs      %d correct URLs    (%d total) " % (nBroken, nCorrect, len(listData) )


raw_input(" Press enter to exit... ")
