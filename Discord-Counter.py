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

# Comment out the line below if you are using MacOS
os.system('cls') # Clears the screen on Windows

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
    i = 1 # Set the iteration count to 1

    # Run the loop until the rate limit is gone
    while True:
        # Break out of the program when ESC is pressed
        while keyboard.is_pressed('esc'):
            print('Exiting the program: Stopped at ' + str(num - 1) + '.')
            exit(0)
        
        # Send the test message
        status = send(token, ''.join(random.choices(string.ascii_letters + string.digits, k = 16)), channel, mode)

        # Execute if status code is 200 (OK)
        if status == 200:
            timeout = random.uniform(delay + 6.1425, delay + 10.8745) # Set the timeout (in seconds)

            print(f'You are no longer rate limited by Discord! The loop will terminate after {timeout} seconds. (Iteration {i})')
            
            time.sleep(timeout)
            mode = 0

            # Break out of loop and increase the delay to prevent another rate limit
            delay *= 1.3765
            break

        # Execute if status code is 429 or any other error
        
        timeout = random.uniform(delay + 6.1425, delay + 10.8745) # Set the timeout (in seconds)
        
        print(f'You are still rate limited by Discord! Checking for rate limit again in {timeout} seconds. (Iteration {i})')
        
        # Add 1 to the iteration count
        i += 1

        # Set the timeout
        time.sleep(timeout)

# This sends a message to the counting channel
# Requires a token and message
def send(token, message, channel, md):
    global num, main, alt, curr, mode
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
    if md == 0:
        # We must check for errors
        if not response.ok:
            if response.status_code == 429:
                print('The request returned status code 429 (Too Many Requests). The program will be thrown into a loop to check if the rate limit has ended.')
                mode = 1

                # Start the loop
                time.sleep(random.uniform(delay + 6.1425, delay + 10.8745))
                check(token)
            else:
                print('Exiting the program: Stopped at ' + str(num - 1) + '.')
                print('The request did not return status code 200 (OK). The script has been stopped to avoid breaking the count.')
                exit(0)
        else:
            num += 1
            if curr == main:
                curr = alt
            else:
                curr = main
    else:
        # The mode is 1, meaning we are currently in the rate limit check loop
        return response.status_code

# Main loop
# Sends a message with a random delay to avoid script detection
while True:
    # Break out of the program when ESC is pressed
    while keyboard.is_pressed('esc'):
        print('Exiting the program: Stopped at ' + str(num - 1) + '.')
        exit(0)
    
    if mode == 0 and curr == main:
        # Count on the main account
        send(main, str(num), channel, mode)
        print('[MAIN]', num)
        time.sleep(random.uniform(delay * 0.9355, delay * 2.1625))

    if mode == 0 and curr == alt:
        # Count on the alt account
        send(alt, str(num), channel, mode)
        print('[ALT]', num)
        time.sleep(random.uniform(delay * 0.9355, delay * 2.1625))
