import pytest
import allure
from PYTEST.pages.Reports.Purchase_Report.Item_wise_purchase_report import PurchaseReport_ItemWise
from PYTEST.pages.Login import login
import time
import os

def test_itemwise_purchase_report(driver):
   login_page = login(driver)
   itemwise_report = PurchaseReport_ItemWise(driver)

   login_page.perform_login("Testuser", "Test@1234")
   itemwise_report.open_purchase_report_item_wise()  
   itemwise_report.run_item_wise_purchase_report()
   time.sleep (10)

   with allure.step("Report Generated - capturing screenshot"):
      os.makedirs("screenshots", exist_ok=True)
      screenshot_path = f"screenshots/sales_report_{int(time.time())}.png"
      driver.save_screenshot(screenshot_path)
      allure.attach.file(screenshot_path, name="Purchase Report Generated", attachment_type=allure.attachment_type.PNG)