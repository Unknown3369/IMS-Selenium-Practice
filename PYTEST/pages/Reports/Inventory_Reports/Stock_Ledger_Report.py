import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# noinspection PyBroadException
@allure.feature("Stock Ledger Report")
class StockLedReportPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)
        self.actions = ActionChains(driver)

    @allure.step("Generate Stock Ledger Report for a selected warehouse and item")
    def generate_stock_ledger_report(self):
        wait = self.wait
        driver = self.driver

        print("Starting Stock Ledger Report generation...")

        try:
            reports_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(normalize-space(),'Reports')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", reports_btn)
            reports_btn.click()
            time.sleep(1)

            try:
                inventory_reports = wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Inventory Reports"))
                )
            except:
                inventory_reports = wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Inventory Reports']"))
                )

            driver.execute_script("arguments[0].scrollIntoView(true);", inventory_reports)
            self.actions.move_to_element(inventory_reports).pause(0.4).perform()
            print("Hovered over 'Inventory Reports'.")
            time.sleep(1)

            stock_led_report = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Stock Ledger Report"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", stock_led_report)
            stock_led_report.click()
            print("Clicked 'Stock Ledger Report'")
            time.sleep(2)

            warehouse_dropdown = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//select[contains(@class,'form-control')]"
            )))
            warehouse_dropdown.click()
            time.sleep(1)

            main_warehouse = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//option[contains(text(),'Main Warehouse')]"
            )))
            main_warehouse.click()
            print("Selected 'Main Warehouse'")
            time.sleep(1)

            item_input = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//input[@placeholder='Press Enter or Tab for Item List']"
            )))
            item_input.click()
            item_input.send_keys(Keys.ENTER)
            print("Opened Item List using ENTER key")
            time.sleep(2)

            white_chocolate = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[@title='Paras-200']"
            )))
            self.actions.double_click(white_chocolate).perform()
            print("Double-clicked item")
            time.sleep(1)

            run_btn = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[contains(text(),'RUN')]"
            )))
            run_btn.click()
            print("RUN clicked. Loading report...")
            time.sleep(3)

            try:
                table = wait.until(EC.presence_of_element_located((
                    By.XPATH, "//table[contains(@class,'table')]"
                )))

                rows = table.find_elements(By.XPATH, ".//tr")
                print(f"Stock Ledger Report loaded with {len(rows) - 1} data rows.")

                # Screenshot
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Stock_Ledger_Report_Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
                print("Screenshot attached to Allure.")

            except:
                print("No report table appeared.")

            print("Stock Ledger Report generated successfully.")

        except Exception as e:

            # Capture error screenshot
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Stock_Ledger_Report_Error",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                str(e),
                name="Error Details",
                attachment_type=allure.attachment_type.TEXT
            )

            raise AssertionError(f"Stock Ledger Report failed due to: {e}")
