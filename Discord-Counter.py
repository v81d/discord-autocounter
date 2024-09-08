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

    try:
        # Send the POST request
        response = requests.post(url, json = data, headers = headers)
    
        # If the code reaches here, the request has finished
        print('Request finished.')
        
    except requests.exceptions.RequestException as e:
        # This will catch any request-related errors, indicating the request was not able to finish
        print(f'An error occurred: {e}')
        print('Exiting the program: Stopped at ' + str(num - 1))
        print('Stopped to avoid any errors.')
        exit(0)

# Main loop
# Sends a message with a random delay to avoid script detection
while True:
    # Break out of the program when ESC is pressed
    while keyboard.is_pressed('esc'):
        print('Exiting the program: Stopped at ' + str(num - 1))
        exit(0)
    
    # Count on the main account
    send_msg(main, str(num))
    time.sleep(random.uniform(0.5, 0.8))
    num += 1

    # Count on the alt account
    send_msg(alt, str(num))
    time.sleep(random.uniform(0.5, 0.8))
    num += 1
