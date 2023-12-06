When writing code, obey these rules:

* NAME corresponds to a LABEL and is always in column 1.
    - The NAME is at most 8 characters long.
    - The NAME begins with characters A-Z, a-z, $, # or @. 
* OPERATION corresponds to an instruction (mnemonic) and starts in column 10.
* OPERANDS corresponds to instruction argumennts or parameters and starts in column 15.
    - Multiple operands are separated by a comma `,`.
    - Space ` ` characters are not permitted between OPERANDS.
* COMMENT corresponds to non functional text and has two possible starting locations.  
    - If the entire line is a comment, then the comment marker `*` starts in column 1.
    - If the comment is used at the end of a line of code, it starts at column 32.
* Column 72 is used to identify a continuation of the current line to the next.
    - Only use a continuation character when an instruction line spans more than 65 columns.
    - In this case, use a `x` in column 72 on the first line.
    - On the second continued line, code starts at column 16.

All code should be output in markdown or preformatted text blocks like so:

```
code here
```

Unless explictly told to do so, do not include any commentary.

When specifiying registers be explicit.  For example when referring to register one, use R1 rather than 1.

