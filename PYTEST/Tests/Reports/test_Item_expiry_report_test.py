import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Item_Expiry_Report import ItemExpiryReportPage


# noinspection PyBroadException
@allure.title("Generate Item Expiry Report in IMS Application")
@allure.description("Logs in, navigates to Item Expiry Report, enters number of days, and runs the report.")
def test_item_expiry_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        item_expiry_report = ItemExpiryReportPage(driver)
        item_expiry_report.generate_item_expiry_report()

        print("Item Expiry Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Item_Expiry_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Item_Expiry_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
