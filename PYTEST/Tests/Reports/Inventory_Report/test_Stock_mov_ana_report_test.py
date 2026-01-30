import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Inventory_Reports.Stock_Movement_Analysis_Report import StockMovementAnalysisReportPage


# noinspection PyBroadException
@allure.title("Generate Stock Movement Analysis Report in IMS Application")
@allure.description("Logs in, navigates to Stock Movement Analysis Report, selects supplier, and runs the report.")
def test_stock_movement_analysis_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Stock Movement Analysis Report ---
        stock_mv_report = StockMovementAnalysisReportPage(driver)
        stock_mv_report.generate_stock_movement_analysis_report()

        print("Stock Movement Analysis Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Movement_Analysis_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Stock_Movement_Analysis_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach error details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
