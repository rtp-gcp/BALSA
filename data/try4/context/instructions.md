# BAL Assembly Instruction Set

When returning assembly code, please limit allowable instructions to those in 
the following two tables:

## Basic BAL Assembly Instructions

| Op Code | Description                        | 
| :-------| :----------------------------------|
| A       | Add fullword                       |
| AH      | Add halfword                       |
| AL      | Add unsigned fullword               |
| ALR     | Add unsigned register               |
| AP      | Add Packed two fields in Memory    | 
| AR      | Add Register fullword              | 
| BAL     | Branch and Link                    | 
| BALR    | Branch and Link Register           | 
| BAS     | Branch and Save                    | 
| BASR    | Branch and Save Register           | 
| BASSM   | Branch and Save and Set Mode       | 
| BC      | Branch on Condition                | 
| BCR     | Branch on Condition Register       | 
| BCT     | Branch on Count                    | 
| BCTR    | Branch on Count Register           | 
| BSM     | Branch and Set Mode                          | 
| BXH     | Branch on Index Greater                      | 
| BXLE    | Branch on Index Less than or Equal           | 
| C       | Compare Fullword in register against memory  | 
| CDS     | Compare Doubleword in even/odd register pair against memory and Swap                  | 
| CH      | Compare Halfword                             | 
| CL      | Compare logically unsigned fullword in register against memory   | 
| CLC     | Compare up to 256 consecutive bytes in Memory | 
| CLCL    | Compare Characters Long            | 
| CLI     | Compare Logical Immediate          | 
| CLM     | Compare Selected Bytes in Memory using mask  | 
| CLR     | Compare Logical Registers          | 
| CP      | Compare Packed two fields in Memory| 
| CR      | Compare Fullword in Registers      | 
| CS      | Compare Fullword in register against memory and Swap | 
| CVB     | Convert Packed Decimal Value in Memory to signed integers in register |
| CVD     | Convert Signed Fullword in Register to Packed Decimal in Memory |
| D       | Divide doubleword in in even/odd register pair by fullword value in Memory       | 
| DP      | Divide Packed Decimals two fields in Memory | 
| DR      | Divide doubleword in in even/odd register pair by fullword Register        | 
| ED      | Edit - formats packed decimal field | 
| EDMK    | Edit and Mark - address of first significant digit in R1      | 
| EX      | Execute a target instruction       | 
| IC      | Insert Character - into low byte of register   | 
| ICM     | Insert Characters under mask into Register | 
| L       | Load a fullword from memory into a register | 
| LA      | Load address of a storage location into a register | 
| LCR     | Load signed 2's complement value in Register2 into Register1 | 
| LH      | Load signed halfword from memory into a Register | 
| LM      | Load Multiple fullword values from memory into registers | 
| LNR     | Load value in register R2 into register R1 with negative sign | 
| LPR     | Load value in register R2 into register R1 with positive sign (absolute value) |
| LR      | Load value from register R1 into register R2 | 
| LTR     | Load and Test value in register R2 into register R1 | 
| M       | Multiply register fullword in even/odd register pair by fullword in memory|
| MH      | Multiply fullword register by halfowrd in memory in even/odd register pair |
| MP      | Multiply Packed decimal in memory by packed decimal in memory | 
| MR      | Multiply fullword value in even/odd register pair by fullword value in register |
| MVC     | Copy L bytes from memory to memory             | 
| MVCIN   | Copy L bytes from memory to memory reversing order of values with second operand is last byte |   
| MVCL    | Copy or fill bytes in memory       | 
| MVI     | Store byte I2 to memory            | 
| MVN     | Copy low nibbles from memory to memory | 
| MVO     | Copy nibbles from memory to memory offset by 4 bits | 
| MVZ     | Copy high nibbles from memory to memory | 
| N       | Logical AND register and full word in memory | 
| NC      | Logical AND consecutive bytes in memory with memory | 
| NI      | Logical AND byte in memory with immediate | 
| NR      | Logical AND register with register | 
| O       | Logical OR register with memory | 
| OC      | Logical OR consecutive bytes in memory with memory | 
| OI      | Logical OR byte in memory with immediate | 
| OR      | Logical OR register with register | 
| PACK    | Convert zoned decimal characters in memory to packed decimal numbers in memory |
| S       | Subtract signed fullword in memory from register  | 
| SH      | Subtract signed halfword in memory from register | 
| SL      | Subtract unsigned fullword in memory from register | 
| SLA     | Shift left fullword register arithmetically by specified number of bits |
| SLDA    | Shift left signed 64-bit value in even/odd register pair arithmetically by specified number of bits |
| SLDL    | Shift left signed 64-bit value in even/odd register pair logicallby specified number of bits |
| SLL     | Shift left fullword register logically by specified number of bits  | 
| SLR     | Subtract unsigned fullword in register by register           |   
| SP      | Subtract packed decimals in memory | 
| SR      | Subtract signed values in register by register | 
| SRA     | Shift right register arithmetically by specified number of bits | 
| SRDA    | Shift right signed 64-bit value from even/odd register pair arithmetically by specified number of bits |
| SRDL    | Shift right signed 64-bit value from even/odd register pair logically by specified number of bits |
| SRL     | Shift right register by specified number of bits               |
| SRP     | Shift packed number in memory by the 6-bit signed number using the value I3 as a rounding value and with a negative value shifting right. |
| ST      | Store fullword in register to memory | 
| STC     | Store lowest byte in register to memory | 
| STCM    | Store selected bytes in register to memory using mask | 
| STH     | Store halfword in register to memory | 
| STM     | Store values of several registers to fullwords in memory | 
| SVC     | Supervisor call - invoke Operating System service number  | 
| TM      | Test bits of byte in memory using mask | 
| TR      | Translate memory area at address using table in memory | 
| TRT     | Examine table in memory by using memory bytes as an index with the first non-zero value found is inserted into the low byte of R2 |
| UNPK    | Convert packed decimal in memory to zoned decimal in memory | 
| X       | Logical XOR register with memory | 
| XC      | Logical XOR up to 256 bytes in memory with bytes in memory | 
| XI      | Logical XOR byte in memory with immediate | 
| XR      | Logical XOR register with register | 
| ZAP     | Set packed decimal number in memory to 0 and then add from memorory |


