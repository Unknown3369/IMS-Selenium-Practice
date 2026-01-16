from selenium import webdriver
from PYTEST.pages.Accounting.Payment_Vouchers import MainPage
from PYTEST.pages.Accounting.Login_accounting import Login
from datetime import datetime
import random
import time

def test_payment_voucher_details(driver):
    # Login and get driver
    login = Login(driver)
    login.perform_login("Saga", "Ims@1234")

    # Initialize MainPage with the logged-in driver
    payment_voucher = MainPage(driver)

    # Navigate through the app
    payment_voucher.open_accounting_module()
    payment_voucher.open_payment_voucher()

    # Add voucher details
    def generate_random_refno():
        date_part = datetime.now().strftime("%y%m%d")  # e.g. 251019
        random_part = random.randint(100, 999)
        return f"JV{date_part}{random_part}"
    
    def generate_rendom_chequeno():
        random_num = random.randint(1000,9999)
        return f"{random_num}"
    
    def generate_random_amount():
        random_float = random.uniform(1000.00,99999.99)
        return f"{random_float}"
    
    payment_voucher.add_voucher_details(generate_random_refno(), "Test Payment", "John Doe", generate_random_amount(), generate_rendom_chequeno())

    payment_voucher.save_voucher()
    assert True