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
sales_transaction = wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "Sales Transaction"))
)
ActionChains(driver).move_to_element(sales_transaction).perform()
time.sleep(2)  # give some time for the submenu to appear

# Click after hovering
sales_transaction.click()
print("Sales Transaction hovered and clicked successfully!")

# Click on “Sales Invoice” link
sales_invoice_link = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Sales Tax Invoice']"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sales_invoice_link)
time.sleep(2)
driver.execute_script("arguments[0].click();", sales_invoice_link)
print("Purchase Invoice clicked successfully!")

# Add Details in Sales Invoice Form
# add reference no
random_num = random.randint(10000, 99999)
ref_value = f"Ref-{random_num}"

refno = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='refnoInput']"))
)
refno.send_keys("ref_value")
print(f"Reference No '{ref_value}' entered successfully!")

# Select Cost Center
cost_center = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='costCenter']"))
)
time.sleep(3)
select = Select(cost_center)
select.select_by_visible_text("Test QA")
print("Cost Center selected successfully!")

#enter customer details
customer_enter =wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='customerselectid']"))
)
customer_enter.send_keys(Keys.ENTER)
print("Clicked on Customer!")

#Customer Select
customer_select =wait.until(
    EC.presence_of_element_located((By.XPATH, "//td[@class='ng-star-inserted']/div[@title=' Bhim lama' and contains(text(), 'Bhim lama')]"))
)
actions = ActionChains(driver)
actions.double_click(customer_select).perform()
print("Customer selected successfully!")

#enter item details
item_enter = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='itemDesc0']"))
)  
item_enter.send_keys(Keys.ENTER)
print("Clicked on Item field!")

#Item Select
item_select = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@title='125 -3' and normalize-space(text())='125 -3']"))
)
dclick = ActionChains(driver)
dclick.double_click(item_select).perform()
print("Item selected successfully!")

unit_select = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='alternateunit0']"))
)
unit_select.send_keys(Keys.ENTER)
print("Unit selected successfully!")

#add quantity
quantity = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='alternateQty0']"))
)
quantity.send_keys("5")
time.sleep(2)
quantity.send_keys(Keys.ENTER)
print("Quantity entered successfully!")

# Click on Save button
save = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='SAVE [End]']"))
)
save.click()
print("Save button clicked successfully!")

# Click on Balance Amount button
amount_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Balance Amount']"))
)
amount_btn.click()
print("Balance Amount button clicked successfully!")

# Click on Add button
add_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Add']"))
)
add_button.click()
print("Add button clicked successfully!")

# Save the Sales Invoice
save_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@title='Save']"))
)
save_button.click()
print("Save button clicked successfully!")
time.sleep(15)

#print invoice 
print_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Print']"))
)
print_button.click()
print("Print button clicked successfully!")

# Wait for user input before closing the browser
print("Press 'Enter' to close the browser.")
keyboard.wait('enter')
driver.quit()