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
import string

# Comment out the line below if you are using a Unix-based OS
os.system('cls')

# Input variables
num = int(input('What is the starting number? '))
delay = float(input('What is the delay? '))

# Configuration variables
main = 'REPLACE_WITH_FIRST_ACCOUNT_TOKEN'
alt = 'REPLACE_WITH_SECOND_ACCOUNT_TOKEN'
channel = REPLACE_WITH_COUNTING_CHANNEL_ID

# Base variables
curr = main # DO NOT TOUCH
mode = 0 # DO NOT TOUCH

print('The program has started! Hold ESC to exit the program at any time. The count will be logged below.')

# This periodically sends random messages in the same channel to check if the rate limit has ended
def check(token):
    global num, channel, delay, curr, mode
    i = 1

    # Run the loop until the rate limit is gone
    while True:
        while keyboard.is_pressed('esc'):
            print('Exiting the program: Stopped at ' + str(num - 1) + '.')
            exit(0)
        
        status = send(token, ''.join(random.choices(string.ascii_letters + string.digits, k = 16)), channel, mode)

        # Proceed if status code is 200 (OK)
        if status == 200:
            timeout = random.uniform(delay + 6.1425, delay + 10.8745)

            print(f'You are no longer rate limited by Discord! The loop will terminate after {timeout} seconds. (Iteration {i})')
            
            time.sleep(timeout)
            mode = 0

            delay *= 1.3765
            break
        
        
        timeout = random.uniform(delay + 6.1425, delay + 10.8745)
        
        print(f'You are still rate limited by Discord! Checking for rate limit again in {timeout} seconds. (Iteration {i})')
        
        i += 1

        time.sleep(timeout)

# This sends a message to the counting channel
def send(token, message, channel, md):
    global num, main, alt, curr, mode
    # POST request headers
    url = f'https://discord.com/api/v9/channels/{channel}/messages'
    data = {
        'content': message
    }
    headers = {
        'Authorization': token
    }

    response = requests.post(url, json = data, headers = headers)

    # If the code reaches here, the request has finished
    if md == 0:
        if not response.ok:
            if response.status_code == 429:
                print('The request returned status code 429 (Too Many Requests). The program will be thrown into a loop to check if the rate limit has ended.')
                mode = 1

                time.sleep(random.uniform(delay + 6.1425, delay + 10.8745))
                check(token)
            else:
                print('Exiting the program: Stopped at ' + str(num - 1) + '.')
                print('The request did not return status code 200 (OK). The script has been stopped to avoid breaking the count.')
                exit(0)
        else:
            if curr == main:
                print('[MAIN]', num)
                curr = alt
            else:
                print('[ALT]', num)
                curr = main

            num += 1
    else:
        return response.status_code

while True:
    while keyboard.is_pressed('esc'):
        print('Exiting the program: Stopped at ' + str(num - 1) + '.')
        exit(0)
    
    if mode == 0 and curr == main:
        send(main, str(num), channel, mode)
        time.sleep(random.uniform(delay * 0.9355, delay * 2.1625))

    if mode == 0 and curr == alt:
        send(alt, str(num), channel, mode)
        time.sleep(random.uniform(delay * 0.9355, delay * 2.1625))
