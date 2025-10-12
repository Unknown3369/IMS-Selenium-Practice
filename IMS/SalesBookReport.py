from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import keyboard
import time

# Set up Microsoft Edge with Chromium options
options = Options()
options.use_chromium = True
driver = webdriver.Edge(options=options)
driver.maximize_window()

# Open the login page
driver.get("https://grn.variantqa.himshang.com.np/#/login")

wait = WebDriverWait(driver, 10)
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

# Click on “Reports” menu
reports = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Reports')]"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", reports)
time.sleep(1)
driver.execute_script("arguments[0].click();", reports)
print("Reports clicked successfully!")
time.sleep(5)

# Hover over "Sales Report" before clicking
sales_report = wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "Sales Report"))
)
ActionChains(driver).move_to_element(sales_report).perform()
time.sleep(2)  # give some time for the submenu to appear

# Click after hovering
sales_report.click()
print("Sales Report hovered and clicked successfully!")

# Click on “Sales Book Report” link
sales_book_report = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Sales Book Report']"))
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sales_book_report)
time.sleep(2)
driver.execute_script("arguments[0].click();", sales_book_report)
print("Sales Book Report clicked successfully!")
time.sleep(5)

#Branch Selection
branch_dropdown = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[contains(@class, 'form-control') and contains(@class, 'selectText')]"))
)
branch_dropdown.click()
time.sleep(2)
select_branch = Select(branch_dropdown)
time.sleep(1)
select_branch.select_by_visible_text("ALL")
select_branch_click = ActionChains(driver)
select_branch_click.double_click(branch_dropdown).perform()
print("Branch selected successfully!")

# Select Cost Center from dropdown 
cost_center_dropdown = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[contains(@class, 'form-control') and contains(@class, 'input-text')]"))
)
select_cost_center = Select(cost_center_dropdown)
select_cost_center.select_by_visible_text("Test QA")
print("Cost Center selected successfully!")

#Select All user
user_dropdown = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @value='0']"))
)
user_dropdown.click()
print("All users selected successfully!")

#Customer Selection
select_customer = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @placeholder='Press Enter or Tab for Account List']"))
)
select_customer.send_keys(Keys.ENTER)
time.sleep(0.5)

select_customer_list = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[normalize-space(text())='Ajay Pradhan,']"))
)
select_customer_click = ActionChains(driver)
select_customer_click.double_click(select_customer_list).perform()
print("Customer selected successfully!")

# Click on the "Run" button
run_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='RUN']"))
)
run_button.click()
print("Run button clicked successfully!")

#load Report
load_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='option-card' and .//span[normalize-space()='Load Report']]"))
)
load_button.click()
print("Load Report clicked successfully!")

# Wait for user input before closing the browser
print("Press 'Enter' to close the browser.")
keyboard.wait('enter')
driver.quit()