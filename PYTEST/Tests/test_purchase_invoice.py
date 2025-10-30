from PYTEST.pages.Login import login
from PYTEST.pages.Purchase_invoice import PurchaseInvoice
from selenium import webdriver
import pytest
import random

def test_purchase_invoice(driver:webdriver):
   login_page = login(driver)
   purchase_invoice = PurchaseInvoice(driver)
   login_page.perform_login("Testuser", "Test@1234")

   random_num = random.randint(1, 99999)

   random_invoice_no = random.randint(10000, 99999)

   purchase_invoice.purchase_invoice_test(driver, random_invoice_no, random_num)
   purchase_invoice.save_button_click(driver)

if __name__ == "__main__":
   pytest.main()