import pytest
from PYTEST.pages.Purchase_report_item_wise_detail import Purchase_report_item_wise_detail
from PYTEST.pages.Login import login
import allure
import time
import os
import csv

def read_products_from_csv(file_path):
   products = []
   with open(file_path, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
            products.append(row)
   return products

def test_purchase_report_item_wise_details(driver):
   login_page = login(driver)
   purchase_report = Purchase_report_item_wise_detail(driver)

   login_page.perform_login("Testuser", "Test@1234")

   products = read_products_from_csv("added_products.csv")

   purchase_report.item_wise_detail_report() 
   purchase_report.open_item_wise_detail_report()  # <-- run actual flow
   # for product in products:
   #    product_name = product['Product Name']
   #    hs_code = product['HS Code']
   #    description = product['Description']
   #    purchase_price = product['Purchase Price']
   #    sales_price = product['Sales Price']
   #    item_code = product['Item Code']  
   #    print(f"Processing product: {product_name} (Item Code: {item_code})")
   #    purchase_report.fill_item_wise_detail_report(product_name)
   #    print(f"Filled report for product: {product_name} (Item Code: {item_code})")
   purchase_report.fill_item_wise_detail_report()
   purchase_report.run_item_wise_detail_report()
   time.sleep(8)  # Wait for report to generate

   with allure.step("Report Generated - capturing screenshot"):
      os.makedirs("screenshots", exist_ok=True)
      screenshot_path = f"screenshots/purchase_report_item_wise_details_{int(time.time())}.png"
      driver.save_screenshot(screenshot_path)
      allure.attach.file(screenshot_path, name="Purchase Report Item Wise Details Generated", attachment_type=allure.attachment_type.PNG)