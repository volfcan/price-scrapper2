from replit import db
import time, requests, os, smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def addToDb():
  link = input("Link: ")
  price = float(input("Price: "))
  db[time.time()] = {"Link": link, "price": None, "level": price}

keys = db.keys()
# for i in keys:
  # print(f"{keys}: {db[i]}")

for key in keys:
  url = db[key]["link"]
  price = db[key]["price"]
  level = db[key]["level"]
  response = requests.get(url)
  html = response.text
  
  soup = BeautifulSoup(html, "html.parser")
  itemPrice = soup.find_all("span", {"class": "price"})
  thisPrice = float(itemPrice[0].text[1:])
  print(itemPrice)

#   # if thisPrice != price:
#     # db[key]["price"] = thisPrice
#   # if thisPrice <= level:
#     # print("Cheaper!")

addToDb()