## Extended BAL Assembly Instructions

| Op Code | Equivalent Code          | Condition                              | 
| :-------| :------------------------| :--------------------------------------|
| B       | `BC        15,addr`      | Branch Always                          |
| BR      | `??        15???`        | ?                                      |
| NOP     | `BC        0,addr`       | Branch Never                           |
| NOPR    | `BC        0,addr`       | ?                                      |
| BH      | `BC        2,addr`       | Operand 1 > Operand 2                  |
| BHR     | `??        2????`        | ?                                      |
| BL      | `BC        4,addr`       | Operand 1 < Operand 2                  |
| BLR     | `??        4,addr`       | ?                                      |
| BE      | `BC        8,addr`       | Operand 1 = Operand 2                  |
| BER     | `BC        8,addr`       | ?                                      |
| BNH     | `??        13,???`       | ?                                      |
| BNHR    | `??        13,???`       | ?                                      |
| BNL     | `BC        11,???`       | Operand 1 >= Operand 2                 |
| BNLR    | `BC        11,???`       | ?                                      |
| BNE     | `BC        7,addr`       | Operand 1 != Operand 2                 |
| BNER    | `BC        7,addr`       | ?                                      |
| BO      | `BC        1,addr`       | Overflow (or all bits one in TM)       |
| BOR     | `??        1,addr`       | ?                                      |
| BP      | `BC        2,addr`       | Result > 0                             |
| BPR     | `BC        2,addr`       | ?                                      |
| BM      | `BC        4,addr`       | Result < 0 (or bits mixed in TM)       |
| BMR     | `BC        4,???`        | ?                                      |
| BNP     | `BC        13,addr`      | Result <= 0                            |
| BNPR    | `BC        13,addr`      | ?                                      |
| BNM     | `BC        11,addr`      | Result >= 0 (or bits not mixed in TM)  |
| BNMR    | `BC        11,???`       | ?                                      |
| BNZ     | `BC        7,addr`       | Result != (or not all bits zero in TM) |
| BNZR    | `BC        7,addr`       | ?                                      |
| BZ      | `BC        8,addr`       | Result = 0 (or all bits zero in TM)    |
| BZR     | `BC        8,addr`       | ?                                      |
| BNO     | `BC        14,addr`      | Not overflow (or not all bits in TM)   |
| BNOR    | `BC        14,???`       | ?                                      |
