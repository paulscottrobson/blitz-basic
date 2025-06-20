; ************************************************************************************************
; ************************************************************************************************
;
;		Name:		zeropage.inc
;		Purpose:	Zeropage usage (common data)
;		Created:	24th October 2023
;		Reviewed: 	No
;		Author:		Paul Robson (paul@robsons.org.uk)
;
; ************************************************************************************************
; ************************************************************************************************

; ************************************************************************************************
;
;								Define sections and locations
;
; ************************************************************************************************

		.section zeropage

; ************************************************************************************************
;
;									Numeric stack
;
; ************************************************************************************************

StackSize = 8
;
;	Status: bit 7 : reference bit 6 : string bit 0 : sign bit.
;
NSStatus:
			.fill 		StackSize
NSExponent:
			.fill 		StackSize
NSMantissa0:	
			.fill 		StackSize
NSMantissa1:	
			.fill 		StackSize
NSMantissa2:	
			.fill 		StackSize
NSMantissa3:	
			.fill 		StackSize
			
NStackPointer:								; current numeric stack pointer.
			.fill 		1

		.send zeropage

; ************************************************************************************************
;
;									Changes and Updates
;
; ************************************************************************************************
;
;		Date			Notes
;		==== 			=====
;
; ************************************************************************************************
