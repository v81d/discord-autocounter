import pyautogui
import keyboard
import time

# Select the points
main = pyautogui.Point(x=1605, y=1034)
alt = pyautogui.Point(x=1586, y=494)
num = int(input('What number do you want to start at? '))

def count(input):
    global num
    # Select the input point
    pyautogui.click(input)
    # Enter the number in the input box, then press enter and increase the count
    keyboard.write(str(num))
    keyboard.press_and_release('enter')
    num += 1

time.sleep(3)
# Main loop
while True:
    # Exit script if ESC is pressed
    while keyboard.is_pressed('esc'):
        print('Exiting the program:\nStopping at ' + str(num))
        exit(0)

    # Execute function on the main point
    count(main)
    # Wait 1.5s
    time.sleep(2)

    # Execute function on the other point
    count(alt)
    # Wait 1.5s
    time.sleep(2)