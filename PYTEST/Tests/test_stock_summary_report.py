import pytest
from PYTEST.pages.stock_summary_report import StockSummaryReport
from PYTEST.pages.Login import login
import allure
import time
import os

def test_stock_summary_report(driver):
   login_page = login(driver)
   stock_report = StockSummaryReport(driver)

   login_page.perform_login("Testuser", "Test@1234")
   stock_report.open_stock_summary_report()  # <-- run actual flow
   stock_report.select_branch()
   stock_report.run_report()
   time.sleep(8)  # Wait for report to generate

   with allure.step("Report Generated - capturing screenshot"):
      os.makedirs("screenshots", exist_ok=True)
      screenshot_path = f"screenshots/stock_summary_report_{int(time.time())}.png"
      driver.save_screenshot(screenshot_path)
      allure.attach.file(screenshot_path, name="Stock Summary Report Generated", attachment_type=allure.attachment_type.PNG)