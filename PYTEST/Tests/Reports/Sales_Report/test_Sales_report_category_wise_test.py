import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Sales_Report.Sales_report_category_wise import SalesReportCategoryWisePage


# noinspection PyBroadException
@allure.title("Generate Sales Report Category Wise in IMS Application")
@allure.description("Logs in, navigates to Reports → Sales Reports → Sales Report Category Wise, and generates the report with screenshots on success and failure.")
def test_generate_sales_report_category_wise(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Purchase Report Category Wise ---
        sales_report_category_page = SalesReportCategoryWisePage(driver)
        sales_report_category_page.generate_sales_report_category_wise()
        print("Sales Report Category Wise generated successfully.")

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Report_Category_Wise_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print("Screenshot captured after successful Sales Report Category Wise generation.")

    except Exception as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Sales_Report_Category_Wise_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Sales Report Category Wise test failed due to: {e}")
