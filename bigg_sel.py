from selenium import webdriver
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv('account_sid'))
account_sid = os.getenv('auth_token')
auth_token = os.getenv('account_sid')
twilio_no = os.getenv('twilio_no')
user_no = os.getenv('user_no')


chrome_driver = os.getenv('driver')
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(os.getenv('search'))
is_avaliable = str(driver.find_element_by_id('availability').text)
print(is_avaliable)
driver.quit()

client = Client(account_sid, auth_token)
msg = 'ASUS TUF Gaming A15 Laptop 15.6" FHD 144Hz Ryzen 5 4600H, GTX 1650 4GB Graphics (8GB RAM/1TB HDD + 256GB NVMe SSD/Windows 10/Bonfire Black/2.30 Kg), FA506IH-AL057T /n https://www.amazon.in/ASUS-GTX-1650-Graphics-Windows-FA506IH-AL057T/dp/B088R5WFHS'

if "In Stock" in is_avaliable:
    message = client.messages \
        .create(
            body=f"\nLAPTOP IS IN STOCK \n {msg}",
            from_=twilio_no,
            to=user_no
        )
    print(message.status)
    print(message.sid)
else:
    message = client.messages \
        .create(
            body=f"\nLAPTOP IS OUT OF STOCK \n {msg}",
            from_=twilio_no,
            to=user_no
        )
    print(message.status)
    print(message.sid)
