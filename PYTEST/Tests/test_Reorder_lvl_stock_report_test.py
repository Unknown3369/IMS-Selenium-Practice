import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reorder_Lvl_Stock_Report import ReorderLevelStockReportPage


# noinspection PyBroadException
@allure.title("Generate Reorder Level Stock Report in IMS Application")
@allure.description("Logs in, navigates to Reorder Level Stock Report, selects warehouse, and runs the report.")
def test_reorder_level_stock_report(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("✅ Logged into IMS")

        # --- Step 2: Generate Reorder Level Stock Report ---
        reorder_stock_report = ReorderLevelStockReportPage(driver)
        reorder_stock_report.generate_reorder_level_stock_report()

        print("✅ Reorder Level Stock Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Reorder_Level_Stock_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Reorder_Level_Stock_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"❌ Test failed due to: {e}")
