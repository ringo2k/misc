#!/usr/bin/python

import sys
print "first parameter the file"

print sys.argv[1]

fileName = sys.argv[1]


fileObj = open(fileName, "r")


for line in fileObj:
  line = line.replace(" ","_")
  line = line.replace("-","")
  line = line.replace("-","")
  if len(line) > 2 :
    print line



