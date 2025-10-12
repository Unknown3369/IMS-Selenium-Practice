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
import random

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

# Click on “Transactions” menu
transactions = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Transactions')]"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", transactions)
time.sleep(1)
driver.execute_script("arguments[0].click();", transactions)
print("Transactions clicked successfully!")

# Hover over "Inventory Info" before clicking
purchase_transaction = wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "Purchase Transaction"))
)
ActionChains(driver).move_to_element(purchase_transaction).perform()
time.sleep(2)  # give some time for the submenu to appear

# Click after hovering
purchase_transaction.click()
print("Purchase Transaction hovered and clicked successfully!")

# Click on “Product Invoice” link
purchase_invoice_link = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Purchase Invoice']"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", purchase_invoice_link)
time.sleep(2)
driver.execute_script("arguments[0].click();", purchase_invoice_link)
print("Purchase Invoice clicked successfully!")

# add invoice no
random_num = random.randint(10000, 99999)
invoice_value = f"PI-{random_num}"

invoice_no = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='invoiceNO']"))
)
invoice_no.send_keys(invoice_value)
print(f"Invoice No '{invoice_value}' entered successfully!")

# Select Vendor
account = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='accountfield']"))
)
account.click()
account.send_keys(Keys.ENTER)
time.sleep(5)
print("Account field clicked successfully!")

# Select account name
account_name = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@title='PAGRN153' and normalize-space()='PAGRN153']"))
)
actions = ActionChains(driver)
actions.double_click(account_name).perform()
print("Account name selected successfully!")
time.sleep(2)

# Click on item name field
item_name = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='ITEMDESC0']"))
)
item_name.send_keys(Keys.ENTER)
time.sleep(2)
print("Item name field clicked successfully!")

# Select item from the dropdown
select_item = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[normalize-space(text())='Helmet nepal']"))
)
actions = ActionChains(driver)
actions.double_click(select_item).perform()
print("Item selected successfully!")
time.sleep(4)

#add unit
unit = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='ALTUNIT0']"))
)
unit.send_keys(Keys.ENTER)
print("Unit selected successfully!")

#add quantity
quantity = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='ALTERNATEQUANTIY0']"))
)
quantity.send_keys("10")
quantity.send_keys(Keys.ENTER)
print("Quantity entered successfully!")

save_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'SAVE')]"))
)
save_button.click()
print("Save button clicked successfully!")

#Alert handling
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert

# Print the alert text (optional)
print("Alert says:", alert.text)

# Alert handling
alert.accept()  # If you want to click "OK"
#alert.dismiss()  # If you want to click "Cancel"

# Wait for user input before closing the browser
print("Press 'Enter' to close the browser.")
keyboard.wait('enter')
driver.quit()