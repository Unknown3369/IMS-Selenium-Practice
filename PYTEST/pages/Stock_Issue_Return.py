import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# noinspection PyBroadException
@allure.feature("Stock Issue Return")
class StockIssueReturnPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    # noinspection PyBroadException
    @allure.step("Generate Stock Issue Return")
    def generate_stock_issue_return(self):

        transaction_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Transactions']"))
        )
        transaction_btn.click()
        time.sleep(1)

        try:
            inventory_movement = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Inventory Movement"))
            )
        except:
            inventory_movement = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//span[normalize-space()='Inventory Movement']")
                )
            )

        ActionChains(self.driver).move_to_element(inventory_movement).pause(0.3).perform()
        time.sleep(2)

        stock_issue_return = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Stock Issue Return"))
        )
        stock_issue_return.click()
        print("Stock Issue page opened.")
        time.sleep(2)

        # STEP 2: Select From Warehouse (FIRST DROPDOWN)

        from_wh = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='stockissueFromWH']"))
        )
        from_wh.click()
        time.sleep(1)

        test_wh = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//select[@id='stockissueFromWH']/option[normalize-space()='IMS Warehouse']")
            )
        )
        test_wh.click()
        print("Selected From Warehouse: IMS Warehouse")
        time.sleep(2)

        r_field = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//textarea"))
        )
        r_field.click()
        r_field.send_keys("Stock Issue Automation Entry")
        print("Remark added.")
        time.sleep(1)

        # STEP 4: Select To Warehouse
        print("Selecting To Warehouse...")

        # Click the SECOND dropdown (To Warehouse)
        to_wh = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//select[@style='width: 70%;' and contains(@class,'ng-valid')])[2]")
            )
        )
        to_wh.click()
        time.sleep(2)

        # Select "Main Warehouse" from second dropdown
        main_wh_2 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"(//select[@style='width: 70%;' and contains(@class,'ng-valid')])[2]/option[contains(text(),'Main Warehouse')]")
            )
        )
        main_wh_2.click()
        print("Selected To Warehouse: Main Warehouse")
        time.sleep(2)

        # Click on the reference field
        ref_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "soNoId"))
        )
        ref_field.click()
        time.sleep(1)

        # Press Enter to load reference list
        ref_field.send_keys(Keys.ENTER)
        print("Loading reference list...")
        time.sleep(2)

        # Wait for reference list to appear
        ref_item = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@title='IS15-STC-82/83']") 
            )
        )

        # Double-click the reference
        print("Double clicking reference number...")
        self.actions.double_click(ref_item).perform()
        time.sleep(2)
        print("Reference Number selected.")

        # STEP 6: Click Save
        print("Saving Stock Issue Return...")
        save_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='SAVE [End]']")
            )
        )
        save_btn.click()
        time.sleep(3)

        # Handle confirmation popup if it appears
        try:
            ok_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='OK']")
                )
            )
            ok_btn.click()
            print("Save confirmation clicked.")
        except:
            print("No confirmation popup appeared.")

        print("Stock Issue Return generated successfully!")

