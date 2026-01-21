import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Stock_Ageing_Report import StockAgeingReportPage


# noinspection PyBroadException
@allure.title("Generate Stock Ageing Report in IMS Application")
@allure.description("Logs in, navigates to Stock Ageing Report, selects supplier, and runs the report.")
def test_stock_ageing_report(driver):
    login_page = login(driver)

    try:

        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Stock Ageing Report ---
        stock_ageing_report = StockAgeingReportPage(driver)
        stock_ageing_report.generate_stock_ageing_report()

        print("Stock Ageing Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Ageing_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Ageing_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
