from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ..tests.login_test import test_login_to_ims
import keyboard
import time
import random

class PurchaseInvoice:
   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 25)
      self.actions = ActionChains(driver)

      self.transactions = (By.XPATH, "//span[contains(text(), 'Transactions')]")
      self.pur_transaction = (By.LINK_TEXT, "Purchase Transaction")
      self.purchase_invoice_link = (By.XPATH, "//span[normalize-space()='Purchase Invoice']")
      self.invoice_no = (By.XPATH, "//input[@id='invoiceNO']")
      self.account = (By.XPATH, "//input[@id='accountfield']")
      self.account_name = (By.XPATH, "//div[@title='Dark Chocolate Vendor']")
      self.item_name = (By.XPATH, "//input[@id='barcodeField' and @placeholder='Enter Barcode']")
      self.quantity = (By.XPATH, "//input[@id='quantityBarcode' and @type='number']")
      self.save_button = (By.XPATH, "//button[contains(text(),'SAVE')]")

   def purchase_invoice(self, driver: webdriver, invoice_value: int):
      transactions = self.wait.until(
         EC.element_to_be_clickable(self.transactions)
      )
      driver.execute_script("arguments[0].scrollIntoView(true);", transactions)
      time.sleep(1)
      driver.execute_script("arguments[0].click();", transactions)
      print("Transactions clicked successfully!")

      # Hover over "Inventory Info" before clicking
      purchase_transaction = self.wait.until(
         EC.presence_of_element_located(self.pur_transaction)
      )
      self.actions.move_to_element(purchase_transaction).perform()

      # Click after hovering
      purchase_transaction.click()
      print("Purchase Transaction hovered and clicked successfully!")

      # Click on “Product Invoice” link
      purchase_invoice_link = self.wait.until(
         EC.presence_of_element_located(self.purchase_invoice_link)
      )
      driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", purchase_invoice_link)
      time.sleep(2)
      driver.execute_script("arguments[0].click();", purchase_invoice_link)
      print("Purchase Invoice clicked successfully!")

      # add invoice no
      invoice_no = self.wait.until(
         EC.presence_of_element_located(self.invoice_no)
      )
      invoice_no.click()
      invoice_no.send_keys(invoice_value)
      print(f"Invoice No '{invoice_value}' entered successfully!")

      # Select Vendor
      account =self.wait.until(
         EC.presence_of_element_located(self.account)
      )
      account.click()
      account.send_keys(Keys.ENTER)
      time.sleep(5)
      print("Account field clicked successfully!")

      # Select account name
      account_name = self.wait.until(
         EC.presence_of_element_located(self.account_name)
      )
      self.actions.double_click(account_name).perform()
      print("Account name selected successfully!")
      time.sleep(2)
   
   def purchase_invoice_test(self, driver:webdriver, item_code: str, enter_quantity: int):

      # Click on item name field
      item_name = self.wait.until(EC.presence_of_element_located(self.item_name))
      item_name.clear()
      item_name.send_keys(item_code)   # type the actual Item Code
      time.sleep(2)
      item_name.send_keys(Keys.ENTER)
      time.sleep(2)
      print("Item name field clicked successfully!")

      #add quantity
      quantity = self.wait.until(
         EC.presence_of_element_located(self.quantity)
      )
      quantity.clear()
      quantity.send_keys(enter_quantity)
      quantity.send_keys(Keys.ENTER)
      print("Quantity entered successfully!")
   
   def save_button_click(self, driver:webdriver):
      # Click on save button
      save_button = self.wait.until(
         EC.element_to_be_clickable(self.save_button)
      )
      save_button.click()
      print("Save button clicked successfully!")

      #Alert handling
      WebDriverWait(driver, 10).until(EC.alert_is_present())
      alert = driver.switch_to.alert

      # Print the alert text (optional)
      print("Alert says:", alert.text)

      # Alert handling
      alert.accept()  # If you want to click "OK"
      #alert.dismiss()  # If you want to click "Cancel"
