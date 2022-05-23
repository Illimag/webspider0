# encoding=utf8

from bs4 import BeautifulSoup as soup
import requests
import time


print("Starting")
time.sleep(1)

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)

print("Test Complete")