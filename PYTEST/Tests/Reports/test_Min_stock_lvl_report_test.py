import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Min_Stock_Lvl_Report import MinStockLevelReportPage


# noinspection PyBroadException
@allure.title("Generate Minimum Stock Level Report in IMS Application")
@allure.description("Logs in, navigates to Minimum Stock Level Report, selects warehouse, and runs the report.")
def test_min_stock_level_report(driver):

    login_page = login(driver)
    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Minimum Stock Level Report ---
        min_stock_report = MinStockLevelReportPage(driver)
        min_stock_report.generate_min_stock_level_report()

        print("Minimum Stock Level Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Min_Stock_Level_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Min_Stock_Level_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
