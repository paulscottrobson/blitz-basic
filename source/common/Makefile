# *******************************************************************************************
# *******************************************************************************************
#
#		Name : 		Makefile
#		Purpose :	Floating point library makefile.
#		Date :		5th October 2023
#		Author : 	Paul Robson (paul@robsons.org.uk)
#
# *******************************************************************************************
# *******************************************************************************************

#
#		Bl**dy Windows.
#
ifeq ($(OS),Windows_NT)
include ..\..\documents\common.make
else
include ../../documents/common.make
endif

LIBNAME = data

all:  build
	
build:
	$(PYTHON) $(CSCRIPTS)build.py  00data_header data_common data_task zzdata_footer
	$(CCOPY) build$(S)library.code $(LIBDIR)$(LIBNAME).library
	$(CCOPY) build$(S)library.link $(LIBDIR)$(LIBNAME).link