from selenium import webdriver
from PYTEST.pages.Accounting.Contra_vouchers import ContraVouchersPage
from PYTEST.pages.Accounting.Login_accounting import Login
import random
import time

def test_contra_voucher_details(driver):
   login = Login(driver)
   login.perform_login("Saga", "Ims@1234")

   contra_voucher = ContraVouchersPage(driver)
   contra_voucher.open_accounting_module()
   contra_voucher.open_contra_voucher()

   def generate_random_refno():
      random_number = random.randint(1000, 9999)
      return f"CV-REF-{random_number}"
   
   contra_voucher.add_contra_voucher(generate_random_refno(), "Automation Test Contra Voucher", 1500, 1500)
   time.sleep(5)
   assert True