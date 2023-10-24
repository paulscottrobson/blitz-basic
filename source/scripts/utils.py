# *******************************************************************************************
# *******************************************************************************************
#
#		Name : 		utils.py
#		Purpose :	Miscellaneous utilities
#		Date :		24th October 2023
#		Reviewed: 	No
#		Author : 	Paul Robson (paul@robsons.org.uk)
#
# *******************************************************************************************
# *******************************************************************************************

import os,sys,re

# *******************************************************************************************
#
#									Dump.bin handler class
#
# *******************************************************************************************

class MemoryBlock(object):
	def __init__(self):
		self.data = [x for x in open("dump.bin","rb").read(-1)]
	def read(self,addr):
		return self.data[addr]

# *******************************************************************************************
#
#									Label handler class
#
# *******************************************************************************************

class LabelSet(object):
	def __init__(self):
		self.labels = {}
		for s in open("build"+os.sep+"code.lbl","r").readlines():
			m = re.match("^(.*?)\\s*\\=\\s*(\\$?[0-9A-Fa-f]+)\\s*$",s)
			assert m is not None,"Cannot decode "+s
			if m.group(2).startswith("$"):
				n = int(m.group(2)[1:],16)
			else:
				n = int(m.group(2))
			self.labels[m.group(1).lower()] = n
	#
	def get(self,label):
		label = label.strip().lower()
		return self.labels[label] if label in self.labels else None


