import requests
from bs4 import BeautifulSoup
import csv

def fetch_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
        return None

def pagination_data(soup, outer_div_class, inner_div_class, header_tag,list1,pages):
    last_page_element = soup.find('li', class_='page-item disabled')
    for i in range(2,pages+1):
        next_page_url = f"https://apps.odoo.com/apps/modules/browse/page/{i}?order=Relevance"
        # print(f"Scraping data from page {i}")
        next_page_content = fetch_data(next_page_url)

        if next_page_content:
            parse_data(next_page_content, outer_div_class, inner_div_class, header_tag,list1)

def parse_data(html_content, outer_div_class, inner_div_class, header_tag,list1):
    soup = BeautifulSoup(html_content, 'html.parser')

    outer_divs = soup.find_all('div', class_=outer_div_class)

    if outer_divs:

        for outer_div in outer_divs:
            inner_div = outer_div.find('div', class_=inner_div_class)

            if inner_div:
                header = inner_div.find(header_tag)

                if header:
                    text_data = header.get_text(strip=True).split('|')[0]
                    print(text_data)
                    list1.append(text_data)
                else:
                    print(f"No {header_tag} tag found within inner div.")
    else:
        print(f"No outer divs found with class '{outer_div_class}'.")


url = 'https://apps.odoo.com/apps/modules/browse?order=Relevance'

outer_div_class_to_extract = 'loempia_app_card'
inner_div_class_to_extract = 'loempia_app_entry_bottom'
header_tag_to_extract = 'h5'

outer_div_class_cname="loempia_app_entry_bottom"
inner_div_class_cname="loempia_panel_author"
header_tag_cname='b'

outer_div_class_price = 'loempia_app_entry_bottom'
inner_div_class_price = 'loempia_panel_price'
header_tag_price = 'b'

name_list = []
cname_list=[]
price_list =[]

pages=int(input("how many pages you want to scrab:"))
html_content = fetch_data(url)
if html_content:
    parse_data(html_content, outer_div_class_to_extract, inner_div_class_to_extract, header_tag_to_extract,name_list)
    pagination_data(BeautifulSoup(html_content, 'html.parser'), outer_div_class_to_extract, inner_div_class_to_extract, header_tag_to_extract,name_list,pages)

    parse_data(html_content, outer_div_class_cname, inner_div_class_cname, header_tag_cname,cname_list)
    pagination_data(BeautifulSoup(html_content, 'html.parser'), outer_div_class_to_extract, inner_div_class_to_extract, header_tag_to_extract,name_list,pages)

    parse_data(html_content, outer_div_class_price, inner_div_class_price, header_tag_price,price_list)
    pagination_data(BeautifulSoup(html_content, 'html.parser'), outer_div_class_price, inner_div_class_price, header_tag_price,price_list,pages)
    
data=zip(name_list,cname_list,price_list)
with open("data.csv", "a",newline="") as file:
    writer = csv.writer(file)
    for l in data:
        writer.writerow(l)

print(f"Data has been successfully saved to data.csv file.")