import time
from plyer import notification

# This loop runs indefinitely.
while True:
    # Display a desktop notification with a title, message, app icon, and a timeout of 5 seconds.
    notification.notify(
        title="Hello Hamza, Drink a glass of water!",
        message="8 glasses of water a day!",
        app_icon="icon.ico.ico",  # Make sure the icon file exists in the same directory.
        timeout=5
    )

    # Wait for 10 seconds before displaying the next notification.
    time.sleep(10)