from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class SalesOrder:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 25)
      self.actions = ActionChains(driver)

      self.transactions = (By.XPATH, "//span[contains(text(), 'Transactions')]")
      self.sales_transaction = (By.LINK_TEXT, "Sales Transaction")
      self.sales_order_link = (By.XPATH, "//span[normalize-space()='Sales Order']")
      self.ref_no = (By.XPATH,"//input[@id='invoiceNO' and @type='text']")
      self.customer = (By.XPATH,"//input[@id='customerselectid' and @placeholder='Press ENTER or TAB to select Customer']")
      self.customer_select = (By.XPATH,"//div[@title='44' and normalize-space(text())='44']")
      self.barcode = (By.XPATH, "//input[@id='barcodeField' and @placeholder='Enter Barcode']")
      self.quantity = (By.XPATH,"//input[@id='quantityBarcode' and @type='number']")
      self.save = (By.XPATH, "//button[normalize-space(text())='SAVE [End]']")

   def sales_order(self):
      transactions = self.wait.until(
         EC.presence_of_element_located(self.transactions)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", transactions)
      self.driver.execute_script("arguments[0].click();", transactions)
      print("Transactions clicked successfully!")

      sales_transaction = self.wait.until(
         EC.presence_of_element_located(self.sales_transaction)
      )
      self.actions.move_to_element(sales_transaction).perform()
      time.sleep(2)
      sales_transaction.click()
      print("Sales Transaction hovered and clicked successfully!")

      sales_order = self.wait.until(
         EC.presence_of_element_located(self.sales_order_link)
      )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sales_order)
      time.sleep(2)
      self.driver.execute_script("arguments[0].click();", sales_order)
      print("Sales Order clicked successfully!")
      time.sleep(5)

   def sales_order_test(self, ref_no_enter: str, barcode_enter: str, enter_quantity: int):
      ref_no = self.wait.until(
         EC.presence_of_element_located(self.ref_no)
      )
      ref_no.click()
      ref_no.send_keys(ref_no_enter)
      print("Reference number entered successfully!")

      customer = self.wait.until(
         EC.presence_of_element_located(self.customer)
      )
      customer.click()
      customer.send_keys(Keys.ENTER)
      print ("Customer clicked entered ")
      time.sleep(2)

      customer_select = self.wait.until(
         EC.presence_of_element_located(self.customer_select)
      )
      self.actions.double_click(customer_select).perform()
      print("Customer selected successfully!")

      barcode = self.wait.until(
         EC.presence_of_element_located(self.barcode)
      )
      barcode.clear()
      barcode.send_keys(barcode_enter)
      barcode.send_keys(Keys.ENTER)
      print(f"Barcode {barcode_enter} entered successfully!")

      quantity = self.wait.until(
         EC.presence_of_element_located(self.quantity)
      )
      quantity.click()
      time.sleep(3)
      quantity.clear()
      quantity.send_keys(enter_quantity)
      quantity.send_keys(Keys.ENTER)
      print("Quantity entered successfully!")

      save_button = self.wait.until(
         EC.element_to_be_clickable(self.save)
      )
      save_button.click()
      print("Save button clicked successfully!")