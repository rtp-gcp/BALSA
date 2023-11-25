# ASM1 walkthrough

## URLs

* [linkage](https://www.ibm.com/docs/en/zos/2.4.0?topic=guide-linkage-conventions)
* [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
* [zSystems CPU architecure Principles of Operations](https://www.ibm.com/docs/en/SSQ2R2_15.0.0/com.ibm.tpf.toolkit.hlasm.doc/dz9zr006.pdf)
* [assembly class](https://idcp.marist.edu/assembler-resources)
* [some assembly links](https://punctiliousprogrammer.com)
* [marist conference](https://ecc.marist.edu/web/conference2023/call-for-papers)


Using ASMPGM.s

Using REXX1.pdf as a guide for TSO debugging part

```
$ zowe tso issue command "exec 'z28274.source(somerexx)'" --ssm
```

Start an address space. You can stop an address space with stop.

```
$ zowe tso start as
TSO address space began successfully, key is: Z28274-144-aacmaaas

Z28274 LOGON IN PROGRESS AT 09:04:52 ON MAY 19, 2023
NO BROADCAST MESSAGES
READY
```

Run the same rexx with the address space:

```
$ zowe tso send as Z28274-144-aacmaaas --data "exec 'z28274.source(somerexx)'" 
```

The result is similar, except, now we are issuing the commands through
a semi-persistant TSO address space. . This allows us to run
a program which persists so we can send data to it.

```
$ zowe tso send as Z28274-144-aacmaaas --data "exec 'z28274.source(guessnum)'" 
I'm thinking of a number between 1 and 10.
What is your guess?
$ zowe tso send as Z28274-144-aacmaaas --data "1" 
You got it! And it only took you 1 tries!
READY 
```

For the assembly lab, do this to capture the address space key.

```
$ export ASKEY=`zowe tso start address-space --sko`
$ echo $ASKEY
```

Now tell TSO to start the TEST environment with your assembled program

(Odd. Is it set by default to look in the Z28274.SOURCE() PDS?)

```
$ zowe tso send address-space $ASKEY --data "test (asmpgm)"
TEST  
$ zowe tso send address-space $ASKEY --data "LISTPSW"      
PSW LOCATED AT 7FA160  
  XRXXXTIE   KEY  XMWP  AS CC  PROGMASK  EA BA  INSTR ADDR         
  00000111    8   1101  00 01    0000     0  0   00024F10          
TEST  
```

If the the address space times out:

1. create a new address space
2. restart the test of asmpgm
3. then send the last `at` command that you got to
4. then send `go` to take you back where you were.

* LISTPSW 
    * lists the current address location of your program in last column, INSTR ADDR
* l 0r:15r 
    * lists the current content of 16 registers. r15 is IPC. r14 is the address 
of TSO Ready envirnoment which called the TEST facility.  When TEST facility is ended,
control is returned to the address in r14.
* l 15r% length(240)
    * List the content starting at address location based on register 15. Observe
    the content is machine instructions and data from compile output.
    * For example, the first byte, x47 machine instruction OPCODE was created by the
    B mnemonic at statement 18.
* l 15r% length(240) c
    * List the content starting at address location based on register 15 in character
    format.  Observe the literal text embedded in the assembler program.  The first
    instruction in the program is to branch around the literal 'eye catchers' embedded
    in the executable program.
* l +0 length(240)
    * list the content starting relative address location.  Observe content is the same as 
    listing absolute address location starting at 11F00.
    * The program executable area can be referenced by either relative or absolute
    addressing.
* at +14 (l 0r:15r)
    * Enter the above command to stop program execution at relative address location 14,
    then list the contents of all the registers (using l 0r:15r)
    * at +14 is statement 22 (21? seems more like it), the statement with the SETUP
    label and STM assembler mnemonic.
* at +28 (l 0r:15r)
    * Enter the above command to stop program execution at relative address location 28,
    then list the contents of all the registers (using l 0r:15r)
    * at +28 is instr `L 2, =C'Begin'`, which loads register 2 with content of
    character string `Begin`.
* at +2C (l 2r)
    * List contents of register 2 which now contains the result of `L 2,=C'Begin'`
    * Enter the above command to stop program execution a relative address location
    2C.
* at +30 (l 2r;l +E8 length(5) c)
    * Enter the above command to stop execution at relative address 30, then list
    content of register 2 containing result of `LA 2,=C'Begin'`
    * at +30 subtract register 2 from itself, thus filling register 2 with zeros.
* at +32 (l 2r)
    * register 2 should now contain zero.
* at +32 (l 2r)
    * Observe r2 changed from 0 to 4 as result of `L 2,=F'4'`
* at +3A (l 2r:3r)
    * at +3A is both statement 39 and 40
    * 39 LOOP DS 0H
    * 40      A 3,=F'1'
    * list contents of r2=4 & r3=1 the first time through the loop
* at +3E (l 2r:3r)
    * The program execution is designed to branch back to the +3A location
    therefore setting a breakpoint at +3A it will be executed again.
* at +42
* at +46
* at +4A
* at +84
    * list contents of r2 and r3 then branch to LOOP
    * once register 2 is zero then execution will stop at +42
    * you will need to enter `go` numerous times to proceed with execution
* when execution stops at +42
    * l 2r:3r
    * r=0 and r3=5 when loop stops
* when execution stops at +46
    * l +D0
    * content of value FULLCON is displayed FFFFFFFF
    * why? FULLCON is an example of twos-complement, -1
* go
    * when execution stops at +4A
    * l 3r
    * l +D4
* go
    * when execution stops at +84
    * HEXCON stores the contents of r
* go
    * ASMPGM ternination and return to the TSO TEST facility
* end 
    * terminates the TSO test facility, returning control to TSO

The source is in JCL directory.





* at +14 (1 0r:15r)
    * stop the program execution 





