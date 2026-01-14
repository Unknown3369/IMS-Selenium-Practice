from selenium import webdriver
from PYTEST.pages.Accounting.Add_Ledger_Group import MainPage
from PYTEST.pages.Accounting.Login_accounting import Login
import time

def random_name():
    import uuid
    return "ledgergroup_" + uuid.uuid4().hex[:8]

def test_ledger_details(driver):
    # Step 1: Login and get driver
    login =Login(driver)
    login.perform_login("Saga", "Ims@1234")

    # Step 2: Initialize MainPage with the logged-in driver
    Add_Ledger_Group = MainPage(driver)

    # Step 3: Navigate through the app
    Add_Ledger_Group.open_accounting_module()
    Add_Ledger_Group.open_ledger_group_master()

    # Step 4: Add new ledger
    add_new_ledger_group_name = random_name()
    Add_Ledger_Group.add_new_ledger_group(add_new_ledger_group_name)
    print("Ledger Group added successfully!")

    # Step 5: Wait before closing
    time.sleep(5)
    assert True