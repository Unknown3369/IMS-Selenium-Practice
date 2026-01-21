import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Vat_Report.Vat_Purchase_Return_Register import VatPurchaseReturnRegisterReportPage


# noinspection PyBroadException
@allure.title("Generate VAT Purchase Return Register Report in IMS Application")
@allure.description("Logs in, navigates to VAT Purchase Return Register Report, selects supplier, checks checkbox, and runs the report.")
def test_vat_purchase_return_register_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:

        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate VAT Purchase Return Register Report ---
        vat_purchase_return_report = VatPurchaseReturnRegisterReportPage(driver)
        vat_purchase_return_report.generate_vat_purchase_return_register_report()

        print("VAT Purchase Return Register Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="VAT_Purchase_Return_Register_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="VAT_Purchase_Return_Register_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
