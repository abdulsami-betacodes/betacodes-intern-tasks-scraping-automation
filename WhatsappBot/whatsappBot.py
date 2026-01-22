# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome driver using webdriver-manager
print("Setting up Chrome driver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize the browser window
driver.maximize_window()

# Open WhatsApp Web
print("Opening WhatsApp Web...")
driver.get("https://web.whatsapp.com")

# Wait for the user to scan the QR code and login

# We wait until the search box appears (this means user has logged in)
print("Please scan the QR code to login to WhatsApp Web...")
wait = WebDriverWait(driver, 300)  # Wait up to 5 minutes for login

# Wait for the search box to appear (indicates successful login)
search_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
)
print("Login successful!")
time.sleep(5)
# Ask user for the contact name
contact_name = "Sami Kareem"
time.sleep(5)

# Click on the search box
search_box.click()


# Type the contact name in the search box
search_box.send_keys(contact_name)

# Wait for search results to appear and click on the contact
print(f"Searching for contact: {contact_name}")
contact_element = wait.until(
    EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]'))
)

# Click on the contact to open the chat
contact_element.click()
print(f"Opened chat with: {contact_name}")

# Wait for the message input box to appear
message_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
)

# Prepare the message text
message_text = """Hello buddy! This message it send by using a Python Selenium bot.

Here's what happened:
the bot i have build of whatsapp open up chrome then in that brouser whatsapp has been open then bar code came it waits till i scan the bar code after that i mention you name as madni korrejo or what the name saves in my phone like sami kareem or what ever then i type this msg like all it sends you the whole typed msg to you...

Pretty cool right? This demonstrates how Selenium can automate web applications! thats it """

# Click on the message input box
message_box.click()

# Type the message
message_box.send_keys(message_text)
time.sleep(10)
#wait = WebDriverWait(driver, 300)
# Send the message by pressing ENTER
message_box.send_keys(Keys.ENTER)
time.sleep(10)
#wait = WebDriverWait(driver, 300)
print("Message sent successfully!")
print("Browser will remain open. Close it manually when done.")

# Keep the browser open (don't close it)
# User can manually close when they want to exit