# Standard Entry and Exit

TODO: this has some errors.  I need to address the errors.

These are notes on standard entry and exit routines when calling an external subroutine.

# Calling an external subroutine

When calling an external subroutine, the calling program does the following:

```
        L       R15,=V(SUBPROG)
        BASR    R14,R15
```

In this case, V denotes a virtual literal address, (a `VCON`), in this case SUBPROG.  During
assembly time, the value of the symbol will be 0x00000000.  After linking, an offset to SUBPROG in the load module will be placed in the symbol.  And finally, when bringing the load module into storage, the LOADER will resolve the offset to the actual 
address of the symbol.

By convention, prior to calling, the SAVEAREA address of the calling routine
should be in R13.  Furthermore, the calling program will supply the 
subroutine parameter list address in R1.   Upon return, the calling program 
expects the subroutine to place its return code in R15.

A consequence of the BASR instruction is that operand one, in this case R14, contains
the return address and R15 contains the entry point address of the subroutine.

* Prior to calling the target subroutine, the caller prepares the registers like so:
    * R1 = subroutine parameter list address
    * R13 = calling programs save area address
    * R14 = return address within the calling program that the target will switch to upon exit
    * R15 = target programs entry point address.  This will be the first instruction address in stdentry.

# Standard entry routine using BASR/BALR

BASR/BALR are essentially the same with the caveat that BASR preserves bit 31 
denoting 31-bit addresses whereas the BALR other will zero this bit. BASR is the preferred later method. 

```
Entry:  STM     R14,R12,12(R13)
        BASR    R12,R0
        USING   *,R12
        ST      R13,SAVEAREA+4
        LR      R2,R13
        LA      R13,SAVEAREA
        ST      R13,8(0,R2)   (or simply   ST R13,8(,R2)  ) 
```

Notes:

* Entry will be a label such as `MYMAIN`, `MYSUB`, etc.
* `STM  R14,R12,12(R13)` stores `R14`,`R15`,`R0`,...`R12` in that order to effective address formed from base address in `R13` and offset 12 bytes.  12 bytes is 3 32-bit words.
* The App Dev Guide mentions a `SAVE` macro which does the same thing.


## Alternative #1 using SAVE macro

```
Entry:  STM     R14,R12,12(R13)
        BASR    R12,R0        (or simply  BASR  R12,0  )  
        USING   *,R12
        ST      R13,SAVEAREA+4
        LR      R2,R13
        LA      R13,SAVEAREA
        ST      R13,8(R0,R2)
```

Notes:
* `STM  R14,R12,12(R13)` stores `R14`,`R15`,`R0`,...`R12` in that order to effective address formed from base address in `R13` and offset 12 bytes.  12 bytes is 3 32-bit words.
* The App Dev Guide mentions a `SAVE` macro which does the same thing.


# Standard exit routine

```
STDEXIT L       R13,SAVEAREA+4
        LM      R14,R12,12(R13)
        LA      R15,0
        BR      R14
```

Notes:

Upon exit:

* the target subroutine restores R13 to be the address of the calling programs save area
using the backwards pointer in its save area.
* the target restores the registers with the contents of the callers save area.
* the target places the subroutines (its) return code in R15. zero is normal condition.
* the target uses the address in R14 as the return address.

# Savearea notes

* The first word is used by PL/1 or the OS
* The addresses increase in address. ie. DONTUSE address is the first word and the last word, R12 is +17 words later.
* The linkage conventions use a standarad 72-byte save area.  There are other save area formats that are not discussed here.
* A standard save area is called a F1SA (Format 1 Save Area).  Other popular formats are F4SA (for 64-bit programs) and F7SA (for PC routines)

# Graphic

![img](../../imgs/stdentryexit.png)


# References

* Chapter 10, The Big Blue Assembler Book, David Woolbright
* Page 2-4, Application Development Guide for Assembly Programs, IBM


