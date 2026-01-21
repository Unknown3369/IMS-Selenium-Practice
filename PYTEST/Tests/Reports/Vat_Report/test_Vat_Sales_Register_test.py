import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Vat_Report.Vat_Sales_Register import VatSalesRegisterReportPage


# noinspection PyBroadException
@allure.title("Generate VAT Sales Register Report in IMS Application")
@allure.description("Logs in, navigates to VAT Sales Register Report, selects customer, and runs the report.")
def test_vat_sales_register_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        vat_sales_report = VatSalesRegisterReportPage(driver)
        vat_sales_report.generate_vat_sales_register_report()

        print(" VAT Sales Register Report generated successfully.")

        allure.attach(
            driver.get_screenshot_as_png(),
            name="VAT_Sales_Register_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="VAT_Sales_Register_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
