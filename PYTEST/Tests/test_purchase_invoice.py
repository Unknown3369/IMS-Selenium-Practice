import csv
import pytest
import random
from selenium import webdriver
from PYTEST.pages.Login import login
from PYTEST.pages.Purchase_invoice import PurchaseInvoice


def read_products_from_csv(file_path):
   products = []
   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
   return products


def test_purchase_invoice(driver: webdriver):
   login_page = login(driver)
   purchase_invoice = PurchaseInvoice(driver)
   login_page.perform_login("Testuser", "Test@1234")

   # Load products from CSV
   products = read_products_from_csv("added_products.csv")

   random_invoice_no = random.randint(10000, 99999)

   purchase_invoice.purchase_invoice(driver, random_invoice_no)

   # Loop through CSV data
   for product in products:
      product_name = product['Product Name']
      hs_code = product['HS Code']
      description = product['Description']
      purchase_price = product['Purchase Price']
      sales_price = product['Sales Price']
      item_code = product['Item Code']  

      random_quantity = random.randint(10, 100)

      purchase_invoice.purchase_invoice_test(driver, item_code, random_quantity)
   purchase_invoice.save_button_click(driver)

if __name__ == "__main__":
   pytest.main()
