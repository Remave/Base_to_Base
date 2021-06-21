#!/usr/bin/python

# Base_to_Base universal library for convertions and coding

# Bases (alphabets)
b2 = '01'
b4 = '0123'
b8 = '01234567'
b10 = '0123456789'
b16 = '0123456789abcdef'
b32 = 'abcdefghijklmnopqrstuvwxyz234567'
b62 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# A number n to other base (10->to)
def numtobase(n:int, to:''):
	if n==0:
		return '0'
	else:
		a =[]
		r =''
		while n != 0:
			a.append(n%len(to))
			n = n//len(to)
		a=a[::-1]
		for i in a:
			r+= to[i] 
		return r

# From base to number (from->10)
def basetodec(s:str, from_:''):
	s =s[::-1]
	a =[]
	r =0
	x =0
	for c in s:
		a.append(from_.index(c))
	for i in a:
		r+= i*len(from_)**x
		x+=1
	return r

# Convert a base to other base
# s    : input string
# in_  : input base of s string
# out_ : output base
def basetobase(s, in_, out_):
	# if s == NULL or in_ == NULL or out_ == NULL:
	# 	return NULL
	return numtobase(basetodec(s, in_),out_)

# n:int or str (10->2)
def dectobin(n):
	if type(n)is str: n=int(n)
	return numtobase(n, b2)

# n:int or str (10->8)
def dectooct(n):
	if type(n)is str: n=int(n)
	return numtobase(n, b8)

# n:int or str (10->16)
def dectohex(n):
	if type(n)is str: n=int(n)
	return numtobase(n, b16)

# n:str (8->2)
def octtobin(n:str):
	return basetobase(n, b8, b2)

# n:str (8->10)
def octtodec(n:str):
	return basetobase(n, b8, b10)

# n:str (8->16)
def octtohex(n:str):
	return basetobase(n, b8, b16)

# n:str (16->2)
def hextobin(n:str):
	return basetobase(n, b16, b2)

# n:str (16->8)
def hextooct(n:str):
	return basetobase(n, b16, b8)

# n:str (16->10)
def hextodec(n:str):
	return basetobase(n, b16, b10)

# n:str (2->8)
def bintooct(n:str):
	return basetobase(n, b2, b8)

# n:str (2->10)
def bintodec(n:str):
	return basetobase(n, b2, b10)

# n:str (2->16)
def bintohex(n:str):
	return basetobase(n, b2, b16)
