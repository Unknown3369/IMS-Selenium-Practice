from PYTEST.pages.Login import login
from PYTEST.pages.Add_product import Add_prod
from selenium import webdriver
import pytest
import random


def test_add_prod(driver: webdriver):
   login_page = login(driver)
   add_prod_page = Add_prod(driver)
   login_page.perform_login("Testuser", "Test@1234")
   add_prod_page.masters_click_test(driver)

   def generate_random_string(length):
      letters = "abcdefghijklmnopqrstuvwxyz"
      return "".join(random.choice(letters) for _ in range(length))
   random_string = generate_random_string(10)

   def generate_random_hscode(length):
      random_hs = random.randint(1000, 9999)
      return str(random_hs)
   
   add_prod_page.add_prod_test(driver, random_string, generate_random_hscode(4), "Testdescription", 100)

if __name__ == "__main__":
   pytest.main()