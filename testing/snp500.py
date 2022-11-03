'''
By Tan Jamie (tanjamie@u.nus.edu)
- Oct 31, 2022
'''


# python -m venv .
# .\Scripts\activate
# python.exe -m pip install --upgrade pip
# python -m pip install -r requirements.txt
# python snp500.py


import os
import bs4
import requests
import pandas as pd


def extract_source(url):
    """
    Summary: Get contents from url
    Args: url (str): url to item we want to obtain
    Returns: request object: response obtained from get request with url provided
    """
    agent = {"User-Agent":"Mozilla/5.0"}
    source = requests.get(url, headers = agent).text
    return source


def extract_data(source, tag):
    """
    Summary: Parse response obtained
    Args:
        source (response object): response from get request
        tag (str): tag attached to response html that we are interested in
    Returns: str: string of html that is related to tag specified
    """
    soup = bs4.BeautifulSoup(source, 'lxml')
    # print(soup.prettify)
    return soup.find_all(tag)


def main():
    url = "https://www.slickcharts.com/sp500"
    table = extract_data(extract_source(url), "table")[0]
    rows = table.find_all('tr')[1:]
    data = {'Company': [], 'Symbol': [], 'Weight': []}
    for row in rows:
        cols = row.find_all('td')
        company = cols[1].get_text(); data["Company"].append(company)
        symbol = cols[2].get_text(); data["Symbol"].append(symbol)
        weight = cols[3].get_text(); data["Weight"].append(weight)
    if not os.path.isdir("output"):
        print("creating output folder...")
        os.mkdir("output")
    print("output folder exists...")
    pd.DataFrame.from_dict(data).to_csv("output/snp500.csv")

main()
