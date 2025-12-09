import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Sales_book_report import SalesBookReportPage


# noinspection PyBroadException
@allure.title("Generate Sales Book Report in IMS Application")
@allure.description("Logs in, navigates to Reports → Sales Reports → Sales Book Report, and generates the report with screenshots on success and failure.")
def test_generate_sales_book_report(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Sales Book Report ---
        sales_report_page = SalesBookReportPage(driver)
        sales_report_page.open_sales_book_report()
        sales_report_page.run_sales_book_report()
        print("Sales Book Report generated successfully.")

        # Step 3: Capture screenshot after full report generation
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Book_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print("Screenshot captured after successful Sales Book Report generation.")

    except Exception as e:
        # Step 4: Capture screenshot & error details if something fails
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Book_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Sales Book Report test failed due to: {e}")
