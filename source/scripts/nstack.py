# *******************************************************************************************
# *******************************************************************************************
#
#		Name : 		nstack.py
#		Purpose :	Dump stack from a dump.bin file.
#		Date :		24th October 2023
#		Reviewed: 	No
#		Author : 	Paul Robson (paul@robsons.org.uk)
#
# *******************************************************************************************
# *******************************************************************************************

import os,sys,re
from utils import *
from floats import *

mem = MemoryBlock()		
ls = LabelSet()
stack = mem.read(ls.get("NStackPointer"))
while stack >= 0:
	print("Stack level {0}:".format(stack))
	exponent = mem.read(ls.get("NSExponent")+stack)
	status = mem.read(ls.get("NSStatus")+stack)
	mantissa = [mem.read(ls.get("NSMantissa"+str(n))+stack) for n in range(0,4)]
	nmantissa = (mantissa[0]) | (mantissa[1] << 8) | (mantissa[2] << 16) | (mantissa[3] << 24)
	if (status & 0x80) != 0:
		assert False
	elif (status & 0x40) == 0:
		print("\tConstant {0}".format(Float().toDecimal([nmantissa,exponent,status])))
	else:
		assert False

	print("\t\tHEX:\tMantissa:${0:08x} Exponent:${1:02x} Status:${2:02x}".format(nmantissa,exponent,status))
	stack -= 1