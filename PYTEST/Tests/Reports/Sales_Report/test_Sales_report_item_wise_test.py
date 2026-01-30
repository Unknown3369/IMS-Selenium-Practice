import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Sales_Report.Sales_report_item_wise import SalesReportItemWisePage


# noinspection PyBroadException
@allure.title("Generate Sales Report (Item Wise) in IMS Application")
@allure.description("Logs in, navigates to Reports → Sales Reports → Item Wise, selects Item Group, Customer, Item, and generates the report with screenshots on success and failure.")
def test_generate_sales_report_itemwise(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Sales Report (Item Wise) ---
        sales_itemwise_page = SalesReportItemWisePage(driver)
        sales_itemwise_page.generate_sales_report_item_wise()
        print("Sales Report (Item Wise) generated successfully.")

        # Step 3: Capture screenshot after successful generation
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Report_ItemWise_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print("Screenshot captured after successful Sales Report (Item Wise) generation.")

    except Exception as e:
        # Step 4: Capture screenshot & error details on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Report_ItemWise_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Sales Report (Item Wise) test failed due to: {e}")
