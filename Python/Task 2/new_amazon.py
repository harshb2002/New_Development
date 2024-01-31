from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.com/s?k=samsung+a15+5g&crid=P4WGEISKDH8T&sprefix=samsung+a15%2Caps%2C539&ref=nb_sb_ss_ts-doa-p_4_11"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US',
    'Accept-Encoding': 'en-US, en;q=0.5'
}

webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, 'html.parser')

links = soup.find_all('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


if links:
    link = links[7].get('href')
    product_list = "https://amazon.com/" + link

    new_webpage = requests.get(product_list, headers=HEADERS)

    new_soup = BeautifulSoup(new_webpage.content, 'html.parser')

    # Check if the element exists before accessing its text attribute
    product_title = new_soup.find("span", attrs={"id": 'productTitle'})
    if product_title:
        print("Product title is : "+product_title.text.strip())
    else:
        print("Product title not found.")

    price_element = new_soup.find("span", attrs={"class": 'a-offscreen'})
    if price_element:
        print("Price of this Product is : "+price_element.text.strip())
    else:
        print("Price not found.")

    rating_element = new_soup.find("span", attrs={"id": 'acrCustomerReviewText'})
    if rating_element:
        print("Rating of this Product is : "+rating_element.text.strip())
    else:
        print("Rating title not found.")
else:
    print("No links found.")

    


