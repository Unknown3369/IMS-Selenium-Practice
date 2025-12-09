import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# noinspection PyBroadException
@allure.feature("Credit Note Creation")
class CreditNotePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.actions = ActionChains(driver)

    @allure.step("Create Credit Note Entry")
    def create_credit_note(self):
        driver = self.driver
        wait = self.wait
        actions = self.actions

        try:
            # --- Navigate to Transactions → Sales Transaction → Credit Note (Sales Return) ---
            transaction_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Transactions']"))
            )
            driver.execute_script("arguments[0].click();", transaction_btn)
            print("Clicked on 'Transactions'")

            try:
                sales_transaction = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sales Transaction")))
            except:
                sales_transaction = wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Sales Transaction']"))
                )

            ActionChains(driver).move_to_element(sales_transaction).perform()
            time.sleep(1)

            credit_note = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Credit Note (Sales Return)")))
            driver.execute_script("arguments[0].click();", credit_note)
            print("Opened 'Credit Note (Sales Return)' page.")
            time.sleep(4)

            actions.move_by_offset(200, 0).click().perform()
            time.sleep(0.5)

            # Step 1: Click on Ref Bill No field — FIXED interception
            print("Clicking 'Ref Bill No' field...")
            ref_bill_field = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='refbill']"))
            )

            driver.execute_script("arguments[0].scrollIntoView(true);", ref_bill_field)
            time.sleep(3)

            try:
                ref_bill_field.click()
            except:
                try:
                    actions.move_to_element(ref_bill_field).pause(0.2).click().perform()
                except:
                    driver.execute_script("arguments[0].click();", ref_bill_field)

            print("Clicked Ref Bill field.")

            # Step 2: Press ENTER to load voucher list
            actions.send_keys("\ue007").perform()
            print("Pressed ENTER to load vouchers...")
            time.sleep(2)

            # Step 3: Double-click voucher
            print("Selecting a voucher from the list...")
            voucher_item = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@title='2025-12-08']")) #update this manually for now .
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", voucher_item)
            actions.double_click(voucher_item).perform()
            print("Voucher selected.")
            time.sleep(5)

            # Step 4: Enter Remarks
            print("Entering Remarks...")
            remarks_field = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//textarea[@id='remarksid']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", remarks_field)
            remarks_field.clear()
            remarks_field.send_keys("Credit note created for returned goods.")
            print("Remarks entered successfully.")
            time.sleep(2)

            # Step 5: Click SAVE button
            print("Clicking SAVE button...")
            save_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'SAVE')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
            driver.execute_script("arguments[0].click();", save_button)
            print("Clicked SAVE successfully.")
            time.sleep(2)

            # Screenshot
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="Credit_Note_Screenshot",
                attachment_type=allure.attachment_type.PNG)
            print("Screenshot saved.")

        except TimeoutException:
            print("Timeout waiting for element while generating Credit Note.")
            raise
        except Exception as e:
            print(f"Error while creating Credit Note: {e}")
            raise
