# testing :construction:

> Testing leads to failure. And failure leads to understanding.

This section is dedicated for preliminary testing of the different functionalities that are planned for this project. Note that files here are designed for execution from this folder only. The specific test subjects are as listed and explained in the table below. To run the code files, execute the following code in your cmd:
* `cd` into the testing folder
* `python -m venv .` 
* `.\Scripts\activate`
* `python.exe -m pip install --upgrade pip`
* `python -m pip install -r requirements.txt`
* `python {FILENAME}.py`, replace FILENAME respectively

|Filename|Task|Package|
|----|-----|-------|
|snp500.py|Obtain list of S&P500 components|os, bs4, requests, pandas|
|tenk.py|Scrape 10-K forms for specified companies|os, json, requests, sec_api|
