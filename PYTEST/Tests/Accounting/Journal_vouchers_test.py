from selenium import webdriver
from PYTEST.pages.Accounting.Journal_Vouchers import MainPage
from PYTEST.pages.Accounting.Login_accounting import Login
from datetime import datetime
import random
import time

def test_journal_voucher_details(driver):
    login = Login(driver)
    login.perform_login("Saga", "Ims@1234")

    journal_voucher = MainPage(driver)

    journal_voucher.open_accounting_module()
    journal_voucher.open_journal_voucher()

    # NOTE: Remove the Comment of the necessary methods and dont remove the comment of this line
    def generate_random_refno():
        date_part = datetime.now().strftime("%y%m%d")  # e.g. 251019
        random_part = random.randint(100, 999)
        return f"JV{date_part}{random_part}"
    # journal_voucher.add_voucher(generate_random_refno(), "Automation Test Voucher", 1000, 1000)
    # journal_voucher.edit_voucher(900, 900)
    journal_voucher.view_voucher()

    time.sleep(5)
    assert True
