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
import os

os.system('cls') # Clears the screen on Windows

# Base variables
num = int(input('What is the starting number? '))
main = 'INPUT_ACCOUNT_TOKEN_STRING'
alt = 'INPUT_ACCOUNT_TOKEN_STRING'
channel = INPUT_DEFAULT_CHANNEL_ID_INTEGER
print('The program has started! Hold ESC to exit the program at any time. The count will be logged below.')

# This sends a message to the counting channel
# Requires a token and message
def send(token, message, channel):
    # Create POST request headers
    url = f'https://discord.com/api/v9/channels/{channel}/messages'
    data = {
        'content': message
    }
    headers = {
        'Authorization': token
    }

    # Send the POST request
    response = requests.post(url, json = data, headers = headers)

    # If the code reaches here, the request has finished
    # However, we must check for errors
    if response.status_code != 200:
        print('Exiting the program: Stopped at ' + str(num - 1))
        print('The request did not return status code 200 (OK). The script has been stopped to avoid breaking the count.')
        exit(0)

# Main loop
# Sends a message with a random delay to avoid script detection
while True:
    # Break out of the program when ESC is pressed
    while keyboard.is_pressed('esc'):
        print('Exiting the program: Stopped at ' + str(num - 1))
        exit(0)
    
    # Count on the main account
    send(main, str(num), channel)
    print('[MAIN]', num)
    time.sleep(random.uniform(0.7, 0.9))
    num += 1

    # Count on the alt account
    send(alt, str(num), channel)
    print('[ALT]', num)
    time.sleep(random.uniform(0.7, 0.9))
    num += 1
