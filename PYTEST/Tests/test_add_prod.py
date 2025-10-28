from PYTEST.pages.Login import login
from PYTEST.pages.Add_product import Add_prod
from selenium import webdriver
import pytest


def test_add_prod(driver: webdriver):
   login_page = login(driver)
   add_prod_page = Add_prod(driver)
   login_page.perform_login("Testuser", "Test@1234")
   add_prod_page.masters_click_test(driver)
   add_prod_page.add_prod_test(driver, "Testitemname", "Test1121", "Testdescription", 100)

if __name__ == "__main__":
   pytest.main()