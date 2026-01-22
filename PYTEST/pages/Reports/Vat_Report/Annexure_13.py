import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# noinspection PyBroadException
@allure.feature("Annexure 13 Report")
class Annexure13ReportPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)
        self.actions = ActionChains(driver)

    @allure.step("Generate Annexure 13 Report")
    def generate_annexure_13_report(self):
        wait = self.wait
        driver = self.driver

        print("Starting Annexure 13 Report generation...")

        try:
            print("Navigating to Reports → VAT Report → Annexure 13...")
            reports_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(normalize-space(),'Reports')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", reports_btn)
            reports_btn.click()
            time.sleep(1)

            try:
                vat_report = wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "VAT Report"))
                )
            except:
                vat_report = wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='VAT Report']"))
                )

            driver.execute_script("arguments[0].scrollIntoView(true);", vat_report)
            self.actions.move_to_element(vat_report).pause(0.4).perform()
            print("Hovered over 'VAT Report'.")
            time.sleep(1)

            annexure_13_report = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Annexure 13 (Anusuchi 13)"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", annexure_13_report)
            annexure_13_report.click()
            print("Clicked 'Annexure 13'")
            time.sleep(2)

            run_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'confirm-btn') and text()='RUN']"))
            )
            run_btn.click()
            print("Clicked 'RUN' button")
            time.sleep(2)

            print("Verifying Annexure 13 Report table...")

            try:
                table = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//table[contains(@class,'table')]"))
                )
                rows = table.find_elements(By.XPATH, ".//tr")
                print(f"Annexure 13 Report loaded with {len(rows) - 1} rows.")

                # Screenshot when the table appears
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Annexure_13_Report_Table",
                    attachment_type=allure.attachment_type.PNG
                )
                print("Screenshot attached to Allure.")

            except TimeoutException:
                print("Table did NOT load — no rows found.")
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="Annexure_13_Report_No_Table",
                    attachment_type=allure.attachment_type.PNG
                )

            print("Annexure 13 Report generation completed successfully.")

        except Exception as e:
            print(f"Error occurred: {e}")
            # Screenshot on failure
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Annexure_13_Report_Error",
                attachment_type=allure.attachment_type.PNG
            )
            raise e
