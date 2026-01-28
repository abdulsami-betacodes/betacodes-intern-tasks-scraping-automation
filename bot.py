# # ============================================================
# # CHUNK 1: IMPORT REQUIRED LIBRARIES
# # ============================================================

# # Selenium webdriver - main library for browser automation
# from selenium import webdriver

# # For locating elements on webpage (by XPath, ID, etc.)
# from selenium.webdriver.common.by import By

# # For keyboard actions like pressing ENTER
# from selenium.webdriver.common.keys import Keys

# # For setting up Chrome driver service
# from selenium.webdriver.chrome.service import Service

# # For configuring Chrome browser options (like saving session)
# from selenium.webdriver.chrome.options import Options

# # For dynamic waits - waits until element appears (better than time.sleep)
# from selenium.webdriver.support.ui import WebDriverWait

# # For wait conditions like "element is present", "element is clickable"
# from selenium.webdriver.support import expected_conditions as EC

# # For auto-downloading and managing Chrome driver
# from webdriver_manager.chrome import ChromeDriverManager

# # For handling file and folder paths
# import os

# # For adding delays and timestamps
# import time
# from datetime import datetime

# # For logging system
# import logging

# # For configuration file handling
# import json

# # For random delays (human-like behavior)
# import random

# # For image validation
# from PIL import Image

# # For graceful shutdown handling
# import signal
# import sys

# # For progress bar
# from tqdm import tqdm


# # ============================================================
# # CHUNK 2: LOGGING SETUP
# # ============================================================

# # Create logs folder if it doesn't exist
# if not os.path.exists('logs'):
#     os.makedirs('logs')

# # Create log filename with timestamp
# log_filename = f"logs/whatsapp_bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# # Configure logging to both file and console
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler(log_filename, encoding='utf-8'),  # Save to file
#         logging.StreamHandler()  # Also print to console
#     ]
# )

# logging.info("="*60)
# logging.info("WhatsApp Image Sender Bot Started")
# logging.info("="*60)


# # ============================================================
# # CHUNK 3: CONFIGURATION FILE LOADING
# # ============================================================

# # Default configuration
# DEFAULT_CONFIG = {
#     "contacts": ["Sami Kareem", "Madni Korejo"],
#     "images_folder": '/Users/samikareem/Desktop/wolf_images',
#     "max_wait_time": 30,
#     "delay_between_contacts": 2,
#     "delay_between_images": 1,
#     "max_retry_attempts": 3,
#     "batch_size": 5,
#     "batch_break_duration": 60,
#     "dry_run": True 
# }

# # Configuration file path
# config_file = "config.json"

# # Load or create configuration file
# if os.path.exists(config_file):
#     logging.info(f"Loading configuration from {config_file}")
#     with open(config_file, 'r', encoding='utf-8') as f:
#         config = json.load(f)
#     logging.info("✓ Configuration loaded successfully")
# else:
#     logging.warning(f"Configuration file not found. Creating default config.json")
#     with open(config_file, 'w', encoding='utf-8') as f:
#         json.dump(DEFAULT_CONFIG, f, indent=4)
#     config = DEFAULT_CONFIG
#     logging.info(f"✓ Created {config_file} - Please edit it with your settings")

# # Extract configuration values
# contacts_list = config.get('contacts', DEFAULT_CONFIG['contacts'])
# images_folder_path = config.get('images_folder', DEFAULT_CONFIG['images_folder'])
# max_wait_time = config.get('max_wait_time', DEFAULT_CONFIG['max_wait_time'])
# delay_between_contacts = config.get('delay_between_contacts', DEFAULT_CONFIG['delay_between_contacts'])
# delay_between_images = config.get('delay_between_images', DEFAULT_CONFIG['delay_between_images'])
# max_retry_attempts = config.get('max_retry_attempts', DEFAULT_CONFIG['max_retry_attempts'])
# batch_size = config.get('batch_size', DEFAULT_CONFIG['batch_size'])
# batch_break_duration = config.get('batch_break_duration', DEFAULT_CONFIG['batch_break_duration'])
# DRY_RUN = config.get('dry_run', DEFAULT_CONFIG['dry_run'])


# # # ============================================================
# # # CHUNK 4: XPATHS - PASTE YOUR XPATHS HERE
# # # ============================================================

# # # XPath for WhatsApp Web search box (top left, to search contacts)
# # XPATH_SEARCH_BOX = '//div[@aria-label="Search input textbox"]'


# # # XPath for contact name in search results (appears after typing in search)
# # # Note: We'll replace contact name dynamically in code
# # # XPATH_CONTACT_IN_RESULTS = '//span[@title="{CONTACT_NAME}"]'
# # # Primary XPath for contact results
# # XPATH_CONTACT_IN_RESULTS = '//span[@title="{CONTACT_NAME}"]'

# # # Backup XPath if primary fails (clicks on the entire contact row)
# # XPATH_CONTACT_RESULT_ROW = '//div[@role="listitem"]//span[@title="{CONTACT_NAME}"]'


# # # XPath for attachment button (paperclip icon in chat)
# # XPATH_ATTACHMENT_BUTTON = '//button[@aria-label="Attach"][aria-haspopup="menu"][type="button"]'

# # # XPath for image/video option after clicking attachment button
# # XPATH_IMAGE_VIDEO_INPUT = '//span[text()="Photos & videos"]'

# # # XPath for send button (green send arrow after selecting image)
# # XPATH_SEND_BUTTON = '//span[@data-icon="wds-ic-send-filled"][aria-hidden="true"]'




# # ============================================================
# # CHUNK 4: XPATHS - CORRECTED AND SIMPLIFIED
# # ============================================================

# # XPath for WhatsApp Web search box (top left, to search contacts)
# XPATH_SEARCH_BOX = '//div[@aria-label="Search input textbox"]'

# # XPath for contact name in search results
# # {CONTACT_NAME} will be replaced dynamically in the code
# XPATH_CONTACT_IN_RESULTS = '//span[@title="{CONTACT_NAME}"]'

# # XPath for attachment button (paperclip icon in chat)
# XPATH_ATTACHMENT_BUTTON = '//div[@title="Attach"]'

# # XPath for "Photos & videos" button in attachment menu
# XPATH_PHOTOS_VIDEOS_BUTTON = '//span[text()="Photos & videos"]'

# # XPath for file input element (accepts files)
# XPATH_IMAGE_VIDEO_INPUT = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'

# # XPath for send button (green arrow after selecting image)
# XPATH_SEND_BUTTON = '//span[@data-icon="send"]'








# # ============================================================
# # CHUNK 5: SENT CONTACTS TRACKING SYSTEM
# # ============================================================

