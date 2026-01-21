import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Purchase_report_item_wise_detail import PurchaseReportItemWiseDetailPage


# noinspection PyBroadException
@allure.title("Generate Purchase Report Item Wise Detail in IMS Application")
@allure.description("Logs in, navigates to Reports → Purchase Reports → Purchase Report Item Wise Detail, and generates the report with screenshots on success and failure.")
def test_generate_purchase_report_item_wise_detail(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        purchase_detail_page = PurchaseReportItemWiseDetailPage(driver)
        purchase_detail_page.generate_purchase_report_item_wise_detail()
        print("Purchase Report Item Wise Detail generated successfully.")

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Purchase_Report_Item_Wise_Detail_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print("Screenshot captured after successful Purchase Report Item Wise Detail generation.")

    except Exception as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Purchase_Report_Item_Wise_Detail_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Purchase Report Item Wise Detail test failed due to: {e}")
