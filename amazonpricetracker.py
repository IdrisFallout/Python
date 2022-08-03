import requests
from bs4 import BeautifulSoup
import smtplib
import time

global round_price_ksh

URL = 'https://www.amazon.com/Raspberry-Pi-MS-004-00000024-Model-Board/dp/B01LPLPBS8/ref=sr_1_6?crid=1VQEENVD25W2P' \
      '&keywords=raspberry+pi&qid=1659520949&sprefix=Rasp%2Caps%2C560&sr=8-6 '
URL2 = 'https://www.exchangerates.org.uk/Dollars-to-Kenyan-Shillings-currency-conversion-page.html'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.71'}


def check_price():
    try:
        page = requests.get(URL, headers=headers)
        page2 = requests.get(URL2, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        title = soup.find(id="productTitle").get_text()
        price = soup.find(class_="a-offscreen").get_text()
        exchange_rate = soup2.find(id="shd2b;").get_text()

        final_title = title.strip()
        price_usd = float(price[1:].strip())
        usd_to_ksh = float(exchange_rate.strip())

        price_ksh = (price_usd * usd_to_ksh)
        round_price_ksh = round(price_ksh, 2)

        print(final_title)
        # print(str(price_usd) + " * " + str(usd_to_ksh) + " = " + str(round_price_ksh))
        print("ksh " + str(round_price_ksh))
        print("1 USD = ksh " + str(usd_to_ksh))

        if round_price_ksh > 13000:
            send_email()
    except:
        print("Error occurred")


def send_email():
    print(f"Sending Email...f{round_price_ksh}")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender@gmail.com', 'password')
    subject = 'The price fell down!'
    body = 'Check the amazon link: ' + URL
    # c_price = 'Current Price: ' + str(round_price_ksh)

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'sender@gmail.com',
        'receiver@gmail.com',
        msg
    )
    print("EMAIL HAS BEEN SENT")
    server.quit()


while True:
    seconds = 10
    check_price()
    time.sleep(seconds)