# # File to track which contacts have already received images
# sent_contacts_file = "sent_contacts.txt"

# def mark_as_sent(contact_name):
#     """
#     Mark a contact as already sent by adding to tracking file
#     This prevents duplicate sends if script is rerun
#     """
#     with open(sent_contacts_file, 'a', encoding='utf-8') as f:
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         f.write(f"{contact_name}|{timestamp}\n")
#     logging.info(f"Marked as sent: {contact_name}")

# def is_already_sent(contact_name):
#     """
#     Check if contact has already received images
#     Returns True if found in tracking file, False otherwise
#     """
#     if not os.path.exists(sent_contacts_file):
#         return False
    
#     with open(sent_contacts_file, 'r', encoding='utf-8') as f:
#         sent_contacts = [line.split('|')[0] for line in f.read().splitlines()]
    
#     return contact_name in sent_contacts

# def get_sent_contacts_list():
#     """
#     Get list of all contacts that already received images
#     """
#     if not os.path.exists(sent_contacts_file):
#         return []
    
#     with open(sent_contacts_file, 'r', encoding='utf-8') as f:
#         return [line.split('|')[0] for line in f.read().splitlines()]


# # ============================================================
# # CHUNK 6: UTILITY FUNCTIONS
# # ============================================================

# def human_delay(min_sec=1, max_sec=3):
#     """
#     Random delay to simulate human behavior and avoid detection
#     Uses random time between min_sec and max_sec
#     """
#     delay = random.uniform(min_sec, max_sec)
#     time.sleep(delay)

# def take_error_screenshot(driver, contact_name="unknown"):
#     """
#     Takes screenshot when error occurs for debugging
#     Saves in screenshots folder with timestamp
#     """
#     # Create screenshots folder if doesn't exist
#     if not os.path.exists('screenshots'):
#         os.makedirs('screenshots')
    
#     # Generate filename with timestamp
#     timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#     filename = f"screenshots/error_{contact_name}_{timestamp}.png"
    
#     try:
#         driver.save_screenshot(filename)
#         logging.info(f"Screenshot saved: {filename}")
#     except Exception as e:
#         logging.error(f"Failed to take screenshot: {str(e)}")

# def signal_handler(sig, frame):
#     """
#     Handle Ctrl+C gracefully - saves progress and exits cleanly
#     """
#     print("\n\n" + "⚠"*30)
#     print("INTERRUPT RECEIVED - SHUTTING DOWN GRACEFULLY")
#     print("⚠"*30)
#     logging.warning("Script interrupted by user (Ctrl+C)")
    
#     print("\n✓ Progress has been saved")
#     print("✓ You can resume by running the script again")
#     print("✓ Goodbye!\n")
    
#     sys.exit(0)

# # Register signal handler for Ctrl+C
# signal.signal(signal.SIGINT, signal_handler)


# # ============================================================
# # CHUNK 7: IMAGE VALIDATION FUNCTION
# # ============================================================

# def validate_image(image_path):
#     """
#     Validates if image file is not corrupted and can be opened
#     Returns True if valid, False if corrupted or invalid
#     """
#     try:
#         # Try to open and verify image
#         img = Image.open(image_path)
#         img.verify()  # Verify image integrity
        
#         # Check file size (optional - skip very large files)
#         file_size_mb = os.path.getsize(image_path) / (1024 * 1024)
#         if file_size_mb > 50:  # WhatsApp has ~16MB limit, but we use 50MB as safe limit
#             logging.warning(f"Image too large ({file_size_mb:.2f}MB): {os.path.basename(image_path)}")
#             return False
        
#         return True
#     except Exception as e:
#         logging.error(f"Invalid image {os.path.basename(image_path)}: {str(e)}")
#         return False


# # ============================================================
# # CHUNK 8: GET IMAGES FROM FOLDER
# # ============================================================

# def get_images_from_folder(folder_path):
#     """
#     Reads all valid image files from the specified folder
#     Returns a list of full file paths for each valid image
#     Only includes images that pass validation
#     """
#     # List to store valid image file paths
#     image_files = []
    
#     # Supported image formats
#     image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    
#     # Check if folder exists
#     if not os.path.exists(folder_path):
#         logging.error(f"Folder not found: {folder_path}")
#         return image_files
    
#     logging.info(f"Scanning folder for images: {folder_path}")
    
#     # Loop through all files in the folder
#     for filename in os.listdir(folder_path):
#         # Get file extension (e.g., .jpg)
#         file_ext = os.path.splitext(filename)[1].lower()
        
#         # Check if file is an image
#         if file_ext in image_extensions:
#             # Create full path to image file
#             full_path = os.path.join(folder_path, filename)
            
#             # Validate image before adding
#             if validate_image(full_path):
#                 image_files.append(full_path)
#                 logging.info(f"  ✓ Valid image: {filename}")
#             else:
#                 logging.warning(f"  ✗ Skipped invalid image: {filename}")
    
#     logging.info(f"Found {len(image_files)} valid image(s)")
#     return image_files


# # ============================================================
# # CHUNK 9: WHATSAPP HEALTH CHECK
# # ============================================================

# def check_whatsapp_health(driver, wait_object):
#     """
#     Checks if WhatsApp Web is still loaded and responsive
#     Returns True if healthy, False if disconnected or unresponsive
#     """
#     try:
#         # Try to find search box - if found, WhatsApp is responsive
#         wait_object.until(
#             EC.presence_of_element_located((By.XPATH, XPATH_SEARCH_BOX))
#         )
#         return True
#     except Exception as e:
#         logging.error(f"WhatsApp health check failed: {str(e)}")
#         take_error_screenshot(driver, "health_check_failed")
#         return False


# # ============================================================
# # CHUNK 10: SEARCH AND OPEN CONTACT WITH RETRY
# # ============================================================

# def search_and_open_contact(contact_name, wait_object, driver, attempt=1):
#     """
#     Searches for a contact and opens their chat
#     Includes retry mechanism for reliability
#     Returns True if successful, False if contact not found after all retries
#     """
#     try:
#         logging.info(f"[Attempt {attempt}/{max_retry_attempts}] Searching for: {contact_name}")
        
#         # Find the search box and wait for it to be clickable
#         search_box = wait_object.until(
#             EC.element_to_be_clickable((By.XPATH, XPATH_SEARCH_BOX))
#         )
        
#         # Click on search box to activate it
#         search_box.click()
#         human_delay(0.5, 1)
        
#         # Type contact name in search box
#         search_box.send_keys(contact_name)
#         human_delay(1, 2)  # Wait for search results to appear
        
