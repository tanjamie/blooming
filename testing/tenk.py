'''
By Tan Jamie (tanjamie@u.nus.edu)
- Nov 3, 2022
'''


# python -m venv .
# .\Scripts\activate
# python.exe -m pip install --upgrade pip
# python -m pip install -r requirements.txt
# python tenk.py


import os
import json
import requests
from sec_api import QueryApi
# documentation of sec_api package: https://pypi.org/project/sec-api/


# get api key and initialize QueryApi
def initialize_api(relpath):
    """
    Summary: Save API key in txt file
    Args: relpath (str): relative path to API key txt file
    Returns: (str, queryApi obj): api as string type, authenticated queryApi object
    """
    key = open(relpath, "r").readline()
    QA = QueryApi(api_key = key)
    return key, QA


def format_query(ticker, start, end):
    """
    Summary: Create & formatted query for queryApi object
    Args:
        ticker (str): index symbol
        start (str): filter files after start date in format YYYY-MM-DD
        end (str): filter file before end date in format YYYY-MM-DD
    Returns: (str): formatted query in string
    """
    query_str = "ticker:" + str(ticker) + " AND filedAt:{" + start + " TO " + end + "} AND formType:\"10-K\""
    query = {"query": {"query_string": {"query": query_str}}, "from": "0", "size": "10", "sort": [{"filedAt": {"order": "desc"}}]}
    return query


def get_filings(queryApi, query):
    """
    Summary: Obtain infromation about filings from API, save prettified response as returns.txt in output folder
    Args: query (str): query that is formatted so QueryApi understands demand
    Return: (str): raw response containing information of all filings that meet requirement
    """
    filings = queryApi.get_filings(query)
    prettify_json = json.dumps(filings, indent = 2, default = str)
    # save sample output from API
    if not os.path.isdir("output"):
        print("creating output folder...")
        os.mkdir("output")
    print("output folder already exists...")
    text_file = open("output/returns.txt", "w")
    text_file.write(prettify_json)
    text_file.close()   
    return filings


def download_10k(apikey, filings):
    """
    Summary: Download filings using API get request in output folder
    Args: filings (str): raw returns of info about the filings that pass filters
    # documentation: https://stackoverflow.com/questions/34503412/download-and-save-pdf-file-with-python-requests-module
    """
    for file in filings["filings"]:
        # parse info
        cik = file["cik"]
        accessionNo = file["accessionNo"].replace("-", "")
        for document in file["documentFormatFiles"]:
            # filter for 10k
            if document["type"] == "10-K/A" or document["type"] == "10-K":
                # get request from api
                filename = document["documentUrl"].split("/")[-1]
                link = "https://www.sec.gov/Archives/edgar/data/" + cik + "/" + accessionNo + "/" + filename
                req = "https://api.sec-api.io/filing-reader?" +"token={}&".format(apikey) + "type=pdf&" + "url={}".format(link)
                response = requests.get(req)
                # save response as pdf
                if not os.path.isdir("output"):
                    print("creating output folder...")
                    os.mkdir("output")
                print("output folder already exists...")
                with open("output/{}.pdf".format(filename.split(".")[0]), "wb") as f:
                    f.write(response.content)   


def Main():
    apikey, queryApi = initialize_api("apikey.txt")
    query = format_query("TSLA", "2020-01-01", "2020-12-31") # TSLA, PFE, EBAY, UAL
    filings = get_filings(queryApi, query)
    download_10k(apikey, filings)

Main()
