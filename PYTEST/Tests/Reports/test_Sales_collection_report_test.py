import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Sales_collection_report import SalesCollectionReportPage


# noinspection PyBroadException
@allure.title("Generate Sales Collection Report in IMS Application")
@allure.description("Logs in, navigates to Reports → Sales Reports → Sales Collection Report, and generates the report with screenshots on success and failure.")
def test_generate_sales_collection_report(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Sales Collection Report ---
        sales_collection_page = SalesCollectionReportPage(driver)
        sales_collection_page.generate_sales_collection_report()
        print("Sales Collection Report generated successfully.")

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Collection_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print("Screenshot captured after successful Sales Collection Report generation.")

    except Exception as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Collection_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Sales Collection Report test failed due to: {e}")
