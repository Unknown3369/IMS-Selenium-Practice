from CICD_Compatible.Pages.login import login
from CICD_Compatible.Pages.add_prod import Add_prod
from selenium import webdriver
import pytest
import allure
import random
import uuid
import csv
import os
import time

CSV_FILE = "added_products.csv"

# RANDOM PRODUCT GENERATOR

def random_name():
   return f"prod_{uuid.uuid4().hex[:8]}"

def generate_random_product():
   purchase_price = random.randint(50, 150)
   return {
      "item_name": random_name(),
      "hs_code": str(random.randint(1000, 9999)),
      "description": "Automation Test Product",
      "purchase_price": purchase_price,
      "sales_price": purchase_price + random.randint(100, 250)
   }

# CSV HELPERS
def clear_csv(filename=CSV_FILE):
   headers = [
      "Group Code",
      "Item Group",
      "Item Code",
      "HS Code",
      "Item Name",
      "Category",
      "Stock Unit",
      "Is Vatable Item",
      "Item Type",
      "Description",
      "Purchase Price",
      "Sales Price"
   ]
   with open(filename, mode="w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(headers)
   print("CSV reset complete.")

def save_product_to_csv(product_data, filename=CSV_FILE):
   file_exists = os.path.exists(filename)
   with open(filename, mode="a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      # Add headers if file newly created
      if not file_exists or os.stat(filename).st_size == 0:
         writer.writerow([
            "Group Code",
            "Item Group",
            "Item Code",
            "HS Code",
            "Item Name",
            "Category",
            "Stock Unit",
            "Is Vatable Item",
            "Item Type",
            "Description",
            "Purchase Price",
            "Sales Price"
         ])
      writer.writerow(product_data)
   print("Product written to CSV successfully.")

# MAIN TEST
@allure.title("Add Product and Save Details to CSV")
@allure.description("Creates products dynamically and stores generated data into CSV")
def test_add_prod(driver: webdriver):
   login_page = login(driver)
   add_prod_page = Add_prod(driver)

   # LOGIN
   login_page.perform_login("Testuser", "Test@1234")
   assert login_page.verify_login_success()

   # NAVIGATE
   add_prod_page.masters_click_test(driver)

   # RESET CSV ONCE
   clear_csv()

   # PRODUCT LOOP
   number_of_products = 3
   for i in range(number_of_products):
      print(f"\nCreating Product #{i + 1}")
      product = generate_random_product()

      # FILL PRODUCT FORM
      item_code = add_prod_page.add_prod_test(
         driver,
         input_itemname=product["item_name"],
         input_hscode=product["hs_code"],
         input_description=product["description"],
         input_purchase_price=product["purchase_price"],
         input_sales_price=product["sales_price"]
      )
      print("Generated Item Code:", item_code)

      # READ PRODUCT DETAILS
      product_data_dict = add_prod_page.read_all_product_fields()

      # PREPARE CSV ROW
      csv_row = [
         product_data_dict.get("Group Code", "14"),
         product_data_dict.get("Item Group", ""),
         product_data_dict.get("Item Code", ""),
         product_data_dict.get("HS Code", ""),
         product_data_dict.get("Item Name", ""),
         product_data_dict.get("Category", ""),
         product_data_dict.get("Stock Unit", ""),
         product_data_dict.get("Is Vatable Item", ""),
         product_data_dict.get("Item Type", ""),
         product_data_dict.get("Description", ""),
         product_data_dict.get("Purchase Price Excl VAT", ""),
         product_data_dict.get("Sales Price Incl VAT", "")
      ]

      # SAVE TO CSV
      save_product_to_csv(csv_row)

      # SAVE PRODUCT
      add_prod_page.save_button()
      print("Product saved successfully.")

      # ASSERTIONS
      toast_message = add_prod_page.get_toast_message()
      print("Toast Message:", toast_message)
      assert (
         "success" in toast_message.lower()
         or "saved" in toast_message.lower()
      )
      # Small stabilization wait
      time.sleep(2)
   print("\nAll products created successfully.")