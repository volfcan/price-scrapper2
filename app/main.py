import time, requests, smtplib, os
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
from tinydb import TinyDB
from flask import Flask, request, render_template
from dotenv import load_dotenv

app = Flask(__name__)


db = TinyDB('db.json')
db.truncate()
load_dotenv()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    link = request.form['link']
    discount_price = request.form.get('discount_price')
    email = request.form.get('email')
    insert(link, discount_price, email)
    return "Form submitted"


def emailMe(level, price, link, email):
    password = os.getenv('PASSWORD')
    username = os.getenv('USERNAME')
    host = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = email
    msg["From"] = username
    msg["Subject"] = "Product is cheaper"
    text = f"""<p><a href='{link}'> This item </a> is now {price} which is below your purchase level of {level} </p>"""
    msg.attach(MIMEText(text, 'html'))
    s.send_message(msg)
    del msg


def insert(link, discount_price, email):
    db.insert({time.time(): {'link': link, 'price': None, 'discount_price': discount_price, 'email': email}})

    documents = db.all()

    for document in documents:
        doc_key = list(document.keys())[0]
        url = document[doc_key]['link']
        price = document[doc_key]['price']
        level = document[doc_key]['discount_price']
        email = document[doc_key]['email']

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        myPrice = soup.find_all("span", {"class": "prc-dsc"})

        price = myPrice[0].text
        numbers = re.findall(r'\d+', price)
        thisPrice = float(''.join(numbers))

        if thisPrice != float(level):
            document[doc_key]['price'] = thisPrice
        if thisPrice <= float(level):
            print("Cheaper")
            emailMe(level, price, url, email)


if __name__ == '__main__':
    app.run()








