import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Ninja-OL501-Pressure-SmartLid-Capacity/dp/B0995HLCQ8/ref=sr_1_2?" \
      "crid=18F0ZYK54ICKW&keywords=ninja+foodi&qid=1687812963&sprefix=ninja+foodi%2Caps%2C159&sr=8-2&u" \
      "fe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0"
MY_EMAIL = "laucoding@gmail.com"
MY_PASSWORD = "PASSWORD"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find(name="span", class_="a-offscreen")
price_text = price.get_text().split("$")
price_split = float(price_text[1])

if price_split <= 110:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="deleonquintero@gmail.com",
            msg=f"Subject:Price Reduce\n\n Price Reduce to {price_split} for product\n{URL}"
        )
