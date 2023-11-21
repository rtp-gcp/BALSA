# opcodes

HLASM uses Intel style syntax as opposed to ATT style.

```
opcode dst, src

Think:

dst:=src
```

There are 2000 assembly instructions. They are of form:

* Storage and Storage for src  and destination operands.  
    * Storage is synomous with memory
    * SS1 has one length 
    * SS2 has two lengths.
* Register and Register 
    * RR
* Register and Indexed Storage
    * RX
* Register and Storage
    * RS
* Storage Immediate
    * SI


These are old IBM 360 opcode tables

I'm not sure if this was a comprehensive list at that time (1967) or this is just 
a subset by the author.

![one](../../imgs/asm360op-1.JPG)
![two](../../imgs/asm360op-2.JPG)
![three](../../imgs/asm360op-3.JPG)
![four](../../imgs/asm360op-4.JPG)
![five](../../imgs/asm360op-5.JPG)

The pdf from the GA class is [here](../pdfs/InstructionFormats.pdf)

The pdf for the mini reference is [here](../pdfs/mainframe_asm_mini_reference.pdf)

