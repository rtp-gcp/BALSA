# directives

These are the recognized directives of the S370BALAsm assembler.  These are the 
associated directives for BALSA.

## USING base, register

```
label     using base,reg[,reg..] 
```

Define to assembler that register reg will contain address base (which may be a name of a section) and can be used as base register when resolving symbols to addresses. More than one register can be specified, then they are assumed to be incremented by 4K with respect to the previous one. If label is specified, then same symbol in two overlapping USING ranges can be resolved using the label.symbol notation.



## USING base, memory

```
         using base,addr
```

Define dependent using. The symbols starting from the address base (which may be a name of a section) will be resolved to addresses by means that addr is resolved.

## DROP `[reg | label],...`


```
         drop base
```

Undefine previous USING instruction. Operand is either register reg currently used as a base or label of previous USING (if it was labeled, then you must use the label). More than one registers/labels to drop can be specified at once.

## CSECT


```
label    CSECT
```

Start a new control section named label.

## LTORG

```
         LTORG
```


Force generation of literal pool. Normally, literal pool is generated at the end of section.


## PRINT `ops,...[,NOPRINT]`


```
         PRINT ops,...[,NOPRINT]
```

Select which statements will be printed into the listing, where `ops` is comma delimited list of operands, can be: `ON`, `OFF`, `[NO]GEN`, `[NO]DATA`, `[NO]MCALL`.

## DC


```
label    DC   [r]type[Llen]value
```

Define data constant. Type of constant is given by type type (see table). Default length can be changed to len. Converts value to appropriate representation and stores it within the program (advancing location counter). The expression will be repeated r times.

## DS


```
label    DS   [r]type[Llen][value]
```
Define space for data. Type of constant is given by type type (see table). Default length can be changed to len. Discards the actual value, only advances location counter by its length. The expression will be repeated r times.


## EQU


```
label    EQU. addr[,len]
```


Associate an address expression (absolute or relocatable) addr, and optionally length len, with symbol label.


## END

```
         END
```

End of assembly

