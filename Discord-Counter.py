'''
DISCLAIMER:
EXECUTING SUCH CODE IS AGAINST DISCORD'S TERMS OF SERVICE AND MAY LEAD TO CONSEQUENCES.
PLEASE RUN THIS CODE AT YOUR OWN RISK.
'''

# Import the necessary modules
import requests
import time
import random
import keyboard

# Base variables
num = int(input('Enter the first number: '))
main = 'INSERT_TOKEN_HERE'
alt = 'INSERT_TOKEN_HERE'

# This sends a message to the counting channel
# Requires a token and message
def send_msg(token, msg, channel = 1220081614277574728):
    # Create POST request headers
    url = f'https://discord.com/api/v9/channels/{channel}/messages'
    data = {
        'content': msg
    }
    headers = {
        'Authorization': token
    }

    # Post the API request
    response = requests.post(url, headers = headers, json = data)

# Main loop
# Sends a message with a random delay to avoid script detection
while True:
    # Break out of the program when ESC is pressed
    while keyboard.is_pressed('esc'):
        print('Exiting the program:\nStopped at ' + str(num - 1))
        exit(0)
    
    # Count on the main account
    send_msg(main, str(num))
    time.sleep(random.uniform(0.3, 0.5))

    # Count on the alt account
    send_msg(alt, str(num + 1))
    time.sleep(random.uniform(0.3, 0.5))

    # Increase the count by 2
    num += 2
