import time
import os
import smtplib
from email.message import EmailMessage
from PIL import ImageGrab

EMAIL_ADRESS = os.getenv('USER_EMAIL')
EMAIL_PASS = os.getenv('USER_PASS')

msg = EmailMessage()
msg['Subject'] = 'Found a dota game!'
msg['From'] = EMAIL_ADRESS
msg['To'] = EMAIL_ADRESS
msg.set_content('You found a dota game, accept!')

time.sleep(5)

searching = True

while searching:
    pixel = ImageGrab.grab(bbox=(840, 540, 841, 541)).load()[0, 0]
    print('Finding Match...')
    time.sleep(1)

    if pixel[0] == 50 and pixel[1] == 78 and pixel[2] == 67:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADRESS, EMAIL_PASS)
            smtp.send_message(msg)

        print('Found game!')
        searching = False
