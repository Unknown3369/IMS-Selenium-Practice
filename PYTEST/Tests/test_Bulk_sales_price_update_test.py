import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Bulk_Sales_Price_Update import BulkSalesPriceUpdatePage


# noinspection PyBroadException
@allure.title("Bulk Sales Price Update in IMS Application")
@allure.description("Logs in, navigates to Bulk Sales Price Update page, selects Item Group and Category as Chocolate, and updates prices for 4 items randomly.")
def test_bulk_sales_price_test(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:

        login_page.perform_login("Paras", "Ims@1234")
        print("✅ Logged into IMS")

        bulk_page = BulkSalesPriceUpdatePage(driver)
        bulk_page.navigate_to_bulk_sales_price()
        print("✅ Navigated to Bulk Sales Price Update page")

        bulk_page.select_item_group()
        print("✅ Successfully selected Item Group and Category: Chocolate")

        bulk_page.update_prices()
        print("✅ Successfully updated prices for 4 items randomly.")

        # Screenshot for success
        allure.attach(driver.get_screenshot_as_png(), name="Bulk_Sales_Price_Update_Success",
            attachment_type=allure.attachment_type.PNG)
        print("📸 Screenshot captured for success.")

    except Exception as e:
        # Capture screenshot and log error for Allure
        allure.attach(driver.get_screenshot_as_png(), name="Bulk_Sales_Price_Update_Error",
            attachment_type=allure.attachment_type.PNG)
        allure.attach(str(e), name="Error Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"❌ Test failed due to: {e}")
