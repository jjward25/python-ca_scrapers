from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import csv
from datetime import date
import pandas as pd

# Modules
from sites.nationalreview import national_review_df
from sites.politico import politico_df
from sites.cfr import cfr_df

combined_df = pd.DataFrame()
combined_df = combined_df.append(national_review_df)
combined_df = combined_df.append(politico_df)
combined_df = combined_df.append(cfr_df)

#print(combined_df)

oped_df = combined_df
print(oped_df)
oped_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\python-ca-scrapers\Current Events\head_oped_pkg\oped_data.csv')