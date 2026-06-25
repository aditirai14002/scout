import pyautogui
from datetime import datetime


def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    print(f"✅ Scout captured the screen: {filename}")

    return filename


if __name__ == "__main__":
    take_screenshot()