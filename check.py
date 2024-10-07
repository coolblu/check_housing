import time
import smtplib
import requests
from bs4 import BeautifulSoup
from getpass import getpass
from tqdm import tqdm

URL = "https://www.hacanet.org/south-austin-pbra/"
WAITLIST_CLOSED_TEXT = "The waitlist for this property is CLOSED."
CHECK_INTERVAL = 60  

sender_email = input("Enter your Gmail address: ")
receiver_email = input("Enter the recipient email: ")
app_password = getpass("Enter your Gmail App Password (input hidden): ")

def check_waitlist_status():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find(id="elementor-tab-content-1021")
    
    if element and WAITLIST_CLOSED_TEXT not in element.get_text():
        return True
    return False

def send_email_notification():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        message = f"Subject: Waitlist Opened!\n\nThe waitlist is now open. Check it out at {URL}."
        server.sendmail(sender_email, receiver_email, message)
        print("Notification sent!")

while True:
    if check_waitlist_status():
        send_email_notification()
        break 
    else:
        print("Waitlist is still closed. Checking again in a minute.")
        
        for _ in tqdm(range(CHECK_INTERVAL), desc="Time until next check", unit="s"):
            time.sleep(1)
