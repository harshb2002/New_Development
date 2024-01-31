from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')
# print(soup)

data = soup.find_all('div',{'class': '_2kHMtA'})
# print(data)

phn_name = []
price = []
reviews = []
links =[]
start_link="https://www.flipkart.com"

for items in data:
    rest_link = items.find('a')['href']
    name = items.find('div',attrs={'class':'_4rR01T'})
    price = items.find('div',attrs={'class':'_30jeq3 _1_WHN1'}).text.strip()
    phn_name.append(name.text.strip())
    links.append(start_link+rest_link)

dataframe = {'Phone_Names':phn_name, 'Price':price, 'Links':links }
Final_dataframe = pd.DataFrame(dataframe)
print(Final_dataframe)

Final_dataframe.to_csv('flipkart.csv', index=False)
print(f"Data added successfully CSV file")
