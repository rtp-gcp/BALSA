# instructions

These are the instructions

mach_inst_dict = {
            'A':          ('5A','R1,D2(X2,B2)',       'RX BD DD'),
            'AH':         ('4A','R1,D2(X2,B2)',       'RX BD DD'),
            'AL':         ('5E','R1,D2(X2,B2)',       'RX BD DD'),
            'ALR':        ('1E','R1,R2',              'RR'),
            'AP':         ('FA','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD'),
            'AR':         ('1A','R1,R2',              'RR'),
            'BAL':        ('45','R1,D2(X2,B2)',       'RX BD DD'),
            'BALR':       ('05','R1,R2',              'RR'),
            'BAS':        ('4D','R1,D2(X2,B2)',       'RX BD DD'),
            'BASR':       ('0D','R1,R2',              'RR'),
            'BASSM':      ('0C','R1,R2',              'RR'),
            'BC':         ('47','M1,D2(X2,B2)',       'MX BD DD'),
            'BCR':        ('07','M1,R2',              'MR'),
            'BCT':        ('46','R1,D2(X2,B2)',       'RX BD DD'),
            'BCTR':       ('06','R1,R2',              'RR'),
            'BSM':        ('0B','R1,R2',              'RR'),
            'BXH':        ('86','R1,R3,D2(B2)',       'RR BD DD'),
            'BXLE':       ('87','R1,R3,D2(B2)',       'RR BD DD'),
            'C':          ('59','R1,D2(X2,B2)',       'RX BD DD'),
            'CDS':        ('BB','R1,R3,D2(B2)',       'RR BD DD'),
            'CH':         ('49','R1,D2(X2,B2)',       'RX BD DD'),
            'CL':         ('55','R1,D2(X2,B2)',       'RX BD DD'),
            'CLC':        ('D5','D1(L,B1),D2(B2)',    'LL BD DD BD DD'),
            'CLCL':       ('0F','R1,R2',              'RR'),
            'CLI':        ('95','D1(B1),I2',          'II BD DD'),
            'CLM':        ('BD','R1,M3,D2(B2)',       'RM BD DD'),
            'CLR':        ('15','R1,R2',              'RR'),
            'CP':         ('F9','D1(L1,B1),D2(L2,B2)','L1L2 BD DD BD DD'),
            'CR':         ('19','R1,R2',              'RR'),
            'CS':         ('BA','R1,R3,D2(B2)',       'RR BD DD'),
            'CVB':        ('4F','R1,D2(X2,B2)',       'RX BD DD'),
            'CVD':        ('4E','R1,D2(X2,B2)',       'RX BD DD'),
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
