from selenium import webdriver
from Journal_Vouchers import MainPage
from login_details import login_to_ims
from datetime import datetime
import random
import time

def journal_voucher_details():
    driver = login_to_ims()

    journal_voucher = MainPage(driver)

    journal_voucher.open_accounting_module()
    journal_voucher.open_journal_voucher()

    # NOTE: Remove the Comment of the necessary methods and dont remove the commetn of this line
    def generate_random_refno():
        date_part = datetime.now().strftime("%y%m%d")  # e.g. 251019
        random_part = random.randint(100, 999)
        return f"JV{date_part}{random_part}"
    journal_voucher.add_voucher(generate_random_refno(), "Automation Test Voucher", 1000, 1000)
    # journal_voucher.edit_voucher(1000)
    # journal_voucher.view_voucher()

    time.sleep(5)
    driver.quit()
if __name__ == "__main__":
    journal_voucher_details()
    time.sleep(25)