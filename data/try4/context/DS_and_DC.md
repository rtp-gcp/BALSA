# Defining fields with DS and DC

DC and DS are assembler directives.  In both case, they are for associating a field name with a reserved area in memory (storage).

* DS means to define storage for variables
* DC is similar but it defines constants

DS fields have the following components

* NAME - an optional word which starts in column 1
* DS - starts in column 10 is the keyword which means this is a define storage directive
* REPETITION FACTOR - also known as DUPLICATION FACTOR, an optional number of how many times storage is repeated.
* DATA TYPE - a single character defining the type of storage.  The options are below:
    - C - character fields. 8-bits
    - F - Fullword fields 32-bits
    - H - Halfword fields. 16-bits
* L - an optional character specifying the following integer specifies the amount of data reserved
    - number - When the L is specifed, this number must be present
* CONSTANT - an optional value for the intial value stored at this location.


## Examples:

This is a ruler to ensure column starting locations are correct.

```
          1         2         3         4         5         6         7         8
012345678901234567890123456789012345678901234567890123456789012345678901234567890
```

### Example 1

This defines 20 bytes of character data which is unitialized and has the field name of `PARTNAME`.

```
PARTNAME  DS    CL20  
```

### Example 2

This defines an unamed region of memory of 20 bytes.  In other words an unamed 20 byte character field.

```
          DS    CL20  
```

### Example 3

This defines two uninitialized character fields of 20 bytes each.   The first filed is called `PARTNAME`.  The second field is unamed.

```
PARTNAME  DS    2CL20  
```


### Example 4

This defines a field of 41 character bytes.  The leading 0 corresponding to a repitation factor for the customer name in line 1 suppresses 
the advancement of the location counter, so `NAME` and `FNAME` begin at the same location in memory.  ie. the address for 
location specified by NAME and FNAME are equivalent.  In terms of C, this would analogous to a union.  The result is that
the following fields `FNAME`, `MI`, and `LNAME` are considered subfields of `NAME`.

```
NAME      DS    0CL41          CUSTOMER NAME
FNAME     DS     CL20          CUSTOMER FIRST NAME
MI        DS     CL1           CUSTOMER MIDDLE INITIAL
LNAME     DS     CL20          CUSTOMER LAST NAME
```

### Example 5

This defines a 6-byte character field named `ITEM`.  The field is uninitialized even though the constant is coded. Constants coded using `DS` directives are ignored. It is a common error to code a constant using a `DS` directive and thinking the field will be initialized.


```
ITEM      DS    CL6'HAMMER'
```


### Example 6

This defines a 18-fullword region named `SAVEAREA`.  This region is for saving registers and restoring registers in a subroutine.

```
SAVEAREA  DS    18F
```

### Example 7

`DS`/`DC` statements can be named or unnamed.   

`DS` statements can also be specified with a zero duplication factor.  This is done not to reserve storage, but to align storage by affecting the current location counter.  Alignment options when using a `DS` statement with a zero duplication factor are:

* byte
* halfword
* fullword
* doubleword
* quadword

In this example, the assembler would cause the location counter to be aligned on a doubleword boundary. It's implied that the next use of storage, either for an instruction or other use of storage, requires doubleword alignment.

```
          DS    0D  
```
