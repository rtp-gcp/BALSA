from flask import Blueprint, render_template,  request, session, redirect, url_for, current_app

balsa = Blueprint('balsa', __name__)

## openai api request
def send_openai_request(prompt):
    """Send a request to OpenAI API."""
    system_msg = """
You are a helpful assistant who understands BAL (a subset of IBM HLASM)

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

When issuing instruction commands, only consider the instructions / op code in this table:


| Instruction / Op Code | Description                        | 
| :-------| :------------------------------------------------|
| A       | Add fullword                                     |
| AH      | Add halfword                                     |
| AL      | Add unsigned fullword                            |
| ALR     | Add unsigned register                            |
| AP      | Add Packed two fields in Memory                  | 
| AR      | Add Register fullword                            | 
| BAL     | Branch and Link                                  | 
| BALR    | Branch and Link Register                         | 
| BAS     | Branch and Save                                  | 
| BASR    | Branch and Save Register                         | 
| BASSM   | Branch and Save and Set Mode                     | 
| BC      | Branch on Condition                              | 
| BCR     | Branch on Condition Register                     | 
| BCT     | Branch on Count                                  | 
| BCTR    | Branch on Count Register                         | 
| BSM     | Branch and Set Mode                              | 
| BXH     | Branch on Index Greater                          | 
| BXLE    | Branch on Index Less than or Equal               | 
| C       | Compare Fullword in register against memory      | 
| CDS     | Compare Doubleword in even/odd register pair against memory and Swap               | 
| CH      | Compare Halfword                                                                   | 
| CL      | Compare logically unsigned fullword in register against memory                     | 
| CLC     | Compare up to 256 consecutive bytes in Memory                                      | 
| CLCL    | Compare Characters Long                                                            | 
| CLI     | Compare Logical Immediate                                                          | 
| CLM     | Compare Selected Bytes in Memory using mask                                        | 
| CLR     | Compare Logical Registers                                                          | 
| CP      | Compare Packed two fields in Memory                                                | 
| CR      | Compare Fullword in Registers                                                      | 
| CS      | Compare Fullword in register against memory and Swap                               | 
| CVB     | Convert Packed Decimal Value in Memory to signed integers in register              |
| CVD     | Convert Signed Fullword in Register to Packed Decimal in Memory                    |
| D       | Divide doubleword in in even/odd register pair by fullword value in Memory         | 
| DP      | Divide Packed Decimals two fields in Memory                                        | 
| DR      | Divide doubleword in in even/odd register pair by fullword Register                | 
| ED      | Edit - formats packed decimal field                                                | 
| EDMK    | Edit and Mark - address of first significant digit in R1                           | 
| EX      | Execute a target instruction                                                       | 
| IC      | Insert Character - into low byte of register                                       | 
| ICM     | Insert Characters under mask into Register                                         | 
| L       | Load a fullword from memory into a register                                        | 
| LA      | Load address of a storage location into a register                                 | 
| LCR     | Load signed 2's complement value in Register2 into Register1                       | 
| LH      | Load signed halfword from memory into a Register                                   | 
| LM      | Load Multiple fullword values from memory into registers                           | 
| LNR     | Load value in register R2 into register R1 with negative sign                      | 
| LPR     | Load value in register R2 into register R1 with positive sign (absolute value)     |
| LR      | Load value from register R1 into register R2                                       | 
| LTR     | Load and Test value in register R2 into register R1                                | 
| M       | Multiply register fullword in even/odd register pair by fullword in memory         |
| MH      | Multiply fullword register by halfowrd in memory in even/odd register pair         |
| MP      | Multiply Packed decimal in memory by packed decimal in memory                      | 
| MR      | Multiply fullword value in even/odd register pair by fullword value in register    |
| MVC     | Copy L bytes from memory to memory                                                 | 
| MVCIN   | Copy L bytes from memory to memory reversing order of values with second operand is last byte |   
| MVCL    | Copy or fill bytes in memory                                                                  | 
| MVI     | Store byte I2 to memory                                                                       | 
| MVN     | Copy low nibbles from memory to memory                                                        | 
| MVO     | Copy nibbles from memory to memory offset by 4 bits                                           | 
| MVZ     | Copy high nibbles from memory to memory                                                       | 
| N       | Logical AND register and full word in memory                                                  | 
| NC      | Logical AND consecutive bytes in memory with memory                                           | 
| NI      | Logical AND byte in memory with immediate                                                     | 
| NR      | Logical AND register with register                                                            | 
| O       | Logical OR register with memory                                                               | 
| OC      | Logical OR consecutive bytes in memory with memory                                            | 
| OI      | Logical OR byte in memory with immediate                                                      | 
| OR      | Logical OR register with register                                                             | 
| PACK    | Convert zoned decimal characters in memory to packed decimal numbers in memory                |
| S       | Subtract signed fullword in memory from register                                              | 
| SH      | Subtract signed halfword in memory from register                                              | 
| SL      | Subtract unsigned fullword in memory from register                                            | 
| SLA     | Shift left fullword register arithmetically by specified number of bits                       |
| SLDA    | Shift left signed 64-bit value in even/odd register pair arithmetically by specified number of bits |
| SLDL    | Shift left signed 64-bit value in even/odd register pair logically specified number of bits         |
| SLL     | Shift left fullword register logically by specified number of bits                                  | 
| SLR     | Subtract unsigned fullword in register by register                                                  |   
| SP      | Subtract packed decimals in memory                                                                  | 
| SR      | Subtract signed values in register by register                                                      | 
| SRA     | Shift right register arithmetically by specified number of bits                                        | 
| SRDA    | Shift right signed 64-bit value from even/odd register pair arithmetically by specified number of bits |
| SRDL    | Shift right signed 64-bit value from even/odd register pair logically by specified number of bits      |
| SRL     | Shift right register by specified number of bits                                                       |
| SRP     | Shift packed number in memory by the 6-bit signed number using the value I3 as a rounding value and with a negative value shifting right. |
| ST      | Store fullword in register to memory                                                                                                      | 
| STC     | Store lowest byte in register to memory                                                                                                   | 
| STCM    | Store selected bytes in register to memory using mask                                                                                     | 
| STH     | Store halfword in register to memory                                                                                                      | 
| STM     | Store values of several registers to fullwords in memory                                                                                  | 
| SVC     | Supervisor call - invoke Operating System service number                                                                                  | 
| TM      | Test bits of byte in memory using mask                                                                                                    | 
| TR      | Translate memory area at address using table in memory                                                                                    | 
| TRT     | Examine table in memory by using memory bytes as an index with the first non-zero value found is inserted into the low byte of R2         |
| UNPK    | Convert packed decimal in memory to zoned decimal in memory                                                                               | 
| X       | Logical XOR register with memory                                                                                                          | 
| XC      | Logical XOR up to 256 bytes in memory with bytes in memory                                                                                | 
| XI      | Logical XOR byte in memory with immediate                                                                                                 | 
| XR      | Logical XOR register with register                                                                                                        | 
| ZAP     | Set packed decimal number in memory to 0 and then add from memory                                                                         |
"""

    response = current_app.openai_client.chat.completions.create(
        model="ft:gpt-3.5-turbo-1106:personal::8SXoaFOx",
        messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@balsa.before_request
def require_login():
    if "email" not in session:
            return redirect(url_for("auth.login"))

@balsa.route('/balsa/train-data', methods=['POST'])
def handle_train_data():
    """Handle submissions for training data."""
    prompt = request.form['prompt']
    response = request.form['response']

    # Use 'prompt' as the document ID to overwrite the response
    doc_ref = current_app.firestore_client.collection('train_data').document(prompt)
    doc_ref.set({
        'prompt': prompt,
        'response': response
    })

    return render_template('balsa.html', email=session["email"])


@balsa.route('/balsa/prompt', methods=['POST'])
def handle_prompt():
    """Handle form submissions from the index page."""
    action = request.form.get('action')
    prompt = request.form.get('prompt')
    response = request.form.get('response')

    if action == 'submit':
        # Prepare and send the request to OpenAI
        response = send_openai_request(prompt)

        return render_template('balsa.html', prompt=prompt, response=response, email=session["email"])

    # elif action == 'good':
    #     # Serve a blank index.html template if 'Good'
    #     return render_template('balsa.html', email=session["email"])
    # elif action == 'bad':
    #     # Serve the train.html template for further editing if 'Bad'
    #     return render_template('train.html', prompt=prompt, response=response)
    


@balsa.route('/balsa', methods=['GET'])
def balsa_index():
    """Route for the service page."""
    print("== hit balsa route === ")

    return render_template('balsa.html', email=session["email"])




