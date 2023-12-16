import time
import pyautogui

save_directory = r'<PATH>'

def take_screenshot():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f'screenshot_{timestamp}.png'
    screenshot_path = save_directory + screenshot_name

    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting gracefully.")

while True:
    try:
        take_screenshot()
        time.sleep(15)
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting gracefully.")
        break
