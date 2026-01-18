import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.One_Lakh_Above_Purchase_Report import OneLakhAbovePurchaseReportPage


# noinspection PyBroadException
@allure.title("Generate One Lakh Above Purchase Report in IMS Application")
@allure.description("Logs in, navigates to One Lakh Above Purchase Report, clicks RUN, and verifies the table.")
def test_one_lakh_above_purchase_report(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate One Lakh Above Purchase Report ---
        one_lakh_purchase_report = OneLakhAbovePurchaseReportPage(driver)
        one_lakh_purchase_report.generate_one_lakh_above_purchase_report()

        print("One Lakh Above Purchase Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="One_Lakh_Above_Purchase_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="One_Lakh_Above_Purchase_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
