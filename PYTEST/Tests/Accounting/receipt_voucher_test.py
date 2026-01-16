from PYTEST.pages.Accounting.Login_accounting import Login
from PYTEST.pages.Accounting.receipt_voucher import MainPage
import time
import random

def test_receipt_voucher_details(driver):
   # Step 1: Login and get driver
   login = Login(driver)
   login.perform_login("Saga", "Ims@1234")
   # Step 2: Initialize MainPage with the logged-in driver
   receipt_voucher = MainPage(driver)
   # Step 3: Navigate through the app
   receipt_voucher.open_accounting_module()
   receipt_voucher.open_receipt_voucher()

   random_amount = random.uniform(1000.00,99999.99)
   random_chequeno = f"CH{random.randint(1000,9999)}"

   # Step 4: Add voucher details
   receipt_voucher.add_voucher("Automation Test Receipt", "PETTY CASH A/C")
   receipt_voucher.voucher_details(random_amount, "Test Narration", random_chequeno)
   assert True
