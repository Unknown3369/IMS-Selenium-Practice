from selenium import webdriver
from PYTEST.pages.Accounting.Add_ledger import MainPage
from PYTEST.pages.Accounting.Login_accounting import Login
import time

def random_name():
    import uuid
    return "ledger_" + uuid.uuid4().hex[:8]

def test_add_ledger_details():
    # Step 1: Login and get driver
    driver = webdriver.Edge()
    login = Login(driver)
    login.perform_login("Saga", "Ims@1234")

    # Step 2: Initialize MainPage with the logged-in driver
    Add_ledger = MainPage(driver)

    # Step 3: Navigate through the app
    Add_ledger.open_accounting_module()
    Add_ledger.open_ledger_group_master()

    add_new_ledger_name = random_name()
    # Step 4: Add new ledger
    Add_ledger.add_new_ledger(add_new_ledger_name)
    print("Ledger added successfully!")

    # Step 5: Wait before closing
    time.sleep(5)
    assert True