#         # Wait for search results and find the contact
#         contact_element = wait_object.until(
#             EC.element_to_be_clickable((By.XPATH, XPATH_CONTACT_IN_RESULTS))
#         )
        
#         # Click on the contact to open chat
#         contact_element.click()
#         human_delay(1, 2)  # Wait for chat to load
        
#         logging.info(f"✓ Successfully opened chat: {contact_name}")
#         return True
        
#     except Exception as e:
#         logging.error(f"Error searching for '{contact_name}': {str(e)}")
#         take_error_screenshot(driver, contact_name)
        
#         # Retry if attempts remaining
#         if attempt < max_retry_attempts:
#             logging.info(f"Retrying in 3 seconds...")
#             time.sleep(3)
            
#             # Clear search box before retry
#             try:
#                 search_box = wait_object.until(
#                     EC.element_to_be_clickable((By.XPATH, XPATH_SEARCH_BOX))
#                 )
#                 search_box.click()
#                 search_box.send_keys(Keys.CONTROL + "a")
#                 search_box.send_keys(Keys.BACKSPACE)
#             except:
#                 pass
            
#             return search_and_open_contact(contact_name, wait_object, driver, attempt + 1)
#         else:
#             logging.error(f"Failed to find contact after {max_retry_attempts} attempts: {contact_name}")
#             return False


# # ============================================================
# # CHUNK 11: SEND IMAGES WITH RETRY
# # ============================================================

# def send_images_to_contact(contact_name, image_paths, wait_object, driver, attempt=1):
#     """
#     Sends all images from the list to the currently open chat
#     Includes retry mechanism and dry run support
#     Returns True if successful, False if failed after all retries
#     """
#     try:
#         logging.info(f"Preparing to send {len(image_paths)} image(s) to {contact_name}")
        
#         # DRY RUN MODE - simulate sending without actually sending
#         if DRY_RUN:
#             logging.info(f"[DRY RUN] Would send {len(image_paths)} images to {contact_name}")
#             for idx, img_path in enumerate(image_paths, 1):
#                 logging.info(f"  [DRY RUN] Image {idx}: {os.path.basename(img_path)}")
#             time.sleep(2)  # Simulate processing time
#             return True
        
#         # ACTUAL SENDING MODE
#         # Loop through each image
#         for idx, image_path in enumerate(image_paths, 1):
#             logging.info(f"  → Sending image {idx}/{len(image_paths)}: {os.path.basename(image_path)}")
            
#             # Wait for and click the attachment button (paperclip icon)
#             attachment_button = wait_object.until(
#                 EC.element_to_be_clickable((By.XPATH, XPATH_ATTACHMENT_BUTTON))
#             )
#             attachment_button.click()
#             human_delay(0.5, 1)
            
#             # Wait for the file input element to appear
#             file_input = wait_object.until(
#                 EC.presence_of_element_located((By.XPATH, XPATH_IMAGE_VIDEO_INPUT))
#             )
            
#             # Send the image file path to the input element
#             file_input.send_keys(image_path)
#             human_delay(1, 2)  # Wait for image to upload
            
#             # Wait for the send button to appear and be clickable
#             send_button = wait_object.until(
#                 EC.element_to_be_clickable((By.XPATH, XPATH_SEND_BUTTON))
#             )
            
#             # Click send button to send the image
#             send_button.click()
            
#             # Wait between images with human-like delay
#             human_delay(delay_between_images, delay_between_images + 1)
            
#             logging.info(f"  ✓ Image {idx} sent successfully")
        
#         logging.info(f"✓ All {len(image_paths)} images sent to {contact_name}")
#         return True
        
#     except Exception as e:
#         logging.error(f"Error sending images to '{contact_name}': {str(e)}")
#         take_error_screenshot(driver, contact_name)
        
#         # Retry if attempts remaining
#         if attempt < max_retry_attempts:
#             logging.info(f"Retrying in 3 seconds...")
#             time.sleep(3)
#             return send_images_to_contact(contact_name, image_paths, wait_object, driver, attempt + 1)
#         else:
#             logging.error(f"Failed to send images after {max_retry_attempts} attempts")
#             return False


# # ============================================================
# # CHUNK 12: CLEAR SEARCH BOX
# # ============================================================

# def clear_search_box(wait_object, driver):
#     """
#     Clears the search box to prepare for next contact search
#     Includes error handling and retry
#     """
#     try:
#         # Find the search box
#         search_box = wait_object.until(
#             EC.element_to_be_clickable((By.XPATH, XPATH_SEARCH_BOX))
#         )
        
#         # Click on search box
#         search_box.click()
#         human_delay(0.3, 0.5)
        
#         # Select all text and delete it
#         search_box.send_keys(Keys.CONTROL + "a")
#         search_box.send_keys(Keys.BACKSPACE)
        
#         logging.info("Search box cleared")
#         return True
        
#     except Exception as e:
#         logging.warning(f"Could not clear search box: {str(e)}")
#         return False


# # ============================================================
# # CHUNK 13: CHROME SETUP WITH PERSISTENT SESSION
# # ============================================================

# logging.info("="*60)
# logging.info("Setting up Chrome browser with persistent session...")
# logging.info("="*60)

# # Create Chrome options object to customize browser behavior
# chrome_options = Options()

# # Create a folder to save WhatsApp login session permanently
# user_data_dir = os.path.join(os.getcwd(), "whatsapp_session")
# chrome_options.add_argument(f"user-data-dir={user_data_dir}")

# # Disable automation detection features
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)

# # Additional options for stability
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")

# # Initialize Chrome driver with custom options
# try:
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=chrome_options
#     )
#     logging.info("✓ Chrome browser opened successfully")
# except Exception as e:
#     logging.error(f"Failed to initialize Chrome: {str(e)}")
#     sys.exit(1)

# # Maximize browser window
# driver.maximize_window()


# # ============================================================
# # CHUNK 14: OPEN WHATSAPP WEB AND LOGIN
# # ============================================================

# logging.info("\nOpening WhatsApp Web...")

# # Navigate to WhatsApp Web
# driver.get("https://web.whatsapp.com")

# # Create WebDriverWait object for dynamic waiting
# wait = WebDriverWait(driver, max_wait_time)

# try:
#     # Try to find search box (means already logged in)
#     logging.info("Checking login status...")
#     search_box = wait.until(
#         EC.presence_of_element_located((By.XPATH, XPATH_SEARCH_BOX))
#     )
#     logging.info("✓ Already logged in! Session restored successfully")
    
