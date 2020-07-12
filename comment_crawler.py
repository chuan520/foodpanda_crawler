
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
url = Request('https://www.foodpanda.com.tw/restaurant/e0jn/starbucks-xing-ba-ke-xin-zhuang-shuang-feng-men-shi'+'#restaurant-info', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(url).read()
soup = bs.BeautifulSoup(webpage, 'html.parser')

for div in soup.find_all('div',{'class': 'review-component hreview'}):
    name = div.find('span',{'class':'fn'}).text
    date = div.find('abbr',{'class':'review-date dtreviewed'})
    review = div.find('div',{'class':'description'}).text
    print(name)
    print(date['title'])
    print(review.strip())
    # name = li.find('span',{'class':'name fn'})
    # for a in li.find_all('a',href=True):
    #     if a.text and name is not None:
    #         print(name.text,'\n',a['href'])
        


    # for a in soup.find_all("div", {"class": "col-xl-3 offset-lg-1 offset-xl-0 col-lg-4 col-6"}):
    #     brand_url = a.find('a')['href']
    #     brand_text = a.find("a",{"class":"brand-link"}).text
    #     print(brand_text,brand_url)
    #     print()
    #     csv_writer.writerow([brand_text]+[brand_url])

# csv_file.close()