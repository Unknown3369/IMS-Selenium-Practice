from PYTEST.pages.Login import login
from PYTEST.pages.Add_product_vatable import Add_prod
from selenium import webdriver
import pytest
import time
import random
import uuid


def random_name():
   # short unique string using uuid
   return "prod_" + uuid.uuid4().hex[:8]

def test_add_prod(driver: webdriver):
   login_page = login(driver)
   add_prod_page = Add_prod(driver)
   login_page.perform_login("Testuser", "Test@1234")
   add_prod_page.masters_click_test(driver)

   for i in range(5):
      random_string = random_name()
      random_hs = random.randint(1000, 9999)
      random_price = random.randint(10, 999)
      output_price = random_price + random.randint(130, 200)
      add_prod_page.add_prod_test(driver, random_string, random_hs, "Testdescription", random_price,output_price)