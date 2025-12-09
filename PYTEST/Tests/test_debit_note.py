import csv
import pytest
import random
import time
from selenium import webdriver
from PYTEST.pages.Login import login
from PYTEST.pages.Debit_Note import Debit_Note

def read_products_from_csv(file_path):
   products = []
   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
   return products

def test_debit_note(driver: webdriver):
   login_page = login(driver)
   debit_note = Debit_Note(driver)
   time.sleep(15)
   login_page.perform_login("TestTest", "Test@1234")

   # Load products from CSV
   products = read_products_from_csv("added_products.csv")

   random_ref_no = "REF_NO" + str(random.randint(10000, 99999))

   debit_note.enter_debit_note()
   debit_note.debit_note_entry(str(random_ref_no))

   # Loop through CSV data
   for product in products:
      item_code = product['Item Code']  
      random_quantity = random.randint(1, 10)

      debit_note.debit_note_test(driver, item_code, random_quantity)
      time.sleep(1)
   debit_note.save_button_click(driver)