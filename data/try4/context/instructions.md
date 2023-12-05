# BAL Assembly Instruction Set

When considered instructions to these:

| Opcode | Description                        | Opcode and Operands        | Encoding              | Instruction Format Type | 
| :------| :----------------------------------| :--------------------------| :---------------------| :-----------------------|
| A      | Add fullword                       | A     R1,D2(X2,B2)         | 5A RX BD DD           |                         |
| AH     | Add halfword                       | AH    R1,D2(X2,B2)         | 4A RX BD DD           |                         |
| AL     | Add unsigned fullword               | AL    R1,D2(X2,B2)         | 5E RX BD DD           |                         |
| ALR    | Add unsigned register               | ALR   R1,R2                | 1E RR                 |                         |
| AP     | Add Packed two fields in Memory    | AP    D1(L1,B1),D2(L2,B2)  | FA L1L2 BD DD BD DD   |                         |
| AR     | Add Register fullword              | AR    R1,R2                | 1A RR                 |                         |
| BAL    | Branch and Link                    | BAL   R1,D2(X2,B2)         | 45 RX BD DD           |                         |
| BALR   | Branch and Link Register           | BALR  R1,R2                | 05 RR                 |                         |
| BAS    | Branch and Save                    | BAS   R1,D2(X2,B2)         | 4D RX BD DD           |                         |
| BASR   | Branch and Save Register           | BASR  R1,R2                | 0D RR                 |                         |
| BASSM  | Branch and Save and Set Mode       | BASSM R1,R2                | 0C RR                 |                         |
| BC     | Branch on Condition                | BC    M1,D2(X2,B2)         | 47 MX BD DD           |                         |
| BCR    | Branch on Condition Register       | BCR   M1,R2                | 07 MR                 |                         |
| BCT    | Branch on Count                    | BCT   R1,D2(X2,B2)         | 46 RX BD DD           |                         |
| BCTR   | Branch on Count Register           | BCTR  R1,R2                | 06 RR                 |                         |
| BSM    | Branch and Set Mode                | BSM   R1,R2                | 0B RR                 |                         |
| BXH    | Branch on Index Greater            | BXH   R1,R3,D2(B2)         | 86 RR BD DD           |                         |
| BXLE   | Branch on Index Less than or Equal | BXLE  R1,R3,D2(B2)         | 87 RR BD DD           |                         |
| C      | Compare Fullword                   | C     R1,D2(X2,B2)         | 59 RX BD DD           |                         |
| CDS    | Compare Doubleword and Swap        | CDS   R1,R3,D2(B2)         | BB RR BD DD           |                         |
| CH     | Compare Halfword                   | CH    R1,D2(X2,B2)         | 49 RX BD DD           |                         |
| CL     | Compare unsigned fullword                    | CL    R1,D2(X2,B2)         | 55 RX BD DD           | RX                      |
| CLC    | Compare up to 256 consecutive bytes in Memory | CLC  D1(L,B1),D2(B2) | D5 LL BD DD BD DD | SS                      |
| CLCL   | Compare Characters Long            | CLCL  R1,R2                | 0F RR                 | RR                      |
| CLI    | Compare Logical Immediate          | CLI   D1(B1),I2            | 95 II BD DD           | SI                      |
| CLM    | Compare Selected Bytes in Memory using mask  | CLM   R1,M3,D2(B2)     | BD RM BD DD     | RS                      |
| CLR    | Compare Logical Registers          | CLR   R1,R2                | 15 RR                 | RR                      |
| CP     | Compare Packed two fields in Memory| CP   D1(L1,B1),D2(L2,B2)   | F9 L1L2 BD DD BD DD   | SS                      |
| CR     | Compare Fullword in Registers      | CR   R1,R2                 | 19 RR                 | RR                      |
| CS     | Compare Fullword in Register to field in Memory | CS    R1,R3,D2(B2) | BA RR BD DD      | RS                      |
| CVB    | Convert Packed Decimal Values in Memory to signed integers in register | CVB R1,D2(X2,B2)     | 4F RX BD DD           | RX    |
| CVD    | Convert Signed Decimal in Register to Packed Decimal in Memory | CVD R1,D2(X2,B2) | 4E RX BD DD           | RX    |
| D      | Divide Register by value in Memory       | D    R1,D2(X2,B2)          | 5D RX BD DD           | RX                |
| DP     | Divide Packed Decimals two fields in Memory | DP  D1(L1,B1),D2(L2,B2)   | FD L1L2 BD DD BD DD   | SS                      |
| DR     | Divide fullword Register by fullword Register        | DR   R1,R2                 | 1D RR                 | RR                      |
| ED     | Edit - formats packed decimal field | ED   D1(L,B1),D2(B2)      | DE LL BD DD BD DD     | SS                      |
| EDMK   | Edit and Mark - address of first significant digit in R1      | EDMK  D1(L,B1),D2(B2)      | DF LL BD DD BD DD     | SS             |
| EX     | Execute a target instruction       | EX    R1,D2(X2,B2)         | 44 RX BD DD           | RX                      |
| IC     | Insert Character - into low byte of register   | IC    R1,D2(X2,B2)         | 43 RX BD DD           | RX                      |
| ICM    | Insert Characters under mask into Register | ICM    R1,M3,D2(B2) |  BF RM BD DD         | RS                      |
| L      | Load a fullword from memory into a register | L      R1,D2(X2,B2) | 58 RX BD DD         | RX                      |
| LA     | Load address of a storage location into a register | LA  R1,D2(X2,B2) | 41 RX BD DD     | RX                      |
| LCR    | Load signed 2's complement value in Register2 into Register1 | LCR       R1,R2 | 13 RR                 | RR                      |
| LH     | Load signed halfword from memory into a Register | LH     R1,D2(X2,B2) | 48 RX BD DD           | RX               |
| LM     | Load Multiple fullword values from memory into registers | LM       R1,R3,D2(B2) | 98 RR BD DD   | RX                      |
| LNR    | Load value in register R2 into register R1 with negative sign | LNR      R1,R2 | 11 RR | RR                |
| LPR    | Load value in register R2 into register R1 with positive sign (absolute value) | LPR    R1,R2 | 10 RR | RR |
| LR     | Load value from register R1 into register R2 | LR  R1,R2 | 18 RR | RR |
| LTR    | Load and Test value in register R2 into register R1 | LTR    R1,R2 | 12 RR| RR |
| M      | Multiply register fullword in even/odd register pair by fullword in memory| M    R1,D2(X2,B2) | 5C RX BD DD | RX |
| MH     | Multiply fullword register by halfowrd in memory in even/odd register pair | MH   R1,D2(X2,B2) | 4C RX BD DD | RX |
| MP     | Multiply Packed decimal in memory by packed decimal in memory | MP  D1(L1,B1),D2(L2,B2) | FC L1L2 BD DD BD DD | SS |
| MR     | Multiply fullword value in even/odd register pair by fullword value in register | MR      R1,R2 | 1C RR                | RR |
| MVC    | Copy L bytes from memory to memory             | MVC   D1(L,B1),D2(B2)    | D2 LL BD DD BD DD      | SS                      |
| MVCIN  | Copy L bytes from memory to memory reversing order of values        | MVCIN D1(L,B1),D2(B2)    | E8 LL BD DD BD DD      ||
| MVCL   | Copy or fill bytes in memory       | MVCL  R1,R2              | 0E RR                  | RR |
| MVI    | Store byte I2 to memory            | MVI   D1(B1),I2            | 92 II BD DD            | SI |
| MVN    | Copy low nibbles from memory to memory | MVN   D1(L,B1),D2(B2)      | D1 LL BD DD BD DD      | SS |
| MVO    | Copy nibbles from memory to memory offset by 4 bits | MVO   D1(L1,B1),D2(L2,B2)  | F1 L1L2 BD DD BD DD    | SS |
| MVZ    | Copy high nibbles from memory to memory | MVZ   D1(L,B1),D2(B2)      | D3 LL BD DD BD DD      | SS |
| N      | Logical AND register and full word in memory | N     R1,D2(X2,B2)         | 54 RX BD DD            | RX | 
| NC     | Logical AND consecutive bytes in memory with memory | NC    D1(L,B1),D2(B2)     | D4 LL BD DD BD DD      | SS | 
| NI     | Logical AND byte in memory with immediate | NI    D1(B1),I2           | 94 II BD DD            | SI | 
| NR     | Logical AND register with register | NR    R1,R2               | 14 RR                  | RR | 
| O      | Logical OR register with memory | O     R1,D2(X2,B2)         | 56 RX BD DD            | RX | 
| OC     | Logical OR consecutive bytes in memory with memory | OC    D1(L,B1),D2(B2)      | D6 LL BD DD BD DD      | SS | 
| OI     | Logical OR byte in memory with immediate | OI    D1(B1),I2           | 96 II BD DD            | SI | 
| OR     | Logical OR register with register | OR    R1,R2               | 16 RR                  | RR | 
| PACK   | Convert zoned decimal characters in memory to packed decimal numbers in memory | PACK  D1(L1,B1),D2(L2,B2) | F2 L1L2 BD DD BD DD | SS | 
| S      | Subtract signed fullword in memory from register  | S     R1,D2(X2,B2)           | 5B RX BD DD            | RX | 
| SH     | Subtract signed halfword in memory from register | SH    R1,D2(X2,B2)          | 4B RX BD DD            | RX | 
| SL     | Subtract unsigned fullword in memory from register | SL    R1,D2(X2,B2)          | 5F RX BD DD            | RX | 
| SLA    | Shift left register arithmetically by specified number of bits | SLA   R1,D2(X2,B2)         | 8B R0 BD DD            | RS | 
| SLDA   | Shift left signed 64-bit value in even/odd register pair arithmetically by specified number of bits | SLDA  R1,D2(X2,B2)| 8F R0 BD DD      | RS | 
| SLDL   | Shift left signed 64-bit value in even/odd register pair logically by specified number of bits | SLDL  R1,D2(X2,B2)        | 8D R0 BD DD   | RS | 
| SLL    | Shift left register logically by specified number of bits  | SLL   R1,D2(X2,B2)         | 89 R0 BD DD            | RS | 
| SLR    | Subtract unsigned fullword in register by register                | SLR   R1,R2                | 1F RR                  | RR | 
| SP     | Subtract packed decimals in memory | SP    D1(L1,B1),D2(L2,B2)   | FB L1L2 BD DD BD DD    | SS | 
| SR     | Subtract signed values in register by register | SR    R1,R2                 | 1B RR                  | RR | 
| SRA    | Shift right register arithmetically by specified number of bits | SRA   R1,D2(X2,B2)        | 8A R0 BD DD            | RS | 
| SRDA   | Shift right signed 64-bit value from even/odd register pair arithmetically by specified number of bits | SRDA  R1,D2(X2,B2)        | 8E R0 BD DD    | RS |
| SRDL   | Shift right signed 64-bit value from even/odd register pair logically by specified number of bits | SRDL  R1,D2(X2,B2)        | 8C R0 BD DD            | RS |
| SRL    | Shift right register by specified number of bits               | SRL   R1,D2(X2,B2)         | 88 R0 BD DD            | RS |
| SRP    | Shift packed number in memory by the 6-bit signed number a negative value shifts right, using the value I3 as a rounding value. | SRP   D1(L1,B1),D2(B2),I3  | F0 LI BD DD BD DD | SS |
| ST     | Store fullword in register to memory | ST    R1,D2(X2,B2)          | 50 RX BD DD            | RX |
| STC    | Store lowest byte in register to memory | STC   R1,D2(X2,B2)         | 42 RX BD DD      | RX |
| STCM   | Store selected bytes in register to memory using mask | STCM  R1,M3,D2(B2)        | BE RM BD DD            | RS |
| STH    | Store halfword in register to memory | STH   R1,D2(X2,B2)         | 40 RX BD DD            | RX |
| STM    | Store values of several registers to fullwords in memory | STM   R1,R3,D2(B2)         | 90 RR BD DD            | RS |
| SVC    | Supervisor call - invoke Operating System service number  | SVC   I1                   | 0A II                  | I |
| TM     | Test bits of byte in memory using mask | TM    D1(B1),I2             | 91 II BD DD            | SI |
| TR     | Translate memory area at address using table in memory | TR    D1(L,B1),D2(B2)       | DC LL BD DD BD DD      | SS |
| TRT    | Examine memory by bytes using table, a non-zero value is inserted into the low byte of R2 | TRT   D1(L,B1),D2(B2)      | DD LL BD DD BD DD      | SS |
| UNPK   | Convert packed decimal in memory to zoned decimal in memory | UNPK  D1(L1,B1),D2(L2,B2) | F3 L1L2 BD DD BD DD    | SS |
| X      | Logical XOR register with memory | X     R1,D2(X2,B2)           | 57 RX BD DD            | RX |
| XC     | Logical XOR up to 256 bytes in memory with bytes in memory | XC    D1(L,B1),D2(B2)       | D7 LL BD DD BD DD      | SS |
| XI     | Logical XOR byte in memory with immediate | XI    D1(B1),I2             | 97 II BD DD            | SI |
| XR     | Logical XOR register with register | XR    R1,R2                 | 17 RR                  | RR |
| ZAP    | Set packed decimal number in memory to 0 and then add from memory | ZAP   D1(L1,B1),D2(L2,B2)  | F8 L1L2 BD DD BD DD    | SS |


# Extended instructions

           'B': '15',
            'BR': '15',
            'NOP': '0',
            'NOPR': '0',
            'BH': '2',
            'BHR': '2',
            'BL': '4',
            'BLR': '4',
            'BE': '8',
            'BER': '8',
            'BNH': '13',
            'BNHR': '13',
            'BNL': '11',
            'BNLR': '11',
            'BNE': '7',
            'BNER': '7',
            'BO': '1',
            'BOR': '1',
            'BP': '2',
            'BPR': '2',
            'BM': '4',
            'BMR': '4',
            'BNP': '13',
            'BNPR': '13',
            'BNM': '11',
            'BNMR': '11',
            'BNZ': '7',
            'BNZR': '7',
            'BZ': '8',
            'BZR': '8',
            'BNO': '14',
            'BNOR': '14' }
