import sys
import os

firstIgnore = 31 
lastIgnore = 8 

def saveInitial(file, input, rango):
	textFile = open(input, 'r')
	x = 0
	savedfile = open(file, 'w')
	config=textFile.readlines()
	while x < rango:
		savedfile.write(config[x])
		x = x+1
	savedfile.close()
	textFile.close()
	
def getLineCount(input):
	textFile = open(input, 'r')
	y=1
	for line in textFile.readlines():
		y=y+1
	return int(y)
	textFile.close()
	
def SaveLast(file, input, rango):
	textFile = open(input, 'r')
	x=0
	y=0
	savedfile=open(file, 'a+b')
	config=textFile.readlines()
	totalLines=getLineCount(input)
	while x < rango:
		y=totalLines-rango+x-1
		savedfile.write(config[y])
		x = x+1
	savedfile.close()
	textFile.close()
	
def saveReverse(file, input):
	global lastIgnore
	global firstIgnore
	currentLine=1
	totalLines=getLineCount(input)
	initialCfg=lastIgnore
	principio=firstIgnore
	lastCfg=totalLines-principio
	textFile = open(input, 'r')
	savedfile = open(file, 'a+b')
	for line in reversed(textFile.readlines()):
		if currentLine > initialCfg and currentLine < lastCfg:
			savedfile.write(line)		
			currentLine = currentLine + 1
		else:
			currentLine = currentLine + 1
	savedfile.close()	
	textFile.close()

f1=sys.argv[1]

if len(sys.argv) < 2:
    print "Error: Please specify a file"
    exit(-1)   



saveInitial("reversed", f1, firstIgnore)
saveReverse("reversed", f1)
SaveLast("reversed", f1, lastIgnore)
