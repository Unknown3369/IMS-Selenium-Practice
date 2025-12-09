import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Stock_Issue_Report import StockIssueReportPage


# noinspection PyBroadException
@allure.title("Generate Stock Issue Report in IMS Application")
@allure.description("Logs in, navigates to Stock Issue Report, selects From and To Warehouses, and runs the report.")
def test_stock_issue_report(driver):
    login_page = login(driver)

    try:

        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Stock Issue Report ---
        stock_issue_report = StockIssueReportPage(driver)
        stock_issue_report.generate_stock_issue_report()

        print("Stock Issue Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Issue_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Issue_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
