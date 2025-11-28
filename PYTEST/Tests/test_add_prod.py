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

def clear_csv(filename="added_products.csv"):
   """Clears the CSV file and writes headers."""
   with open(filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Item Code", "Product Name", "HS Code", "Description", "Purchase Price", "Sales Price"])
   print("CSV file cleared successfully before adding new products.")

def save_product_to_csv(product_data, filename="added_products.csv"):
   """Appends a product entry to the CSV file. Creates file if it doesn’t exist."""
   file_exists = os.path.isfile(filename)
   with open(filename, mode="a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      # Only write headers if the file was missing or empty
      if os.stat(filename).st_size == 0:
         writer.writerow(["Item Code", "Product Name", "HS Code", "Description", "Purchase Price", "Sales Price"])
      writer.writerow(product_data)

def test_add_prod(driver: webdriver):
   login_page = login(driver)
   add_prod_page = Add_prod(driver)
   login_page.perform_login("Testuser", "Test@1234")
   add_prod_page.masters_click_test(driver)

   # Clear CSV before adding any new products
   clear_csv("added_products.csv")

   # Generate and add multiple products
   for i in range(1000):
      random_string = random_name()
      random_hs = random.randint(1000, 9999)
      random_price = random.randint(10, 999)
      output_price = random_price + random.randint(130, 200)
      
      # Get item code from add_prod_test()
      item_code = add_prod_page.add_prod_test(driver, random_string, random_hs, "Testdescription", random_price, output_price)

      # Save with item code included
      save_product_to_csv([item_code, random_string, random_hs, "Testdescription", random_price, output_price])