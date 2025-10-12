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
inventory_info = wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "Inventory Info"))
)
ActionChains(driver).move_to_element(inventory_info).perform()
time.sleep(2)  # give some time for the submenu to appear

# Click after hovering
inventory_info.click()
print("Inventory Info hovered and clicked successfully!")

# Click on “Product Master” link
product_master_link = wait.until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/vendor-master/product')]"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_master_link)
time.sleep(2)
driver.execute_script("arguments[0].click();", product_master_link)
print("Product Master clicked successfully!")

# Click on “Add Product” button
add_product_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Product')]"))
)
add_product_btn.click()
print("Add Product button clicked successfully!")

# Wait for the "Add Product" label
add_product_label = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Add Product')]"))
)
print("Add Product label is visible")
time.sleep(1)
add_product_label.click()
print("Add Product label clicked successfully!")

# Wait for the item group input box
item_group_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='-- Press Enter For Item Group --']"))
)
item_group_input.send_keys(Keys.ENTER)
time.sleep(1)

# Wait for the ng-select dropdown
ng_select_box = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ng-select[@bindlabel='DESCA']"))
)
ng_select_box.click()
print("ng-select box clicked successfully!")

# Select the option
wait = WebDriverWait(driver, 10)
ims8_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='IMS8']")))
ims8_option.click()
print("option selected successfully!")

# Click OK button
ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Ok')]]"))
)
ok_button.click()
print("OK button clicked successfully!")

# Wait for the "Enter Item Code" input box to be visible
item_code_input = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Item Code']"))
)
item_code_input.send_keys("ITEM12234")
print("Item Code entered successfully!")

# Wait for the "Enter Item Name" input box
item_name_input = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Item Name']"))
)
item_name_input.send_keys("Tesst Producttts")
print("Item Name entered successfully!")

# Wait for the "Enter HS Code" input box
hs_code_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter HS Code']"))
)
hs_code_input.send_keys("12345")
print("HS Code entered successfully!")

# Wait until the Stock Unit is visible
unit_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//select[@id='unit']"))
)
unit_dropdown.click()
print("Unit dropdown clicked successfully!")

stock = Select(unit_dropdown)

stock.select_by_visible_text("Pcs.")
print("Stock Unit selected successfully!")

# Wait for the "Enter Product Description" input box
description_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Product Description']"))
)
description_input.send_keys("This is a test product description.")
print("Product Description entered successfully!")

# Wait for the "Enter Short Name" input box
short_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Short Name']"))
)
short_name.send_keys("TestProd")
print("Short Name entered successfully!")

category_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@id='Category']"))
)
select_category = Select(category_dropdown)
select_category.select_by_visible_text("N/A")
print("Category selected successfully!")

purchase_price = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Purchase Price']"))
)
purchase_price.send_keys("100")
print("Purchase Price entered successfully!")

# Wait for the input field to appear
select_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Press Enter to select']"))
)

# Click the input field (since it is read-only, we simulate a click or press Enter)
select_input.send_keys(Keys.ENTER)
print("Triggered dropdown selection successfully!")
time.sleep(5)

# Wait for the cell with text "ABC Camp 2" to appear and be clickable
supplier = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//td[contains(@class,'mat-column-ACNAME') and normalize-space(text())='ABC Camp 2']"))
)

# Click the cell
actions = ActionChains(driver)
actions.double_click(supplier).perform()
print("Supplier selected successfully!")

# Wait for the Sales Price input box
sales_price = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='number' and @placeholder='0']"))
)  
sales_price.send_keys("150")
print("Sales Price entered successfully!")

# Wait for the SAVE button to be clickable
save_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='save' and text()='SAVE']"))
)

# Click the SAVE button
save_button.click()
print("SAVE button clicked successfully!")

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert

# Print the alert text (optional)
print("Alert says:", alert.text)

# Alert handling
#alert.accept()  # If you want to click "OK"
alert.dismiss()  # If you want to click "Cancel"

# Wait for user input before closing the browser
print("Press 'Enter' to close the browser.")
keyboard.wait('enter')
driver.quit()