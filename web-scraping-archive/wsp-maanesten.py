import re
import time
import smtplib
import requests
import keys
from datetime import datetime 
from bs4 import BeautifulSoup

def stock_check(url):
    """Checks url for 'sold out!' substring in buy-now-bar-con"""
    soup = BeautifulSoup(url.content, "html.parser")
    section = soup.find('div', {'class' : 'woocommerce-variation-price'})
    status = re.findall(r"Out of stock", str(section))
    return status # returns "Out of stock" from soup string.

def send_email(address, receiver, password, message):
    """Send an e-mail to yourself!"""
    server = smtplib.SMTP("smtp.gmail.com", 587) #e-mail server
    server.ehlo()
    server.starttls()
    server.login(address,password) #login
    message = str(message) #message to email yourself
    server.sendmail(address, receiver, message) #send the email through dedicated server
    return

def stock_check_listener(url, address, receiver, password, run_hours):
    """Periodically checks stock information."""
    listen = True # listen boolean
    start = datetime.now() # start time
    while(listen): #while listen = True, run loop
        if "Out of stock" in stock_check(url): #check page
            now = datetime.now()
            print(str(now) + ": Not in stock.")
        else:
            message = str(now) + ": NOW IN STOCK!"
            print(message)
            send_email(address, password, message)
            listen = False

        duration = (now - start)
        seconds = duration.total_seconds()
        hours = int(seconds/3600)
        if hours >= run_hours: #check run time
            print("Finished.")
            listen = False

        time.sleep(30*60) #Wait N minutes to check again.    
    return

if __name__=="__main__":

    #Set url and userAgent header for javascript issues.
    page = "https://maanesten.com/product/florina-tan-hairclaw/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html'}

    #URL request.
    url = requests.get(url=page,
                       headers=headers)

    #Run listener to stream stock checks.
    address = keys.sender #your email
    receiver = keys.receiver
    password = keys.password #your email password
    stock_check_listener(url = url,
                         address = address,
                         receiver = receiver,
                         password = password,
                         run_hours = 1000) 