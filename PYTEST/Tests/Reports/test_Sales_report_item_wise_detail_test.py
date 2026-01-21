import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Sales_report_item_wise_detail import SalesReportItemWiseDetailPage


# noinspection PyBroadException
@allure.title("Generate Sales Report Item Wise Detail in IMS Application")
@allure.description("Logs in, navigates to Reports → Sales Reports → Sales Report Item Wise Detail, and generates the report with screenshots on success and failure.")
def test_generate_sales_report_item_wise_detail(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Sales Report Item Wise Detail ---
        sales_report_page = SalesReportItemWiseDetailPage(driver)
        sales_report_page.generate_sales_report_item_wise_detail()
        print("Sales Report Item Wise Detail generated successfully.")

        # Step 3: Capture screenshot after successful report generation
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Report_Item_Wise_Detail_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print("Screenshot captured after successful Sales Report Item Wise Detail generation.")

    except Exception as e:
        # Step 4: Capture screenshot & error details on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Report_Item_Wise_Detail_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Sales Report Item Wise Detail test failed due to: {e}")