# except:
#     # Search box not found - first time login needed
#     logging.warning("First time login detected")
#     print("\n" + "⚠"*30)
#     print("PLEASE SCAN QR CODE WITH YOUR PHONE NOW")
#     print("⚠"*30 + "\n")
    
#     # Wait for user to scan QR code
#     search_box = wait.until(
#         EC.presence_of_element_located((By.XPATH, XPATH_SEARCH_BOX))
#     )
#     logging.info("✓ Login successful! Session saved for future use")

# logging.info("✓ WhatsApp Web is ready!\n")
# time.sleep(2)


# # ============================================================
# # CHUNK 15: LOAD IMAGES FROM FOLDER
# # ============================================================

# logging.info("="*60)
# logging.info("LOADING IMAGES")
# logging.info("="*60)

# # Get all valid images from folder
# images_to_send = get_images_from_folder(images_folder_path)

# # Check if any images found
# if len(images_to_send) == 0:
#     logging.error("No valid images found in folder!")
#     logging.error(f"Please check the path: {images_folder_path}")
#     print("\n" + "❌"*30)
#     print("NO IMAGES FOUND - CANNOT PROCEED")
#     print("❌"*30)
#     print(f"\nPlease:")
#     print(f"1. Check the folder path in config.json")
#     print(f"2. Ensure images exist in the folder")
#     print(f"3. Run the script again")
#     print("\nBrowser will remain open for inspection...")
    
#     # Keep browser open
#     try:
#         while True:
#             time.sleep(1)
#             driver.current_url
#     except:
#         logging.info("Browser closed")
    
#     sys.exit(1)


# # ============================================================
# # CHUNK 16: PREPARE CONTACTS LIST (SKIP ALREADY SENT)
# # ============================================================

# logging.info("="*60)
# logging.info("PREPARING CONTACTS LIST")
# logging.info("="*60)

# # Get list of contacts already sent
# already_sent = get_sent_contacts_list()

# if already_sent:
#     logging.info(f"Found {len(already_sent)} contact(s) already sent:")
#     for contact in already_sent:
#         logging.info(f"  - {contact}")

# # Filter out already sent contacts
# pending_contacts = [c for c in contacts_list if not is_already_sent(c)]

# if not pending_contacts:
#     logging.info("\n" + "✓"*30)
#     logging.info("ALL CONTACTS ALREADY RECEIVED IMAGES!")
#     logging.info("✓"*30)
#     print("\nNothing to do. All contacts in list have already been sent images.")
#     print("To resend, delete or rename 'sent_contacts.txt' file.")
    
#     # Keep browser open
#     print("\nBrowser will remain open...")
#     try:
#         while True:
#             time.sleep(1)
#             driver.current_url
#     except:
#         logging.info("Browser closed")
    
#     sys.exit(0)

# logging.info(f"\n✓ {len(pending_contacts)} contact(s) pending:")
# for contact in pending_contacts:
#     logging.info(f"  - {contact}")


# # ============================================================
# # CHUNK 17: DISPLAY PRE-RUN SUMMARY
# # ============================================================

# print("\n" + "="*60)
# print("PRE-RUN SUMMARY")
# print("="*60)
# print(f"Images to send: {len(images_to_send)}")
# print(f"Total contacts: {len(contacts_list)}")
# print(f"Already sent: {len(already_sent)}")
# print(f"Pending contacts: {len(pending_contacts)}")
# print(f"Batch size: {batch_size} contacts per batch")
# print(f"Dry run mode: {'ENABLED' if DRY_RUN else 'DISABLED'}")
# print("="*60)

# if DRY_RUN:
#     print("\n⚠ DRY RUN MODE - No images will actually be sent")

# # Small delay before starting
# time.sleep(2)


# # ============================================================
# # CHUNK 18: MAIN LOOP - PROCESS ALL CONTACTS
# # ============================================================

# logging.info("\n" + "="*60)
# logging.info("STARTING IMAGE SENDING PROCESS")
# logging.info("="*60 + "\n")

# # Counters for tracking
# successful_sends = 0
# failed_sends = 0
# skipped_contacts = 0

# # Process contacts with progress bar
# for index, contact in enumerate(tqdm(pending_contacts, desc="Processing", unit="contact"), 1):
    
#     # Display contact info
#     print(f"\n{'='*60}")
#     print(f"[{index}/{len(pending_contacts)}] Contact: {contact}")
#     print('='*60)
    
#     # Check WhatsApp health before processing
#     if not check_whatsapp_health(driver, wait):
#         logging.error("WhatsApp is not responsive! Stopping...")
#         print("\n⚠ WhatsApp disconnected. Please check and restart script.")
#         break
    
#     # Step 1: Search and open contact
#     if search_and_open_contact(contact, wait, driver):
        
#         # Step 2: Send all images
#         if send_images_to_contact(contact, images_to_send, wait, driver):
#             successful_sends += 1
            
#             # Mark as sent (only if not dry run)
#             if not DRY_RUN:
#                 mark_as_sent(contact)
#         else:
#             failed_sends += 1
        
#         # Step 3: Clear search box
#         clear_search_box(wait, driver)
        
#         # Delay before next contact
#         if index < len(pending_contacts):
#             logging.info(f"Waiting {delay_between_contacts}s before next contact...")
#             human_delay(delay_between_contacts, delay_between_contacts + 0.5)
#     else:
#         # Contact not found
#         failed_sends += 1
#         clear_search_box(wait, driver)
    
#     # Batch break after every batch_size contacts
#     if index % batch_size == 0 and index < len(pending_contacts):
#         print(f"\n{'⏸'*30}")
#         print(f"BATCH BREAK - Processed {index}/{len(pending_contacts)} contacts")
#         print(f"Taking {batch_break_duration}s break...")
#         print('⏸'*30)
#         logging.info(f"Batch break: {batch_break_duration}s")
#         time.sleep(batch_break_duration)


# # ============================================================
# # CHUNK 19: FINAL SUMMARY AND REPORT
# # ============================================================

# print("\n\n" + "="*60)
# print("PROCESS COMPLETED!")
# print("="*60)

# # Calculate statistics
# total_processed = successful_sends + failed_sends
# success_rate = (successful_sends / total_processed * 100) if total_processed > 0 else 0

# print(f"\n📊 Statistics:")
# print(f"  ✓ Successful: {successful_sends}")
# print(f"  ❌ Failed: {failed_sends}")
# print(f"  📈 Success Rate: {success_rate:.1f}%")
# print(f"  📁 Images per contact: {len(images_to_send)}")
# print(f"  📦 Total images sent: {successful_sends * len(images_to_send)}")

# if DRY_RUN:
#     print(f"\n⚠ Note: This was a DRY RUN - no images were actually sent")

