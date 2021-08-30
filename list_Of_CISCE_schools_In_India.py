from os import remove

import bs4
import pandas as pd
from googlesearch import search
import csv
import requests

from bs4 import BeautifulSoup

url = 'https://www.cisce.org/locate-search.aspx?country=0&state=0&dist=0&city=0&location=&schooltype=&cve=&isc=&icse=&schoolclassi=&school=&search=locate'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}


datas = []

r = requests.get(url , headers=header)
htmlContent = r.content

# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

items = soup.findAll('table' )


for y in items:
    child = y.find_all('tr')
    # print(child)
    for z in child[1::]:
        # print(z)
        print("\n")
        contentS = z.findChildren()
        contactN = z.findChildren()[7].text
        n = ''.join(contactN.split())
        contactNumber = list(contactN.split(" "))
        ActualNumber = str(contactNumber[1])
        ActualNumber = ActualNumber.strip('\n')
        ActualNumber = ActualNumber.strip('\t')
        ActualNumber = ActualNumber.replace('"','')
        schoolCode = z.findChildren()[1].text
        schooName = str(z.find('a')['param'])
        schooName = schooName.replace(',', ' ')
        schooName = schooName.replace('   ', '')
        

        datas.append([schoolCode, schooName, ActualNumber[:-3]])



with open('CISCE.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    headers = ['schoolCode','schoolName', 'contactNumber']
    writer.writerow(headers)
    for data in datas:
        writer.writerow(data)

print("Stopped")

