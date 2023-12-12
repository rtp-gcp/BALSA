When writing code, obey these rules:

* `NAME` corresponds to a `LABEL` and is always in column 1.
* `NAME` is at most 8 characters long.
* `NAME` begins with characters `A-Z`, `a-z`, `$`, `#` or `@`. 
* `OPERATION` or `OPCODE` or `OP CODE` corresponds to an instruction (mnemonic) and starts in column 10.
* `OPERANDS` corresponds to instruction argumennts or parameters and starts in column 15.
* Multiple `OPERANDS` are separated by a comma `,` without a space ` ` between operands.
* `COMMENT` corresponds are identified with a asterisk `*` in column 1 making the entire line non fuctional.

All code should be output in markdown code blocks like so:

```
code here
```

Unless explictly told to do so, do not include any commentary.

When specifiying registers be explicit.  For example when referring to register one, use R1 rather than 1.

Do not show any subroutine standard entry and exit code unless explicitly requested.

Limit allowable instructions to those in this list:

A
AH
AL
ALR
AP
AR
BAL
BALR
BAS
BASR
BASSM
BC
BCR
BCT
BCTR
BSM
BXH
BXLE
C
CDS
CH
CL
CLC
CLCL
CLI
CLM
CLR
CP
CR
CS
CVB
CVD
D
DP
DR
ED
EDMK
EX
IC
ICM
L
LA
LCR
LH
LM
LNR
LPR
LR
LTR
M
MH
MP
MR
MVC
MVCIN
MVCL
MVI
MVN 
MVO
MVZ
N
NC
NI
NR
O
OC
OI
OR
PACK
S
SH
SL
SLA
SLDA
SLDL
SLL
SLR
SP
SR
SRA
SRDA
SRDL
SRL
SRP
ST
STC
STCM
STH
STM
SVC
TM
TR
TRT
UNPK
X
XC
XI
XR
ZAP
B      
BR  
NOP 
NOPR
BH  
BHR 
BL  
BLR 
BE  
BER 
BNH 
BNHR
BNL 
BNLR
BNE 
BNER
BO  
BOR 
BP  
BPR 
BM  
BMR 
BNP 
BNPR
BNM 
BNMR
BNZ 
BNZR
BZ  
BZR 
BNO 
BNOR
