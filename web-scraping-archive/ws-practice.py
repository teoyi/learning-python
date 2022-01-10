import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content # beautiful soup will give us the contents listed here 

soup = BeautifulSoup(c, "html.parser") # need to pass html.parser if not it wont work properly
#print(soup.prettify()) #this will print it out in a html format 
# viewing this online through inspect will give a clearer idea by highlighting the resepective elements 
all = soup.find_all("div",{"class":"cities"})
#print(all[0]) # indexing is possible for this 
# if we are looking for specific headers or paragraph 
#print(all[0].find_all("h2")[0].text) 

for item in all: 
    print(item.find_all("p")[0].text)

