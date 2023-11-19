# SYSPROG-JLS

Notes regarding the work of James Salvino.

Mr. Salvino has an assembler and emulator that is helpful for the S/370
subset of IBM BAL assembly.  He has written two python projects that
can assemble and emulate.

## Usage

### Assembly

Add the code to the root of the S370BALAsm git repo.  In this case the source file
is named `john.s370`.  Assemble with the following command.  The repo is [here](https://github.com/SYSPROG-JLS/S370BALAsm)

```
$ cd S370BALAsm
$ python3 S370BALAsm.py john
```

### Exercise the assembly code using the Emulator

From the assembly directory, invoke the emulator using the debug option.  This
will bring up the Text UI and allow the code to be exercised.  The repo is [here](https://github.com/SYSPROG-JLS/S370BALEmulator)

```
$ cd 
$ cd S370BALAsm
$ python3 ../S370BALEmulator/S370BALEmulator.py -debug
```

### Emulator Command Guide

* s 
    - single step
* dm
    - display memory
    - dm 4 8
        - dump 8 bytes of memory starting at address 0x00000004
* df
    - display field
* x
    - exit
* g
    - go. run until exit or breakpoint
* sb
    - set breakpoint
* cb
    - clear breakpoint
* db
    - display breakpoint
* sd
    - set execution delay in ms

## Notes on the instructions in the sample

### BALR

This is a branch instruction.  See page 89 of the Germain book.  This is from the 
book regarding Branching instructions

45    BAL         Branch and Link [RX]
05    BALR        Branch and Link [RR]

When BALR is used an R2=0, no branch occurs and the next instruction in 
sequence is taken.  This form is useful for setting a base register.
The instruction `BALR R1, 0` loads the address of BALR+2 into register
R1 and then goes to the next instruction.

Usually an instruction of this form is the first instructino of a program
and all other addresses are referred to in terms of a displacement from the
base address.  In this way it is posible for the program to be relocated
anywhere in core and still work correctly.








