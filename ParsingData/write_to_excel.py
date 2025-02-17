import requests
from bs4 import BeautifulSoup

from data_perser import collect_user_rates

import pandas as pd


user_rates = collect_user_rates(user_login='rfeldman9')
df = pd.DataFrame(user_rates)

df.to_excel('user_rates.xlsx')