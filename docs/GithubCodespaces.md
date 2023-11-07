# Github CodeSpaces Setup


One concise document to setup vscode in a github codespace.

##  github codespaces setup

These are notes on how to setup a vs code installation using github codespaces for use with 
jupyter/inotebooks

### workflow

1. start a githubcodespace via a git repo
2. using settings icon in lower left, select themes
3. in terminal create the venv
    
    This varies for notebooks and webapps.  In this case I'll show how to do it for the notebooks
    1. `cd notebooks`
    2. `mkdir nbenv`
    3. `cd nbenv` 
    5.  `python -m venv nbenv`
    6.  `source nbenv/bin/activate`
        - at this point you should notice your prompt has a prefix of `(nbenv)` meaning the venv is operational
    7.  `pip install --upgrade pip`
    8.  `python -m pip install numpy`
        - just to test that you can install `numpy`
    9. `cd ..`
        - For now, there is just one requirements.txt and its above this dir
    9. `python install -r requirements.txt`
        - this installs the common identified modules for the notebooks in this venv
    7. add `.gitignore` for `nbenv` and for `.env`
        - this is so that git does not try to CM your modules nor your api keys in `.env`
        - `echo nbenv/nbenv/ >> .gitignore`
        - `echo .env >> .gitignore`
4. Install jupyter notebooks in vscode
    1. click extensions in left sidebar
    2. type jupyter<CR>
    3. select jupyter from microsoft
5. Setup python inpreter for the VS Code workspace
    1. cmd shift p to bring up command window
    2. type `Python: Select Interpreter`
    3. click the use existing or browse to existing
    3. Use browse capability to browse to `notebooks/nbenv/bin/python3`
6. In the file menu, create a new notebook
    1. click explorer on left sidebar
    2. click notebooks in the file explorer
        - We want to create the notebook in this folder
    3. click the add file button at the top of the explorer to add a new file
        - name it `Testy.ipynb`
        - click the new file and it should bring up a blank python jupyter notebook
6. Test notebook setup
    1. Use this code for the first cell

        ```
        from pprint import pprint
        foo={"id": 1,"name": "Leanne Graham","username": "Bret","email": "Sincere@april.biz","address": {  "street": "Kulas Light",  "suite": "Apt. 556",  "city": "Gwenborough",  "zipcode": "92998-3874",  "geo": {    "lat": "-37.3159",    "lng": "81.1496"  }},"phone": "1-770-736-8031 x56442","website": "hildegard.org","company": {  "name": "Romaguera-Crona",  "catchPhrase": "Multi-layered client-server neural-net",  "bs": "harness real-time e-markets"}}
        pprint(foo)

        import pandas as pd
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
        print(df)
        ```
7. On right hand side, it will say in the menu bar, `Select Kernel`
    1. click the `Select Kernel` button
    2. click `nbenv` which is recommended



## Extensions to install

* Google Cloud Code
* Python
* jupyter
* rainbow CSV


## vs code multiple tabs

```
Within your settings, under workbench, set:

"workbench.editor.enablePreview": false,
"workbench.editor.enablePreviewFromQuickOpen": false
This will allow you to open the files with a single click, as opposed to double-clicking. It may seem minute, but it was incredibly annoying to have to double-click every single file.
```


