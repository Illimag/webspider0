# encoding=utf8

from bs4 import BeautifulSoup as soup
import requests
import time

print("Starting")
time.sleep(1)

URL = "https://www.softwaretestinghelp.com/default-router-ip-address-list/"
page = requests.get(URL)

print(page.text)
print("Complete")