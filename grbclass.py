#!/usr/bin/python
"""Default python script layout."""

# import

__author__ = "Jonny Elliott"
__copyright__ = "Copyright 2011"
__credits__ =  ""
__license__ = "GPL"
__version__ = "0.0"
__maintainer__ = "Jonny Elliott"
__email__ = "jonnyelliott@mpe.mpg.de"
__status__ = "Prototype"

class GRB(object):
	
	def __init__(self):
		self._RA = ""
		self._DEC = ""
		self._MOON_DIST = ""
		self._SUN_DIST = ""
		self._TIME = ""

	def setRA(self, RA):
		self._RA = RA
	def getRA(self):
		return self._RA

	def setDEC(self, DEC):
		self._DEC = DEC
	def getDEC(self):
		return self._DEC

	def setMOONDIST(self, MOONDIST):
		self._MOON_DIST = MOONDIST
	def setSUNDIST(self, SUNDIST):
		self._SUN_DIST = _SUN_DIST

	def setTIME(self, SETTIME):
		self._TIME = SETTIME
	def getTIME(self):
		return self._TIME

	def enoughProperties(self):

		if self._RA != "" and self._DEC !="" and self._TIME != "":
			return True
		else:
			return False

def main():
	print __doc__

if __name__ == "__main__":
	main()
# Sat Dec 3 12:58:52 CET 2011
