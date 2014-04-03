#!/usr/bin/env python

import re
import sys

target = "abc123 kkk444 342342 3123123 231313  wtf434"


def match(pattern):
	typelist = []
	opflag = 0
	typemap = {0:"[a-z]",1:"[A-Z]",2:"\d",3:"\S",4:"\s"}
	for i in pattern:
		if i == '[':
			opflag += 1
		if i == ']':
			opflag -= 1
		if opflag >= 1:
			if opflag == 1 and i == '[':
				continue
			else:
				typelist.append(i)
			print 'specific'
			#enter specific word check mode
		else:
			if opflag == 0 and i == '[' or i == ']':
				continue
			#normal symobic mode
			if ord(i) >= 97 and ord(i) <= 122:
					typelist.append(0)
			elif ord(i) >= 65 and ord(i) <= 90:
					typelist.append(1)
			elif ord(i) >= 48 and ord(i) <= 57:
					typelist.append(2)
			elif ord(i) >= 33 and ord(i) <= 47 or ord(i) >= 58 and ord(i) <= 64 or ord(i) >= 91 and ord(i) <= 96 or ord(i) >= 123 and ord(i) <= 126:
					typelist.append(3)
			else:
					typelist.append(4)
		print i, opflag
	regexstr = ""
	for j in typelist:
		if type(j) is str:
			regexstr += j
		else:
			regexstr += typemap[j]
	return '('+regexstr+')'


#print json.dumps()

#outputre = match('[[][\/+]~!@#$%^&''""**()_+}|]')
outputre = match('def555')
print outputre

s = outputre
m = re.findall(s, target)
print m

#quote need to escape =.=
#ascii decimal number
#0: char : 97 ~ 122 (lowercase)
#1: 65 ~ 90 (uppercase)
#2: digit : 48 ~ 57
#3: symbol : 33 ~ 47 , 58 ~ 64, 91 ~ 96 , 123 ~ 126
#4: space : 32

