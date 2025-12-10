import pytest
import random
from selenium import webdriver
from PYTEST.pages.Login import login
from PYTEST.pages.Sales_invoice import sales_invoice
import csv
import time

def read_products_from_csv(file_path):
   products = []
   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
   return products

def test_sales_invoice(driver: webdriver):

   login_page = login(driver)
   login_page.perform_login("Testuser", "Test@1234")

   ref_num = str(random.randint(1000, 9999))
   

   # Load products from CSV
   products = read_products_from_csv("added_products.csv")

   sales_invoice_page = sales_invoice(driver)
   sales_invoice_page.sales_invoice_test(driver, ref_num)

   for product in products:
      product_name = product['Product Name']
      hs_code = product['HS Code']
      description = product['Description']
      purchase_price = product['Purchase Price']
      sales_price = product['Sales Price']
      item_code = product['Item Code']  

      ran_quantity = str(random.randint(4, 20))

      sales_invoice_page.sales_invoice_form_test(driver, item_code,ran_quantity)
   sales_invoice_page.save_btn(driver)

if __name__ == "__main__":
   pytest.main()