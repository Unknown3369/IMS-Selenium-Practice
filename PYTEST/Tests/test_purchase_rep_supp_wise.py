import pytest
import allure
from PYTEST.pages.Purchase_rep_supp_wise import Purchase_rep_supp_wise
from PYTEST.pages.Login import login
import time
import os

def test_itemwise_purchase_report(driver):
   login_page = login(driver)
   supplierwise_report = Purchase_rep_supp_wise(driver)

   login_page.perform_login("Testuser", "Test@1234")
   supplierwise_report.purchase_report_supp()  
   supplierwise_report.run_purchase_report_supp()
   time.sleep (10)

   with allure.step("Report Generated - capturing screenshot"):
      os.makedirs("screenshots", exist_ok=True)
      screenshot_path = f"screenshots/sales_report_{int(time.time())}.png"
      driver.save_screenshot(screenshot_path)
      allure.attach.file(screenshot_path, name="Purchase Report Generated", attachment_type=allure.attachment_type.PNG)