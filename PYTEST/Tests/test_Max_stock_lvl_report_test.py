import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Max_Stock_Lvl_report import MaxStockLevelReportPage


# noinspection PyBroadException
@allure.title("Generate Maximum Stock Level Report in IMS Application")
@allure.description("Logs in, navigates to Maximum Stock Level Report, selects supplier and warehouse, and runs the report.")
def test_max_stock_level_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("✅ Logged into IMS")

        max_stock_report = MaxStockLevelReportPage(driver)
        max_stock_report.generate_max_stock_level_report()

        print("✅ Maximum Stock Level Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Max_Stock_Level_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Max_Stock_Level_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"❌ Test failed due to: {e}")
