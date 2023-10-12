from unittest import result
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import numpy as np

##tarticle içindeki tek h1

# website = 'https://subslikescript.com/movie/Titanic-120338'
# result = requests.get(website)
# content = result.text
# soup = BeautifulSoup(content, 'html.parser')
# #print(soup.prettify())
# box = soup.find('article', class_= "main-article")
# title = box.find('h1').get_text()
# print(title)

##entry divindeki partial_entry clasına sahip olan p'yi yazdırmak.

# website = 'https://www.tripadvisor.com/Restaurant_Review-g293974-d806407-Reviews-Haci_Abdullah_Lokantasi-Istanbul.html'
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# result = requests.get(url = website, headers=headers)
# content = result.text
# soup = BeautifulSoup(content, 'html.parser')
# # # # #print(soup.prettify())
# box = soup.find('div', class_ = "entry")
# comment = box.find('p', class_ ="partial_entry").get_text()
# print(comment)

##entry classındaki TÜM divlerin içindeki partial classındaki p'ler.

# website = 'https://www.tripadvisor.com/Restaurant_Review-g293974-d806407-Reviews-Haci_Abdullah_Lokantasi-Istanbul.html'
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# result = requests.get(url = website, headers=headers)
# content = result.text
# soup = BeautifulSoup(content, 'html.parser')
# divs = soup.findAll('div',{'class':'entry'})    
# comments = []

# for p in divs: 
#    comment = p.find('p',{'class':"partial_entry"})
#    comment = comment.text[0:]
#    #comment = comment.replace(',','')
#    comments.append(comment)
# print(comments)

##REWIEV CLASSINDAKI DIV - > ICINDEKI TUM partiel entry classındaki p nin içindeki tüm texxtler. bunbu SCV kutuphanesi ile csv dondurme.
# website = 'https://www.tripadvisor.com/Restaurant_Review-g293974-d806407-Reviews-Haci_Abdullah_Lokantasi-Istanbul.html'
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# result = requests.get(url = website, headers=headers)
# content = result.text
# soup = BeautifulSoup(content, 'html.parser')
# #divs = soup.find('div',{'class':'entry'})   
# divs = soup.find('div',attrs = {'id':'REVIEWS'})   
# comments = []

# for row in divs.findAll('p',{'class':"partial_entry"}):
#    comment = {}
#    comment['yorumlar'] = row.text
#    comments.append(comment)
#    print(comment)


# filename = 'deneme_comments6.csv'
# with open(filename, 'w', newline='') as f:
#      w = csv.DictWriter(f,['yorumlar'])
#      w.writeheader()
#      for comment in comments:
#          w.writerow(comment)


## Tek Satır Row
# website = 'https://www.tripadvisor.com/Restaurant_Review-g293974-d806407-Reviews-Haci_Abdullah_Lokantasi-Istanbul.html'
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# result = requests.get(url = website, headers=headers)
# content = result.text
# soup = BeautifulSoup(content, 'html.parser')
# #divs = soup.find('div',{'class':'entry'})   
# divs = soup.find('div',attrs = {'id':'REVIEWS'})   
# comments = []

# for row in divs.findAll('p',{'class':"partial_entry"}):
#    comment = {}
#    comment['yorumlar'] = row.text
#    comments.append(comment)

# filename = 'deneme_comments3.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['yorumlar'])
#     w.writeheader()
#     for comment in comments:
#         w.writerow(comment)

# website = 'https://www.tripadvisor.com/Restaurant_Review-g293974-d806407-Reviews-Haci_Abdullah_Lokantasi-Istanbul.html'
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# result = requests.get(url = website, headers=headers)
# content = result.text
# soup = BeautifulSoup(content, 'html.parser')
# #divs = soup.find('div',{'class':'entry'})   
# divs = soup.find('div',attrs = {'id':'REVIEWS'})   
# comments = []

# for row in divs.findAll('p',{'class':"partial_entry"}):
#    comment = {}
#    comment['yorumlar'] = row.text
#    comments.append(comment)
#   # print(comment)
# a = pd.Series(comments)
# print(a)


website = 'https://www.tripadvisor.com/Restaurant_Review-g293974-d806407-Reviews-Haci_Abdullah_Lokantasi-Istanbul.html'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
result = requests.get(url = website, headers=headers)
content = result.text
soup = BeautifulSoup(content, 'html.parser')
#divs = soup.find('div',{'class':'entry'})   
divs = soup.find('div',attrs = {'id':'REVIEWS'})   
comments = []

for row in divs.findAll('p',{'class':"partial_entry"}):
   comment = {}
   comment['yorumlar'] = row.text
   comments.append(comment)
  # print(comment)

df = pd.DataFrame({'Yorumlar' : comments})
df.to_csv('yorumlar.csv', index=False,encoding='utf-8')