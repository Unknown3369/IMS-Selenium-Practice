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
   return "prod_" + uuid.uuid4().hex[:8]

def clear_csv(filename="added_products.csv"):
   with open(filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Group Code", "Item Group", "Item Code", "HS Code", "Item Name", "Category", "Stock Unit", "Is Vatable Item", "Item Type", "Description", "Purchase Price", "Sales Price"])
   print("CSV reset complete.")

def save_product_to_csv(product_data, filename="added_products.csv"):
   file_empty = (not os.path.exists(filename)) or os.stat(filename).st_size == 0
   with open(filename, mode="a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      if file_empty:
         writer.writerow(["Group Code", "Item Group", "Item Code", "HS Code", "Item Name", "Category", "Stock Unit", "Is Vatable Item", "Item Type", "Description", "Purchase Price", "Sales Price"])
      writer.writerow(product_data)

def test_add_prod(driver: webdriver):
   login_page = login(driver)
   add_prod_page = Add_prod(driver)
   # Login and navigate
   login_page.perform_login("Testuser", "Test@1234")
   add_prod_page.masters_click_test(driver)
   # CSV reset
   clear_csv("added_products.csv")
   # prepare product input
   for i in range(1):  # Change range for multiple products
      random_item_name = random_name()
      random_hs_code = str(random.randint(1000, 9999))
      random_description = "Test Product Description"
      random_purchase_price = random.randint(50, 150)
      random_sales_price = random.randint(200, 350)
      # Fill the form (do not save yet)
      item_code = add_prod_page.add_prod_test(
         driver,
         input_itemname=random_item_name,
         input_hscode=random_hs_code,
         input_description=random_description,
         input_purchase_price=random_purchase_price,
         input_sales_price=random_sales_price
      )
      print("Form filled. Generated Item Code:", item_code)
      # Read all fields BEFORE clicking save
      product_data_dict = add_prod_page.read_all_product_fields()
      # Prepare CSV row and save BEFORE clicking SAVE
      csv_row = [
         product_data_dict.get("Group Code", "14"),
         product_data_dict.get("Item Group", ""),
         product_data_dict.get("Item Code", ""),
         product_data_dict.get("HS Code", ""),
         product_data_dict.get("Item Name", ""),
         product_data_dict.get("Category",""),
         product_data_dict.get("Stock Unit", ""),
         product_data_dict.get("Is Vatable Item", ""),
         product_data_dict.get("Item Type", ""),
         product_data_dict.get("Description", ""),
         product_data_dict.get("Purchase Price Excl VAT", ""),
         product_data_dict.get("Sales Price Incl VAT", "")
      ]
      save_product_to_csv(csv_row, "added_products.csv")
      print("Product details written to CSV BEFORE saving the product!")
      # Now click save and handle popups
      add_prod_page.save_button()
      # Optional: after save you may want to re-read or assert something
      # final_data = add_prod_page.read_all_product_fields()
      # assert final_data.get("Item Code") == item_code
