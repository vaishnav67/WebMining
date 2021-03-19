import requests
from bs4 import BeautifulSoup
import csv
URL = "https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&p%5B%5D=facets.brand%255B%255D%3DDell&pageUID=1591709957426&otracker=clp_metro_expandable_2_42.metroExpandable.METRO_EXPANDABLE_Dell_laptops-store_ATZ0N15AZUUY_wp15&fm=neo%2Fmerchandising&iid=M_ca65ed95-c9d2-43c5-a26b-7f11392b09c7_42.ATZ0N15AZUUY&ppt=clp&ppn=laptops-store&ssid=z75u6hvmmoq7qlts1614177778325"
r = requests.get(URL)
soup = BeautifulSoup(r.content,"html5lib")
products=[]
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
for row in soup.find_all('div',attrs={'class':'_2kHMtA'}):
    product={}
    product['Name']=row.find('div',attrs={'class':'_4rR01T'}).string
    product['Discount Price']=row.find('div',attrs={'class':'_30jeq3 _1_WHN1'}).string
    try:
        product['Real Price']=row.find('div',attrs={'class':'_3I9_wc _27UcVY'}).text
    except:
        product['Real Price']=product['Discount Price']
        product['Discount Price']="NIL"
    product['Image']=row.img['src']
    products.append(product)
filename = 'amazonscrap.csv'
with open(filename, 'w', newline='',encoding="utf-8") as f: 
    w = csv.DictWriter(f,['Name','Discount Price','Real Price','Image']) 
    w.writeheader() 
    for product in products: 
        print(product)
        w.writerow(product) 
