import pytest
from PYTEST.pages.Purchase_book_report import PurchaseBookReport
from PYTEST.pages.Login import login
import allure
import time
import os

def test_purchase_book_report(driver):
   login_page = login(driver)
   purchase_report = PurchaseBookReport(driver)

   login_page.perform_login("Testuser", "Test@1234")
   purchase_report.open_purchase_book_report()  # <-- run actual flow

   with allure.step("Report Generated - capturing screenshot"):
      os.makedirs("screenshots", exist_ok=True)
      screenshot_path = f"screenshots/sales_report_{int(time.time())}.png"
      driver.save_screenshot(screenshot_path)
      allure.attach.file(screenshot_path, name="Purchase Report Generated", attachment_type=allure.attachment_type.PNG)
      