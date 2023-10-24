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
include ..\..\..\documents\common.make
else
include ../../../documents/common.make
endif

LIBNAME = ifloat

all:  test

test : build
	$(ASM) __main.asm $(LIBDIR)data.library

build: datasegment
	$(PYTHON) $(CSCRIPTS)build.py source -rom1		
	$(CCOPY) build$(S)library.code $(LIBDIR)$(LIBNAME).library

datasegment:
	make -B -C $(SRCDIR)common
