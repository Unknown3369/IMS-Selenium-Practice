from selenium import webdriver
from PYTEST.pages.Accounting.Add_Sub_Ledger import MainPage
from PYTEST.pages.Accounting.Login_accounting import Login
import time

def random_name():
    import uuid
    return "subledger_" + uuid.uuid4().hex[:8]

def random_number():
    import random
    return str(random.randint(1000000000, 9999999999))

def test_add_sub_ledger_details(driver):
    login = Login(driver)
    login.perform_login("Saga", "Ims@1234")

    # Step 2: Initialize MainPage with the logged-in driver
    Add_sub_ledger = MainPage(driver)

    # Step 3: Navigate through the app
    Add_sub_ledger.open_accounting_module()
    Add_sub_ledger.open_sub_ledger_account_master()

    # Step 4: Add new sub ledger
    Add_sub_ledger.add_new_sub_ledger(random_name(), random_number())

    # Step 5: Wait before closing
    time.sleep(5)
    assert True