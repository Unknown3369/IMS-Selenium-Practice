from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import keyboard
import time

# Set up Microsoft Edge with Chromium options
options = Options()
options.use_chromium = True
driver = webdriver.Edge(options=options)

# Open the login page
driver.get("https://grn.variantqa.himshang.com.np/#/login")

wait = WebDriverWait(driver, 25)

# Enter username
username_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
username_box.send_keys("Sagan2")

# Enter password
password_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
password_box.send_keys("Ims@1234")

# Click on Sign In button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]")))
login_button.click()
print("Login attempted successfully!")

try:
    logout_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Logout']]"))
    )
    # Click the Logout button
    logout_button.click()
    print("Logged out successfully.")

    ok_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and normalize-space(text())='OK']"))
    )
    ok_button.click()
    print("Clicked OK on the confirmation dialog.")

    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "btn-auth").click()
    print("Clicked on re-login button.")
except:
    print("Logout button not found.")

# Click on “Masters” menu
masters = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Masters')]"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", masters)
time.sleep(1)
driver.execute_script("arguments[0].click();", masters)
print("Masters clicked successfully!")

# Hover over "Inventory Info" before clicking
custom_info = wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "Customer & Vendor Info"))
)
ActionChains(driver).move_to_element(custom_info).perform()
time.sleep(1)  

custom_info.click()
print("Inventory Info hovered and clicked successfully!")



# Click on “Product Master” link
customer_master_link = wait.until(
    EC.presence_of_element_located((By.XPATH, "//a[@title='Customer Master']//span[normalize-space()='Customer Master']"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", customer_master_link)
time.sleep(2)
driver.execute_script("arguments[0].click();", customer_master_link)
print("Customer Master clicked successfully!")
time.sleep(5)

# Click on "Create Customer" button
create_customer = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='create' and normalize-space()='Create Customer']"))
)
create_customer.click()
print("Create Customer button clicked successfully!")

# Add Customer Details
# add customer name
customer_name = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='customerName' and @placeholder='Enter Name']"))
)
customer_name.send_keys("Customer0001")
print("Customer Name entered successfully!")

# add customer address
address = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='address' and @placeholder='Enter Address']"))
)
address.send_keys("Kathmandu")
print("Address entered successfully!")

# add customer contact
contact = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='Mobile' and @placeholder='Mobile']"))
)
contact.send_keys("9841234567")
print("Contact entered successfully!")

save_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='save' and text()='SAVE']"))
)
save_btn.click()
print("Save button clicked successfully!")




# Wait for user input before closing the browser
print("Press 'Enter' to close the browser.")
keyboard.wait('enter')
driver.quit()