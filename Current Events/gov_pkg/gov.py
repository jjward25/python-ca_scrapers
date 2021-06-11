from bs4 import BeautifulSoup  ## BeautifulSoup is a web parsing package to help pull specific HTML components
import urllib.request  ## to get a access to a URL and its content
import csv
from datetime import date
import pandas as pd

# Modules
from other.whitehouse import white_house_df
from other.supremecourt import supreme_court_df

from cabinet.state import state_dept_df
from cabinet.ed import ed_dept_df
from cabinet.treasury import treasury_dept_df
from cabinet.defense import defense_dept_df
from cabinet.justice import justice_dept_df

combined_df = pd.DataFrame()
combined_df = combined_df.append(white_house_df)
combined_df = combined_df.append(supreme_court_df)
combined_df = combined_df.append(state_dept_df)
combined_df = combined_df.append(ed_dept_df)
combined_df = combined_df.append(treasury_dept_df)
combined_df = combined_df.append(defense_dept_df)
combined_df = combined_df.append(justice_dept_df)
#print(combined_df)


gov_df = combined_df
print(gov_df)
gov_df.to_csv(r'C:\Users\Josep\OneDrive\Desktop\Coding\CA Scrapers\Current Events\gov_pkg\gov_data.csv')