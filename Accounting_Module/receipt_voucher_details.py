from login_details import login_to_ims
from receipt_voucher import MainPage
import time

def receipt_voucher_details():
   # Step 1: Login and get driver
   driver = login_to_ims()
   driver.maximize_window()
   # Step 2: Initialize MainPage with the logged-in driver
   receipt_voucher = MainPage(driver)
   # Step 3: Navigate through the app
   receipt_voucher.open_accounting_module()
   receipt_voucher.open_receipt_voucher()
   # Step 4: Add voucher details
   receipt_voucher.add_voucher("Automation Test Receipt", "PETTY CASH A/C")
   receipt_voucher.voucher_details(1500, "Test Narration", "7898548")
   # Step 5: Wait before closing
   time.sleep(5)
   driver.quit()

if __name__ == "__main__":
   receipt_voucher_details()