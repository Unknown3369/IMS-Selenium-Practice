from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class sales_invoice:
   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 25)
      self.actions = ActionChains(driver)

      self.transactictions = (By.XPATH, "//span[contains(text(),'Transactions')]")
      self.sales_transaction =(By.LINK_TEXT, "Sales Transaction")
      self.sales_invoice_link = (By.XPATH, "//span[normalize-space()='Sales Tax Invoice']")
      self.refno = (By.XPATH, "//input[@id='refnoInput']")
      self.customer_enter = (By.XPATH, "//input[@id='customerselectid']")
      self.customer_select = (By.XPATH, "//div[@title='11 QA Customer ']")
      self.item_enter = (By.XPATH, "//input[@id='barcodeField']")
      self.quantity = (By.XPATH, "//input[@id='quantityBarcode' and @type='number' and @autocomplete='off']")
      self.save= (By.XPATH, "//button[normalize-space(text())='SAVE [End]']")
      self.amount_btn = (By.XPATH, "//button[normalize-space(text())='Balance Amount']")
      self.add_button = (By.XPATH, "//button[normalize-space(text())='Add']")
      self.save_button = (By.XPATH, "(//button[contains(text(),'SAVE') and contains(@class,'btn-info')])[last()]")

   def sales_invoice_test(self, driver: webdriver, ref_value: int):

      # Click on “Transactions” menu
      transactions = self.wait.until(
         EC.presence_of_element_located(self.transactictions)
      )
      driver.execute_script("arguments[0].scrollIntoView(true);", transactions)
      driver.execute_script("arguments[0].click();", transactions)
      print("Transactions clicked successfully!")

      # Hover over "Inventory Info" before clicking
      sales_transaction = self.wait.until(
         EC.presence_of_element_located(self.sales_transaction)
      )
      self.actions.move_to_element(sales_transaction).perform()
      time.sleep(2)  # give some time for the submenu to appear

      # Click after hovering
      sales_transaction.click()
      print("Sales Transaction hovered and clicked successfully!")

      # Click on “Sales Invoice” link
      sales_invoice_link = self.wait.until(
         EC.presence_of_element_located(self.sales_invoice_link)
      )
      driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sales_invoice_link)
      time.sleep(2)
      driver.execute_script("arguments[0].click();", sales_invoice_link)
      print("Sales Tax Invoice clicked successfully!")

      refno = self.wait.until(
         EC.presence_of_element_located(self.refno)
      )
      refno.send_keys(ref_value)
      print(f"Reference No '{ref_value}' entered successfully!")

      #enter customer details
      customer_enter =self.wait.until(
         EC.presence_of_element_located(self.customer_enter)
      )
      customer_enter.send_keys(Keys.ENTER)
      print("Clicked on Customer!")

      #Customer Select
      customer_select =self.wait.until(
         EC.presence_of_element_located(self.customer_select)
      )
      self.actions.double_click(customer_select).perform()
      print("Customer selected successfully!")

   def sales_invoice_form_test(self, driver: webdriver, item_code: str, gen_quantity: int):
      # Add Details in Sales Invoice Form

      #enter item details
      item_enter = self.wait.until(
         EC.presence_of_element_located(self.item_enter)
      )
      item_enter.click()
      item_enter.send_keys(item_code)
      item_enter.send_keys(Keys.ENTER)
      print("Clicked on Item field!")
      time.sleep(2) 

      #add quantity
      quantity = self.wait.until(
         EC.presence_of_element_located(self.quantity)
      )
      quantity.clear()
      quantity.send_keys(gen_quantity)
      quantity.send_keys(Keys.ENTER)
      quantity.clear()
      time.sleep(5)
      print("Quantity entered successfully!")


   def save_btn(self,driver: webdriver):

      # Click on Save button
      save = self.wait.until(
         EC.element_to_be_clickable(self.save)
      )
      save.click()
      print("Save button clicked successfully!")

      # Click on Balance Amount button
      amount_btn = self.wait.until(
         EC.element_to_be_clickable(self.amount_btn)
      )
      time.sleep(2)
      amount_btn.click()
      print("Balance Amount button clicked successfully!")

      # Click on Add button
      add_button = self.wait.until(
         EC.element_to_be_clickable(self.add_button)
      )
      time.sleep(2)
      add_button.click()
      print("Add button clicked successfully!")

      # Save the Sales Invoice
      save_button = self.wait.until(
         EC.element_to_be_clickable(self.save_button)
      )
      save_button.click()
      print("Save button clicked successfully!")
      time.sleep(5)