
import csv
import bs4 as bs
from urllib.request import Request, urlopen
from string import ascii_uppercase
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

csv_file = open('review.csv', 'w', newline='',encoding="utf-8-sig")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'date', 'review'])

# for letter in ascii_uppercase:
url = Request('https://www.foodpanda.com.tw/restaurant/e0jn/starbucks-xing-ba-ke-xin-zhuang-shuang-feng-men-shi'+'#restaurant-info', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(url).read()
soup = bs.BeautifulSoup(webpage, 'html.parser')

for div in soup.find_all('div',{'class': 'review-component hreview'}):
    name = div.find('span',{'class':'fn'}).text
    date = div.find('abbr',{'class':'review-date dtreviewed'})['title']
    review = div.find('div',{'class':'description'}).text.strip()
    print(name)
    print(date)
    print(review)
    csv_writer.writerow([name]+[date]+[review])
csv_file.close()