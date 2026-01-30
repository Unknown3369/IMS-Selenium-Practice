import pytest
import allure
from PYTEST.pages.Reports.Sales_Report.Sales_report_customer_wise import Sales_report_customer_wise
from PYTEST.pages.Login import login
import time
import os

def test_sales_report_customer_wise(driver):
   login_page = login(driver)
   login_page.perform_login("Testuser", "Test@1234")
   sales_report_customer_wise = Sales_report_customer_wise(driver)
   sales_report_customer_wise.sale_report_customer_wise()
   sales_report_customer_wise.test_sales_report_customer_wise()
   time.sleep (10)

   with allure.step("Report Generated - capturing screenshot"):
      os.makedirs("screenshots", exist_ok=True)
      screenshot_path = f"screenshots/sales_report_{int(time.time())}.png"
      driver.save_screenshot(screenshot_path)
      allure.attach.file(screenshot_path, name="Purchase Report Generated", attachment_type=allure.attachment_type.PNG)