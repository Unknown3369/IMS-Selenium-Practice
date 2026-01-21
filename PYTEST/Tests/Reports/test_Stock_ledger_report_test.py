import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Stock_Ledger_Report import StockLedReportPage


# noinspection PyBroadException
@allure.title("Generate Stock Ledger Report in IMS Application")
@allure.description("Logs in, navigates to Stock Ledger Report, selects warehouse and item, and runs the report.")
def test_stock_ledger_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Stock Ledger Report ---
        stock_led_report = StockLedReportPage(driver)
        stock_led_report.generate_stock_ledger_report()

        print("Stock Ledger Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Ledger_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Ledger_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
