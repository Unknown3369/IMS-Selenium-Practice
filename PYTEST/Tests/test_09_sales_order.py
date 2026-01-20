import pytest
import random
import csv
import time
from PYTEST.pages.Login import login
from PYTEST.pages.Sales_order import SalesOrder
from selenium import webdriver

def read_products_from_csv(file_path):
   products = []
   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
   return products

def test_sales_order(driver: webdriver):
   login_page = login(driver)
   sales_order = SalesOrder(driver)
   login_page.perform_login("Testuser", "Test@1234")

   # Load products from CSV
   products = read_products_from_csv("added_products.csv")

   sales_order.sales_order()
   
   for product in products:
      product_name = product['Item Name']
      hs_code = product['HS Code']
      description = product['Description']
      purchase_price = product['Purchase Price']
      sales_price = product['Sales Price']
      item_code = product['Item Code']  
      ref_no = str(random.randint(10000, 99999))
      random_quantity = random.randint(2, 10)

      sales_order.sales_order_test(ref_no, item_code, random_quantity)