# print("="*60)

# # Log final summary
# logging.info("="*60)
# logging.info("FINAL SUMMARY")
# logging.info("="*60)
# logging.info(f"Successful: {successful_sends}")
# logging.info(f"Failed: {failed_sends}")
# logging.info(f"Success Rate: {success_rate:.1f}%")
# logging.info(f"Log file: {log_filename}")
# logging.info("="*60)


# # ============================================================
# # CHUNK 20: KEEP BROWSER OPEN INDEFINITELY
# # ============================================================

# print("\n" + "🌐"*30)
# print("Browser will remain open")
# print("You can continue using WhatsApp manually")
# print("Close browser window to terminate script")
# print("🌐"*30 + "\n")

# logging.info("Script finished - Browser remains open")

# # Infinite loop to keep script running
# try:
#     while True:
#         time.sleep(1)  # Reduce CPU usage
#         driver.current_url  # Check if browser still open
# except Exception:
#     # Browser was closed
#     print("\n✓ Browser closed. Script terminated.")
#     logging.info("Browser closed - Script terminated")





















# ============================================================
# CHUNK 1: IMPORT REQUIRED LIBRARIES
# ============================================================

# Selenium webdriver - main library for browser automation
from selenium import webdriver

# For locating elements on webpage (by XPath, ID, etc.)
from selenium.webdriver.common.by import By

# For keyboard actions like pressing ENTER
from selenium.webdriver.common.keys import Keys

# For setting up Chrome driver service
from selenium.webdriver.chrome.service import Service

# For configuring Chrome browser options (like saving session)
from selenium.webdriver.chrome.options import Options

# For dynamic waits - waits until element appears (better than time.sleep)
from selenium.webdriver.support.ui import WebDriverWait

# For wait conditions like "element is present", "element is clickable"
from selenium.webdriver.support import expected_conditions as EC

# For auto-downloading and managing Chrome driver
from webdriver_manager.chrome import ChromeDriverManager

# For handling file and folder paths
import os

# For adding delays and timestamps
import time
from datetime import datetime

# For logging system
import logging

# For configuration file handling
import json

# For random delays (human-like behavior)
import random

# For image validation
from PIL import Image

# For graceful shutdown handling
import signal
import sys

# For progress bar
from tqdm import tqdm


# ============================================================
# CHUNK 2: LOGGING SETUP
# ============================================================

# Create logs folder if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Create log filename with timestamp
log_filename = f"logs/whatsapp_bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Configure logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),  # Save to file
        logging.StreamHandler()  # Also print to console
    ]
)

logging.info("="*60)
logging.info("WhatsApp Image Sender Bot Started")
logging.info("="*60)


# ============================================================
# CHUNK 3: CONFIGURATION FILE LOADING
# ============================================================

# Default configuration
DEFAULT_CONFIG = {
    "contacts": ["Sami Kareem", "Madni Korejo"],
    "images_folder": '/Users/samikareem/Desktop/wolf_images',
    "max_wait_time": 30,
    "delay_between_contacts": 2,
    "delay_between_images": 1,
    "max_retry_attempts": 3,
    "batch_size": 5,
    "batch_break_duration": 60,
    "dry_run": False
}

# Configuration file path
config_file = "config.json"

# Load or create configuration file
if os.path.exists(config_file):
    logging.info(f"Loading configuration from {config_file}")
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    logging.info("✓ Configuration loaded successfully")
else:
    logging.warning(f"Configuration file not found. Creating default config.json")
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)
    config = DEFAULT_CONFIG
    logging.info(f"✓ Created {config_file} - Please edit it with your settings")

# Extract configuration values
contacts_list = config.get('contacts', DEFAULT_CONFIG['contacts'])
images_folder_path = config.get('images_folder', DEFAULT_CONFIG['images_folder'])
max_wait_time = config.get('max_wait_time', DEFAULT_CONFIG['max_wait_time'])
delay_between_contacts = config.get('delay_between_contacts', DEFAULT_CONFIG['delay_between_contacts'])
delay_between_images = config.get('delay_between_images', DEFAULT_CONFIG['delay_between_images'])
max_retry_attempts = config.get('max_retry_attempts', DEFAULT_CONFIG['max_retry_attempts'])
batch_size = config.get('batch_size', DEFAULT_CONFIG['batch_size'])
batch_break_duration = config.get('batch_break_duration', DEFAULT_CONFIG['batch_break_duration'])
DRY_RUN = config.get('dry_run', DEFAULT_CONFIG['dry_run'])


# ============================================================
# CHUNK 4: XPATHS - CORRECTED AND SIMPLIFIED
# ============================================================

# XPath for WhatsApp Web search box (top left, to search contacts)
XPATH_SEARCH_BOX = '//div[@aria-label="Search input textbox"]'

# XPath for contact name in search results
# {CONTACT_NAME} will be replaced dynamically in the code
XPATH_CONTACT_IN_RESULTS = '//span[@title="{CONTACT_NAME}"]'

# XPath for attachment button (paperclip icon in chat)
#XPATH_ATTACHMENT_BUTTON = '//div[@title="Attach"]'
XPATH_ATTACHMENT_BUTTON = '//button[@aria-label="Attach" and @data-tab="10"]'

# XPath for "Photos & videos" button in attachment menu
XPATH_PHOTOS_VIDEOS_BUTTON = '//span[text()="Photos & videos"]'

# XPath for file input element (accepts files)
XPATH_IMAGE_VIDEO_INPUT = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'

# XPath for send button (green arrow after selecting image)
#XPATH_SEND_BUTTON = '//span[@data-icon="send"]'

XPATH_SEND_BUTTON = '//div[@role="button"][@aria-label="Send"]'

# ============================================================
# CHUNK 5: SENT CONTACTS TRACKING SYSTEM
# ============================================================

# File to track which contacts have already received images
sent_contacts_file = "sent_contacts.txt"

