import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


# noinspection PyBroadException
@allure.feature("Stock Issue Report")
class StockIssueReportPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)
        self.actions = ActionChains(driver)

    @allure.step("Generate Stock Issue Report for selected From and To Warehouses")
    def generate_stock_issue_report(self):
        driver = self.driver
        wait = self.wait

        print("Opening Stock Issue Report directly via URL...")

        try:
            time.sleep(5)
            # --- Step 1: Navigate directly to Stock Issue Report page ---
            driver.get("https://stc21.webredirect.himshang.com.np/#/pages/reports/stock-issue-report")

            # Wait for page to load (page-unique element)
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//h5[normalize-space()='Stock Issue Report']")
                )
            )
            print("Stock Issue Report page loaded.")

            # --- Step 2: Select From Warehouse ---
            # from_warehouse_dropdown = wait.until(
            #     EC.element_to_be_clickable((By.XPATH, "(//select[contains(@class,'form-control')])[2]"))
            # )
            # from_warehouse_dropdown.click()
            # time.sleep(2)
            # print("From Warehouse dropdown clicked")

            # from_warehouse = self.wait.until(
            #     EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Main Warehouse']"))
            # )
            # from_warehouse.click()

            # wait.until(EC.presence_of_element_located(
            #     (By.XPATH, "//div[contains(@class,'ng-dropdown-panel')]")
            # ))

            # option = wait.until(EC.element_to_be_clickable(
            #     (By.XPATH, "//div[contains(@class,'ng-option') and .//span[normalize-space()='Main Warehouse']]")
            # ))
            # driver.execute_script("arguments[0].click();", option)
            # Select(from_warehouse_dropdown).select_by_visible_text("Main Warehouse")
            # print("From Warehouse selected")
            # time.sleep(2)
            from_warehouse_select = self.wait.until(
                EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='From Warehouse:']/following::select[1]")
                )
            )
            select_from = Select(from_warehouse_select)
            time.sleep(2)

            # Debug: print all options (IMPORTANT)
            for opt in select_from.options:
                print(f"'{opt.text}'")

            select_from.select_by_visible_text("Main Warehouse")


            # --- Step 3: Select To Warehouse ---
            # to_warehouse_dropdown = self.wait.until(
            #     EC.element_to_be_clickable((By.XPATH, "(//select[contains(@class,'form-control')])[3]"))
            # )
            # to_warehouse_dropdown.click()
            # time.sleep(2)
            # print("To Warehouse dropdown clicked")

            # to_warehouse = wait.until(
            #     EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='IMS Warehouse']"))
            # )
            # # self.actions.move_to_element(to_warehouse).pause(0.5).double_click().perform()
            # to_warehouse.click()
            # print("To Warehouse selected")

            to_warehouse_select = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//label[normalize-space()='To Warehouse:']/following::select[1]")
                )
            )

            select_to = Select(to_warehouse_select)
            select_to.select_by_visible_text("IMS Warehouse")


            # --- Step 4: Click RUN ---
            run_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@class,'confirm-btn') and normalize-space()='RUN']")
                )
            )
            run_btn.click()
            print("Clicked RUN button")

            time.sleep(5)

            # --- Step 5: Validate table load ---
            wait.until(
                EC.presence_of_element_located((By.XPATH, "//tr[contains(@class,'Bold') and contains(@class,'ng-star-inserted')]"))
            )
            print("Stock Issue Report generated successfully.")

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Stock_Issue_Report_Success",
                attachment_type=allure.attachment_type.PNG
            )

        except Exception as e:
            print(f"Error occurred: {e}")
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Stock_Issue_Report_Error",
                attachment_type=allure.attachment_type.PNG
            )
            raise