from PYTEST.pages.Login import login
from PYTEST.pages.Add_product_vatable import Add_prod
from selenium import webdriver
import pytest
import time
import random
import uuid
import csv
import os


def random_name():
   # short unique string using uuid
   return "prod_" + uuid.uuid4().hex[:8]

def save_product_to_csv(product_data, filename="added_products.csv"):
   """Appends a product entry to the CSV file. Creates file if it doesn’t exist."""
   file_exists = os.path.isfile(filename)
   with open(filename, mode="a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      if not file_exists:
         writer.writerow(["Item Code", "Product Name", "HS Code", "Description", "Purchase Price", "Sales Price"])
      writer.writerow(product_data)


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

      # get item code from add_prod_test()
      item_code = add_prod_page.add_prod_test(driver, random_string, random_hs, "Testdescription", random_price, output_price)

      # save with item code included
      save_product_to_csv([item_code, random_string, random_hs, "Testdescription", random_price, output_price])