def mark_as_sent(contact_name):
    """
    Mark a contact as already sent by adding to tracking file
    This prevents duplicate sends if script is rerun
    """
    with open(sent_contacts_file, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{contact_name}|{timestamp}\n")
    logging.info(f"Marked as sent: {contact_name}")

def is_already_sent(contact_name):
    """
    Check if contact has already received images
    Returns True if found in tracking file, False otherwise
    """
    if not os.path.exists(sent_contacts_file):
        return False
    
    with open(sent_contacts_file, 'r', encoding='utf-8') as f:
        sent_contacts = [line.split('|')[0] for line in f.read().splitlines()]
    
    return contact_name in sent_contacts

def get_sent_contacts_list():
    """
    Get list of all contacts that already received images
    """
    if not os.path.exists(sent_contacts_file):
        return []
    
    with open(sent_contacts_file, 'r', encoding='utf-8') as f:
        return [line.split('|')[0] for line in f.read().splitlines()]


# ============================================================
# CHUNK 6: UTILITY FUNCTIONS
# ============================================================

def human_delay(min_sec=1, max_sec=3):
    """
    Random delay to simulate human behavior and avoid detection
    Uses random time between min_sec and max_sec
    """
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def take_error_screenshot(driver, contact_name="unknown"):
    """
    Takes screenshot when error occurs for debugging
    Saves in screenshots folder with timestamp
    """
    # Create screenshots folder if doesn't exist
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"screenshots/error_{contact_name}_{timestamp}.png"
    
    try:
        driver.save_screenshot(filename)
        logging.info(f"Screenshot saved: {filename}")
    except Exception as e:
        logging.error(f"Failed to take screenshot: {str(e)}")

def signal_handler(sig, frame):
    """
    Handle Ctrl+C gracefully - saves progress and exits cleanly
    """
    print("\n\n" + "⚠"*30)
    print("INTERRUPT RECEIVED - SHUTTING DOWN GRACEFULLY")
    print("⚠"*30)
    logging.warning("Script interrupted by user (Ctrl+C)")
    
    print("\n✓ Progress has been saved")
    print("✓ You can resume by running the script again")
    print("✓ Goodbye!\n")
    
    sys.exit(0)

# Register signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)


# ============================================================
# CHUNK 7: IMAGE VALIDATION FUNCTION
# ============================================================

def validate_image(image_path):
    """
    Validates if image file is not corrupted and can be opened
    Returns True if valid, False if corrupted or invalid
    """
    try:
        # Try to open and verify image
        img = Image.open(image_path)
        img.verify()  # Verify image integrity
        
        # Check file size (optional - skip very large files)
        file_size_mb = os.path.getsize(image_path) / (1024 * 1024)
        if file_size_mb > 50:  # WhatsApp has ~16MB limit, but we use 50MB as safe limit
            logging.warning(f"Image too large ({file_size_mb:.2f}MB): {os.path.basename(image_path)}")
            return False
        
        return True
    except Exception as e:
        logging.error(f"Invalid image {os.path.basename(image_path)}: {str(e)}")
        return False


# ============================================================
# CHUNK 8: GET IMAGES FROM FOLDER
# ============================================================

def get_images_from_folder(folder_path):
    """
    Reads all valid image files from the specified folder
    Returns a list of full file paths for each valid image
    Only includes images that pass validation
    """
    # List to store valid image file paths
    image_files = []
    
    # Supported image formats
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        logging.error(f"Folder not found: {folder_path}")
        return image_files
    
    logging.info(f"Scanning folder for images: {folder_path}")
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Get file extension (e.g., .jpg)
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Check if file is an image
        if file_ext in image_extensions:
            # Create full path to image file
            full_path = os.path.join(folder_path, filename)
            
            # Validate image before adding
            if validate_image(full_path):
                image_files.append(full_path)
                logging.info(f"  ✓ Valid image: {filename}")
            else:
                logging.warning(f"  ✗ Skipped invalid image: {filename}")
    
    logging.info(f"Found {len(image_files)} valid image(s)")
    return image_files


# ============================================================
# CHUNK 9: WHATSAPP HEALTH CHECK
# ============================================================

def check_whatsapp_health(driver, wait_object):
    """
    Checks if WhatsApp Web is still loaded and responsive
    Returns True if healthy, False if disconnected or unresponsive
    """
    try:
        # Try to find search box - if found, WhatsApp is responsive
        wait_object.until(
            EC.presence_of_element_located((By.XPATH, XPATH_SEARCH_BOX))
        )
        return True
    except Exception as e:
        logging.error(f"WhatsApp health check failed: {str(e)}")
        take_error_screenshot(driver, "health_check_failed")
        return False


# ============================================================
# CHUNK 10: SEARCH AND OPEN CONTACT WITH RETRY - FIXED
# ============================================================

def search_and_open_contact(contact_name, wait_object, driver, attempt=1):
    """
    Searches for a contact and opens their chat
    Includes retry mechanism for reliability
    Returns True if successful, False if contact not found after all retries
    """
    try:
        logging.info(f"[Attempt {attempt}/{max_retry_attempts}] Searching for: {contact_name}")
        
        # Find the search box and wait for it to be clickable
        search_box = wait_object.until(
            EC.element_to_be_clickable((By.XPATH, XPATH_SEARCH_BOX))
        )
        
        # Click on search box to activate it
        search_box.click()
        human_delay(0.3, 0.5)
        
        # IMPORTANT: Clear search box FIRST (Mac uses COMMAND key)
        search_box.send_keys(Keys.COMMAND + "a")  # Select all
        search_box.send_keys(Keys.BACKSPACE)      # Delete
        human_delay(0.5, 1)
        
        # Type contact name in search box
        search_box.send_keys(contact_name)
        human_delay(2, 3)  # Wait LONGER for search results to appear
        
        # BUILD XPATH with actual contact name (replace placeholder)
        contact_xpath = XPATH_CONTACT_IN_RESULTS.replace("{CONTACT_NAME}", contact_name)
        logging.info(f"  Looking for XPath: {contact_xpath}")
        
        # Wait for search results and find the contact
        try:
            contact_element = wait_object.until(
                EC.element_to_be_clickable((By.XPATH, contact_xpath))
            )
            logging.info(f"  ✓ Found contact with exact match")
        except:
            # Fallback: Click first result if exact match fails
            logging.info(f"  Exact match failed, clicking first result...")
            contact_xpath = '//div[@role="listitem"][1]'
            contact_element = wait_object.until(
                EC.element_to_be_clickable((By.XPATH, contact_xpath))
            )
        
        # Click on the contact to open chat
        contact_element.click()
        human_delay(2, 3)  # Wait for chat to load
        
        logging.info(f"✓ Successfully opened chat: {contact_name}")
        return True
        
    except Exception as e:
        logging.error(f"Error searching for '{contact_name}': {str(e)}")
        take_error_screenshot(driver, contact_name)
        
        # Retry if attempts remaining
        if attempt < max_retry_attempts:
            logging.info(f"Retrying in 3 seconds...")
            time.sleep(3)
            
            # Clear search box before retry (Mac uses COMMAND)
            try:
                search_box = wait_object.until(
                    EC.element_to_be_clickable((By.XPATH, XPATH_SEARCH_BOX))
                )
                search_box.click()
                search_box.send_keys(Keys.COMMAND + "a")  # Changed from CONTROL
                search_box.send_keys(Keys.BACKSPACE)
            except:
                pass
            
            return search_and_open_contact(contact_name, wait_object, driver, attempt + 1)
        else:
            logging.error(f"Failed to find contact after {max_retry_attempts} attempts: {contact_name}")
            return False


# ============================================================
# CHUNK 11: SEND IMAGES WITH RETRY - FIXED
# ============================================================

def send_images_to_contact(contact_name, image_paths, wait_object, driver, attempt=1):
    """
    Sends all images from the list to the currently open chat
    Includes retry mechanism and dry run support
    Returns True if successful, False if failed after all retries
    """
    try:
        logging.info(f"Preparing to send {len(image_paths)} image(s) to {contact_name}")
        
        # DRY RUN MODE - simulate sending without actually sending
        if DRY_RUN:
            logging.info(f"[DRY RUN] Would send {len(image_paths)} images to {contact_name}")
            for idx, img_path in enumerate(image_paths, 1):
                logging.info(f"  [DRY RUN] Image {idx}: {os.path.basename(img_path)}")
            time.sleep(2)  # Simulate processing time
            return True
        
        # ACTUAL SENDING MODE
        # Loop through each image
        for idx, image_path in enumerate(image_paths, 1):
            logging.info(f"  → Sending image {idx}/{len(image_paths)}: {os.path.basename(image_path)}")
            
            # Wait for and click the attachment button (paperclip icon)
            attachment_button = wait_object.until(
                EC.element_to_be_clickable((By.XPATH, XPATH_ATTACHMENT_BUTTON))
            )
            attachment_button.click()
            human_delay(0.5, 1)
            
            # Click "Photos & videos" button first
            photos_button = wait_object.until(
                EC.element_to_be_clickable((By.XPATH, XPATH_PHOTOS_VIDEOS_BUTTON))
            )
            photos_button.click()
            human_delay(0.5, 1)
            
            # Wait for the file input element to appear
            file_input = wait_object.until(
                EC.presence_of_element_located((By.XPATH, XPATH_IMAGE_VIDEO_INPUT))
            )
            
            # Send the image file path to the input element
            file_input.send_keys(image_path)
            human_delay(2, 3)  # Wait for image to upload
            
            # Wait for the send button to appear and be clickable
            send_button = wait_object.until(
                EC.element_to_be_clickable((By.XPATH, XPATH_SEND_BUTTON))
            )
            
            # Click send button to send the image
            send_button.click()
            
            # Wait between images with human-like delay
            human_delay(delay_between_images, delay_between_images + 1)
            
            logging.info(f"  ✓ Image {idx} sent successfully")
        
        logging.info(f"✓ All {len(image_paths)} images sent to {contact_name}")
        return True
        
    except Exception as e:
        logging.error(f"Error sending images to '{contact_name}': {str(e)}")
        take_error_screenshot(driver, contact_name)
        
        # Retry if attempts remaining
        if attempt < max_retry_attempts:
            logging.info(f"Retrying in 3 seconds...")
            time.sleep(3)
            return send_images_to_contact(contact_name, image_paths, wait_object, driver, attempt + 1)
        else:
            logging.error(f"Failed to send images after {max_retry_attempts} attempts")
            return False


# ============================================================
# CHUNK 12: CLEAR SEARCH BOX - FIXED
# ============================================================

def clear_search_box(wait_object, driver):
    """
    Clears the search box to prepare for next contact search
    Includes error handling and retry
    Works on Mac (uses CMD instead of CTRL)
    """
    try:
        # Find the search box
        search_box = wait_object.until(
            EC.element_to_be_clickable((By.XPATH, XPATH_SEARCH_BOX))
        )
        
        # Click on search box
        search_box.click()
        human_delay(0.3, 0.5)
        
        # Select all text and delete it (Mac uses COMMAND)
        search_box.send_keys(Keys.COMMAND + "a")  # Changed from CONTROL
        search_box.send_keys(Keys.BACKSPACE)
        
        # Press ESC to close search results
        search_box.send_keys(Keys.ESCAPE)
        human_delay(0.3, 0.5)
        
        logging.info("✓ Search box cleared")
        return True
        
    except Exception as e:
        logging.warning(f"Could not clear search box: {str(e)}")
        return False


# ============================================================
# CHUNK 13: CHROME SETUP WITH PERSISTENT SESSION - FIXED
# ============================================================

logging.info("="*60)
logging.info("Setting up Chrome browser with persistent session...")
logging.info("="*60)

# Create Chrome options object to customize browser behavior
chrome_options = Options()

# TEMPORARILY DISABLE session saving to fix Chrome crash
# Uncomment these lines once everything works to enable session saving
user_data_dir = os.path.join(os.getcwd(), "whatsapp_session")
chrome_options.add_argument(f"user-data-dir={user_data_dir}")

# Mac-specific: Disable sandbox
chrome_options.add_argument("--no-sandbox")

# Disable automation flags
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Initialize Chrome driver with custom options
try:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    logging.info("✓ Chrome browser opened successfully")
except Exception as e:
    logging.error(f"Failed to initialize Chrome: {str(e)}")
    sys.exit(1)

# Maximize browser window
driver.maximize_window()


# ============================================================
# CHUNK 14: OPEN WHATSAPP WEB AND LOGIN
# ============================================================

logging.info("\nOpening WhatsApp Web...")

# Navigate to WhatsApp Web
driver.get("https://web.whatsapp.com")

# Create WebDriverWait object for dynamic waiting
wait = WebDriverWait(driver, max_wait_time)

try:
    # Try to find search box (means already logged in)
    logging.info("Checking login status...")
    search_box = wait.until(
        EC.presence_of_element_located((By.XPATH, XPATH_SEARCH_BOX))
    )
    logging.info("✓ Already logged in! Session restored successfully")
    
except:
    # Search box not found - first time login needed
    logging.warning("First time login detected")
    print("\n" + "⚠"*30)
    print("PLEASE SCAN QR CODE WITH YOUR PHONE NOW")
    print("⚠"*30 + "\n")
    
    # Wait for user to scan QR code
    search_box = wait.until(
        EC.presence_of_element_located((By.XPATH, XPATH_SEARCH_BOX))
    )
    logging.info("✓ Login successful! Session saved for future use")

logging.info("✓ WhatsApp Web is ready!\n")
time.sleep(2)


# ============================================================
# CHUNK 15: LOAD IMAGES FROM FOLDER
# ============================================================

logging.info("="*60)
logging.info("LOADING IMAGES")
logging.info("="*60)

# Get all valid images from folder
images_to_send = get_images_from_folder(images_folder_path)

# Check if any images found
if len(images_to_send) == 0:
    logging.error("No valid images found in folder!")
    logging.error(f"Please check the path: {images_folder_path}")
    print("\n" + "❌"*30)
    print("NO IMAGES FOUND - CANNOT PROCEED")
    print("❌"*30)
    print(f"\nPlease:")
    print(f"1. Check the folder path in config.json")
    print(f"2. Ensure images exist in the folder")
    print(f"3. Run the script again")
    print("\nBrowser will remain open for inspection...")
    
    # Keep browser open
    try:
        while True:
            time.sleep(1)
            driver.current_url
    except:
        logging.info("Browser closed")
    
    sys.exit(1)


# ============================================================
# CHUNK 16: PREPARE CONTACTS LIST (SKIP ALREADY SENT)
# ============================================================

logging.info("="*60)
logging.info("PREPARING CONTACTS LIST")
logging.info("="*60)

# Get list of contacts already sent
already_sent = get_sent_contacts_list()

if already_sent:
    logging.info(f"Found {len(already_sent)} contact(s) already sent:")
    for contact in already_sent:
        logging.info(f"  - {contact}")

# Filter out already sent contacts
pending_contacts = [c for c in contacts_list if not is_already_sent(c)]

if not pending_contacts:
    logging.info("\n" + "✓"*30)
    logging.info("ALL CONTACTS ALREADY RECEIVED IMAGES!")
    logging.info("✓"*30)
    print("\nNothing to do. All contacts in list have already been sent images.")
    print("To resend, delete or rename 'sent_contacts.txt' file.")
    
    # Keep browser open
    print("\nBrowser will remain open...")
    try:
        while True:
            time.sleep(1)
            driver.current_url
    except:
        logging.info("Browser closed")
    
    sys.exit(0)

logging.info(f"\n✓ {len(pending_contacts)} contact(s) pending:")
for contact in pending_contacts:
    logging.info(f"  - {contact}")


# ============================================================
# CHUNK 17: DISPLAY PRE-RUN SUMMARY
# ============================================================

print("\n" + "="*60)
print("PRE-RUN SUMMARY")
print("="*60)
print(f"Images to send: {len(images_to_send)}")
print(f"Total contacts: {len(contacts_list)}")
print(f"Already sent: {len(already_sent)}")
print(f"Pending contacts: {len(pending_contacts)}")
print(f"Batch size: {batch_size} contacts per batch")
print(f"Dry run mode: {'ENABLED' if DRY_RUN else 'DISABLED'}")
print("="*60)

if DRY_RUN:
    print("\n⚠ DRY RUN MODE - No images will actually be sent")

# Small delay before starting
time.sleep(2)


# ============================================================
# CHUNK 18: MAIN LOOP - PROCESS ALL CONTACTS
# ============================================================

logging.info("\n" + "="*60)
logging.info("STARTING IMAGE SENDING PROCESS")
logging.info("="*60 + "\n")

# Counters for tracking
successful_sends = 0
failed_sends = 0
skipped_contacts = 0

# Process contacts with progress bar
for index, contact in enumerate(tqdm(pending_contacts, desc="Processing", unit="contact"), 1):
    
    # Display contact info
    print(f"\n{'='*60}")
    print(f"[{index}/{len(pending_contacts)}] Contact: {contact}")
    print('='*60)
    
    # Check WhatsApp health before processing
    if not check_whatsapp_health(driver, wait):
        logging.error("WhatsApp is not responsive! Stopping...")
        print("\n⚠ WhatsApp disconnected. Please check and restart script.")
        break
    
    # Step 1: Search and open contact
    if search_and_open_contact(contact, wait, driver):
        
        # Step 2: Send all images
        if send_images_to_contact(contact, images_to_send, wait, driver):
            successful_sends += 1
            
            # Mark as sent (only if not dry run)
            if not DRY_RUN:
                mark_as_sent(contact)
        else:
            failed_sends += 1
        
        # Step 3: Clear search box
        clear_search_box(wait, driver)
        
        # Delay before next contact
        if index < len(pending_contacts):
            logging.info(f"Waiting {delay_between_contacts}s before next contact...")
            human_delay(delay_between_contacts, delay_between_contacts + 0.5)
    else:
        # Contact not found
        failed_sends += 1
        clear_search_box(wait, driver)
    
    # Batch break after every batch_size contacts
    if index % batch_size == 0 and index < len(pending_contacts):
        print(f"\n{'⏸'*30}")
        print(f"BATCH BREAK - Processed {index}/{len(pending_contacts)} contacts")
        print(f"Taking {batch_break_duration}s break...")
        print('⏸'*30)
        logging.info(f"Batch break: {batch_break_duration}s")
        time.sleep(batch_break_duration)


# ============================================================
# CHUNK 19: FINAL SUMMARY AND REPORT
# ============================================================

print("\n\n" + "="*60)
print("PROCESS COMPLETED!")
print("="*60)

# Calculate statistics
total_processed = successful_sends + failed_sends
success_rate = (successful_sends / total_processed * 100) if total_processed > 0 else 0

print(f"\n📊 Statistics:")
print(f"  ✓ Successful: {successful_sends}")
print(f"  ❌ Failed: {failed_sends}")
print(f"  📈 Success Rate: {success_rate:.1f}%")
print(f"  📁 Images per contact: {len(images_to_send)}")
print(f"  📦 Total images sent: {successful_sends * len(images_to_send)}")

if DRY_RUN:
    print(f"\n⚠ Note: This was a DRY RUN - no images were actually sent")

print("="*60)

# Log final summary
logging.info("="*60)
logging.info("FINAL SUMMARY")
logging.info("="*60)
logging.info(f"Successful: {successful_sends}")
logging.info(f"Failed: {failed_sends}")
logging.info(f"Success Rate: {success_rate:.1f}%")
logging.info(f"Log file: {log_filename}")
logging.info("="*60)


# ============================================================
# CHUNK 20: KEEP BROWSER OPEN INDEFINITELY
# ============================================================

print("\n" + "🌐"*30)
print("Browser will remain open")
print("You can continue using WhatsApp manually")
print("Close browser window to terminate script")
print("🌐"*30 + "\n")

logging.info("Script finished - Browser remains open")

# Infinite loop to keep script running
try:
    while True:
        time.sleep(1)  # Reduce CPU usage
        driver.current_url  # Check if browser still open
except Exception:
    # Browser was closed
    print("\n✓ Browser closed. Script terminated.")
    logging.info("Browser closed - Script terminated")