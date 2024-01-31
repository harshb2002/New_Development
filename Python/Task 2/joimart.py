from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.jiomart.com/c/electronics/mobiles-tablets/smartphones/777"

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')
# print(soup)

data = soup.find_all('div',{'class': 'plp-card-container'})
# print(data)

phn_name = []
price = []
discount = []

for items in data:
    name = items.find('div',attrs={'class':'plp-card-details-name line-clamp jm-body-xs jm-fc-primary-grey-80'})
    phn_name.append(name.text.strip())
    price = items.find('span',attrs={'class':'jm-heading-xxs jm-mb-xxs'}).text.strip()
    discount = items.find('span',attrs={'class':'jm-badge'}).text.strip()

dataframe = {'Phone_Names':phn_name, 'Price':price, 'Discount':discount}
Final_dataframe = pd.DataFrame(dataframe)
print(Final_dataframe)

Final_dataframe.to_csv('joimart.csv', index=False)
print("Data added successfully CSV file")