# instructions

These are the instructions


| Opcode | Description                        | Opcode and Operands        | Encoding              | Instruction Format Type | 
| :------| :----------------------------------| :--------------------------| :---------------------| :-----------------------|
| A      | Add                                | A     R1,D2(X2,B2)         | 5A RX BD DD           |                         |
| AH     | Add halfword                       | AH    R1,D2(X2,B2)         | 4A RX BD DD           |                         |
| AL     | Add ???                            | AL    R1,D2(X2,B2)         | 5E RX BD DD           |                         |
| ALR    | Add ??                             | ALR   R1,R2                | 1E RR                 |                         |
| AP     | Add ??                             | AP    D1(L1,B1),D2(L2,B2)  | FA L1L2 BD DD BD DD   |                         |
| AR     | Add Register                       | AR    R1,R2                | 1A RR                 |                         |
| BAL    | Branch and Link                    | BAL   R1,D2(X2,B2)         | 45 RX BD DD           |                         |
| BALR   | Branch and Link Register           | BALR  R1,R2                | 05 RR                 |                         |
| BAS    | Branch ???                         | BAS   R1,D2(X2,B2)         | 4D RX BD DD           |                         |
| BASR   | Branch ??                          | BASR  R1,R2                | 0D RR                 |                         |
| BASSM  | Branch ??                          | BASSM R1,R2                | 0C RR                 |                         |
| BC     | Branch on Condition                | BC    M1,D2(X2,B2)         | 47 MX BD DD           |                         |
| BCR    | Branch on Condition Register       | BCR   M1,R2                | 07 MR                 |                         |
| BCT    | Branch on Count                    | BCT   R1,D2(X2,B2)         | 46 RX BD DD           |                         |
| BCTR   | Branch on Count Register           | BCTR  R1,R2                | 06 RR                 |                         |
| BSM    | Branch ???                         | BSM   R1,R2                | 0B RR                 |                         |
| BXH    | Branch on Index Greater            | BXH   R1,R3,D2(B2)         | 86 RR BD DD           |                         |
| BXLE   | Branch on Index Less than or Equal | BXLE  R1,R3,D2(B2)         | 87 RR BD DD           |                         |
| C      | Compare Fullword                   | C     R1,D2(X2,B2)         | 59 RX BD DD           |                         |
| CDS    | Compare ???                        | CDS   R1,R3,D2(B2)         | BB RR BD DD           |                         |
| CH     | Compare Halfword                   | CH    R1,D2(X2,B2)         | 49 RX BD DD           |                         |
| CL     | Compare Unsigned Fullword          | CL    R1,D2(X2,B2)         | 55 RX BD DD           | RX                      |
| CLC    | Compare upto 256 consecutive bytes in Memory | CLC  D1(L,B1),D2(B2) | D5 LL BD DD BD DD | SS                      |
| CLCL   | Compare Characters Long            | CLCL  R1,R2                | 0F RR                 | RR                      |
| CLI    | Compare Logical Immediate          | CLI   D1(B1),I2            | 95 II BD DD           | SI                      |
| CLM    | Compare Selected Bytes in Memory using mask  | CLM   R1,M3,D2(B2)     | BD RM BD DD     | RS                      |
| CLR    | Compare Registers                  | CLR   R1,R2                | 15 RR                 | RR                      |
| CP     | Compare Packed two fields in Memory| CP   D1(L1,B1),D2(L2,B2)   | F9 L1L2 BD DD BD DD   | SS                      |
| CR     | Compare Signed Value in Register   | CR   R1,R2                 | 19 RR                 | RR                      |
| CS     | Compare Fullword in Register to field in Memory | CS    R1,R3,D2(B2) | BA RR BD DD      | RS                      |
| CVB    | Convert Packed Decimal Values in Memory to signed integers | CVB R1,D2(X2,B2)     | 4F RX BD DD           | RX    |
| CVD    | Convert Signed Decimal in Register to Packed Decimal in Memory | CVD R1,D2(X2,B2) | 4E RX BD DD           | RX    |







  
  

           
            

            'D':          ('5D','R1,D2(X2,B2)',       'RX BD DD'),
            'DP':         ('FD','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD'),
            'DR':         ('1D','R1,R2',              'RR'),
            'ED':         ('DE','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'EDMK':       ('DF','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'EX':         ('44','R1,D2(X2,B2)',       'RX BD DD'),
                        'IC':         ('43','R1,D2(X2,B2)',       'RX BD DD'),
            'ICM':        ('BF','R1,M3,D2(B2)',       'RM BD DD'),
            'L':          ('58','R1,D2(X2,B2)',       'RX BD DD'),
            'LA':         ('41','R1,D2(X2,B2)',       'RX BD DD'),
            'LCR':        ('13','R1,R2',              'RR'),
            'LH':         ('48','R1,D2(X2,B2)',       'RX BD DD'),
            'LM':         ('98','R1,R3,D2(B2)',       'RR BD DD'),
            'LNR':        ('11','R1,R2',              'RR'),
            'LPR':        ('10','R1,R2',              'RR'),
            'LR':         ('18','R1,R2',              'RR'),
            'LTR':        ('12','R1,R2',              'RR'),
            'M':          ('5C','R1,D2(X2,B2)',       'RX BD DD'),
            'MH':         ('4C','R1,D2(X2,B2)',       'RX BD DD'),
            'MP':         ('FC','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD'),
            'MR':         ('1C','R1,R2',              'RR'),
            'MVC':        ('D2','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'MVCIN':      ('E8','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'MVCL':       ('0E','R1,R2',              'RR'),
            'MVI':        ('92','D1(B1),I2',          'II BD DD'),
            'MVN':        ('D1','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'MVO':        ('F1','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD'),
            'MVZ':        ('D3','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'N':          ('54','R1,D2(X2,B2)',       'RX BD DD'),
            'NC':         ('D4','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'NI':         ('94','D1(B1),I2',          'II BD DD'),
            'NR':         ('14','R1,R2',              'RR'),
            'O':          ('56','R1,D2(X2,B2)',       'RX BD DD'),
            'OC':         ('D6','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'OI':         ('96','D1(B1),I2',          'II BD DD'),
            'OR':         ('16','R1,R2',              'RR'),
            'PACK':       ('F2','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD'),
            'S':          ('5B','R1,D2(X2,B2)',       'RX BD DD'),
            'SH':         ('4B','R1,D2(X2,B2)',       'RX BD DD'),
            'SL':         ('5F','R1,D2(X2,B2)',       'RX BD DD'),
            'SLA':        ('8B','R1,D2(X2,B2)',       'R0 BD DD'),
            'SLDA':       ('8F','R1,D2(X2,B2)',       'R0 BD DD'),
            'SLDL':       ('8D','R1,D2(X2,B2)',       'R0 BD DD'),
            'SLL':        ('89','R1,D2(X2,B2)',       'R0 BD DD'),
            'SLR':        ('1F','R1,R2',              'RR'),
            'SP':         ('FB','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD'),
            'SR':         ('1B','R1,R2',              'RR'),
            'SRA':        ('8A','R1,D2(X2,B2)',       'R0 BD DD'),

                        'SRDA':       ('8E','R1,D2(X2,B2)',       'R0 BD DD'),
            'SRDL':       ('8C','R1,D2(X2,B2)',       'R0 BD DD'),
            'SRL':        ('88','R1,D2(X2,B2)',       'R0 BD DD'),
            'SRP':        ('F0','D1(L1,B1),D2(B2),I3','LI BD DD BD DD'),
            'ST':         ('50','R1,D2(X2,B2)',       'RX BD DD'),
            'STC':        ('42','R1,D2(X2,B2)',       'RX BD DD'),
            'STCM':       ('BE','R1,M3,D2(B2)',       'RM BD DD'),
            'STH':        ('40','R1,D2(X2,B2)',       'RX BD DD'),
            'STM':        ('90','R1,R3,D2(B2)',       'RR BD DD'),
            'SVC':        ('0A','I1',                 'II'),
            'TM':         ('91','D1(B1),I2',          'II BD DD'),
            'TR':         ('DC','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'TRT':        ('DD','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'UNPK':       ('F3','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD'),
            'X':          ('57','R1,D2(X2,B2)',       'RX BD DD'),
            'XC':         ('D7','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'XI':         ('97','D1(B1),I2',          'II BD DD'),
            'XR':         ('17','R1,R2',              'RR'),
            'ZAP':        ('F8','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD') }


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

