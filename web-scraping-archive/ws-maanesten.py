import requests
import re
import numpy as np
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html'}
gen_url = 'https://maanesten.com/product-category/accessories-2/hair-claws/?metaltype[]=accessories&ajaxcall=1&page='
pNames = []
for n in np.arange(1, 7, 1):
    #print(gen_url+str(n))
    r = requests.get(gen_url+str(n), headers = header)
    c = r.content 
    soup = BeautifulSoup(c, 'html.parser')
    uls = soup.find('ul', {'class' : 'products'})
    ils = uls.find_all('li')
    for il in ils: 
        pNames.append(il.find('h3').text)

for n in np.arange(0, len(pNames)):
    pNames[n] =  pNames[n].replace(' ', '-')
# print(pNames)

prod_url = 'https://maanesten.com/product/'
for n in np.arange(0, len(pNames)):
    prod_r = requests.get(prod_url+pNames[n], headers = header)
    prod_c = prod_r.content 
    prod_s = BeautifulSoup(prod_c, 'html.parser')
    section = prod_s.find('div', {'class' : 'woocommerce-variation-price'})
    status = re.findall(r"Out of stock", str(section))
    amt = prod_s.find('span', {'class' : 'amount'}).text
    if not status:
        print(f'{pNames[n]} : IN STOCK')
    else: 
        print(f'{pNames[n]} : Out of stock')
