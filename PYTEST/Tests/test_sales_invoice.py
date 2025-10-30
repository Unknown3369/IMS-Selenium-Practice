import pytest
import random
from selenium import webdriver
from PYTEST.pages.Login import login
from PYTEST.pages.Sales_invoice import sales_invoice

def test_sales_invoice(driver: webdriver):

   login_page = login(driver)
   login_page.perform_login("Testuser", "Test@1234")

   sales_invoice_page = sales_invoice(driver)
   sales_invoice_page.sales_invoice_test(driver)

   ref_num = str(random.randint(1000, 9999))
   ran_quantity = str(random.randint(1, 9999))

   sales_invoice_page.sales_invoice_form_test(driver, ref_num, ran_quantity)

   assert "Invoice" in driver.title or driver.current_url, "Sales invoice not loaded correctly"