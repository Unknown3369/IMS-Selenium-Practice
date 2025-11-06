import pytest
from PYTEST.pages.Sales_book_report import SalesBookReportPage
from PYTEST.pages.Login import login
import allure
import time

def test_sales_book_report(driver):
   login_page = login(driver)
   sales_report = SalesBookReportPage(driver)

   login_page.perform_login("Testuser", "Test@1234")
   sales_report.open_sales_book_report()
   sales_report.run_sales_book_report()  

   with allure.step("Report Generated - capturing screenshot"):
      screenshot_path = f"screenshots/sales_report_{int(time.time())}.png"
      driver.save_screenshot(screenshot_path)
      allure.attach.file(screenshot_path, name="Sales Report Generated", attachment_type=allure.attachment_type.PNG)