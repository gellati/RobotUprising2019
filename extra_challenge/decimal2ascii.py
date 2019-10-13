#!/bin/python

sourceString = "67 82 51 52 49 45 99 117 110 110 105 110 103 45 105 110 115 101 114 116 45 105 110 116 101 114 102 101 114 101 110 99 101"

sourceStringArray = sourceString.split()

letterArray = []

for number in sourceStringArray:
  print ">" + number + "<"
  letterArray.append(chr(int(number)))

letterString = ''.join(letterArray)

print letterString


