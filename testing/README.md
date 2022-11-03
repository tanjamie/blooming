# testing

### Purpose?
This section is dedicated for preliminary testing of the different functionalities that are planned for this project. Note that files here are designed for execution from this folder only. 

### Test Subject
|Filename|Task|Package|
|----|-----|-------|
|snp500.py|Obtain list of S&P500 components|os, bs4, requests, pandas|
|tenk.py|Scrape 10-K forms for specified companies|os, json requests sec_api|

### To Run Code
To run the code files, run the following code in your cmd:
* `cd` into the testing folder
* `python -m venv .` 
* `.\Scripts\activate`
* `python.exe -m pip install --upgrade pip`
* `python -m pip install -r requirements.txt`
* `python {FILENAME}.py`
