import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Inventory_Reports.Stock_Valuation_Report import StockValuationReportPage


# noinspection PyBroadException
@allure.title("Generate Stock Valuation Report in IMS Application")
@allure.description("Logs in, navigates to Stock Valuation Report, selects item, and runs the report.")
def test_stock_valuation_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        stock_val_report = StockValuationReportPage(driver)
        stock_val_report.generate_stock_valuation_report()

        print("Stock Valuation Report generated successfully.")

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Valuation_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Valuation_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
