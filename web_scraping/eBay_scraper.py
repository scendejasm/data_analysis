import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import pandas as pd
import numpy as np

# Declaring the headers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'}

# declaring the list of empty variables, so that we can append the data overall

acc_name = []
lap_state = []
lap_price = []

# creting a n array of values and passing it in the url for dynamic webpages
pages = np.arange(1,50,1)

# the whole core of the script
for page in pages:
    page = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=laptop&_sacat=0&_pgn="+str(page)+"&rt=nc")
    soup = BeautifulSoup(page.text, 'html.parser')
    acc_data = soup.find_all('div', {'class': 's-item__info clearfix'})
    sleep(randint(2,6))
    print(acc_data[0])
    for store in acc_data:
        name = store.find('div', {'class' : 's-item__title'}).text
        acc_name.append(name)

        try:
            state = store.find('span', {'class' : 'SECONDARY_INFO'}).text
        except AttributeError:
            state = np.nan
        lap_state.append(state)
        print(state)

        price = store.find('span', {'class' : 's-item__price'}).text
        lap_price.append(price)

data = pd.DataFrame({"Laptop Detail": acc_name, "Laptop State": lap_state, "Laptop Price": lap_price})

print(data.head())

data.to_csv('ebay_laptops.csv', index = None)