
import csv

import bs4 as bs
from urllib.request import Request, urlopen

from string import ascii_uppercase

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# import selenium_test as st

# csv_file = open('brand.csv', 'w', newline='',encoding="utf-8")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Brand Name', 'Brand Url'])

# for letter in ascii_uppercase:
url = Request('https://www.foodpanda.com.tw/en/restaurants/lat/25.0393093/lng/121.4262066/city/Taishan%20District/address/No.%252010%252C%2520Alley%252034%252C%2520Lane%2520145%252C%2520Section%25203%252C%2520Mingzhi%2520Road%252C%2520Taishan%2520District%252C%2520New%2520Taipei%2520City%252C%2520Taiwan%2520243/Alley%252034%252C%2520Lane%2520145%252C%2520Section%25203%252C%2520Mingzhi%2520Road/10?postcode=243', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(url).read()
soup = bs.BeautifulSoup(webpage, 'html.parser')

for li in soup.find_all('li'):
    name = li.find('span',{'class':'name fn'})
    for a in li.find_all('a',href=True):
        if a.text and name is not None:
            print(name.text,'\n',a['href'])
        


    # for a in soup.find_all("div", {"class": "col-xl-3 offset-lg-1 offset-xl-0 col-lg-4 col-6"}):
    #     brand_url = a.find('a')['href']
    #     brand_text = a.find("a",{"class":"brand-link"}).text
    #     print(brand_text,brand_url)
    #     print()
    #     csv_writer.writerow([brand_text]+[brand_url])

# csv_file.close()