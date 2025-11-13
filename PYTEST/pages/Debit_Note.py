from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

class Debit_Note:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 25)
      self.actions = ActionChains(self.driver)

      self.transactions = (By.XPATH, "//span[contains(text(), 'Transactions')]")
      self.pur_transaction = (By.LINK_TEXT, "Purchase Transaction")
      self.debit_note = (By.XPATH, "//span[normalize-space()='Debit Note (Purchase Return)']")
      self.ref_no = (By.XPATH, "//input[@id='invoiceNO']")
      self.return_mode = (By.XPATH, "//select[@id='paymentTerms']")
      self.supplier = (By.XPATH, "//input[@id='customerselectid']")
      self.select_supplier = (By.XPATH, "//div[normalize-space(text())='Dark Chocolate Vendor']") 
      self.item_name = (By.XPATH, "//input[@id='barcodeField']")
      self.quantity = (By.XPATH, "//input[@id='quantityBarcode']")    
      self.save_button = (By.XPATH, "//button[normalize-space(text())='SAVE [End]']")

   def enter_debit_note(self):
      transactions = self.wait.until(
         EC.element_to_be_clickable(self.transactions)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", transactions)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", transactions)
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
      debit_note_link = self.wait.until(
         EC.presence_of_element_located(self.debit_note)
      )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", debit_note_link)
      time.sleep(2)
      self.driver.execute_script("arguments[0].click();", debit_note_link)
      print("Debit Note clicked successfully!")

   def debit_note_entry(self, enter_ref_no: str):
      ref_no = self.wait.until(
         EC.presence_of_element_located(self.ref_no)
      )
      ref_no.click()
      ref_no.send_keys(enter_ref_no)
      print(f"Reference No '{enter_ref_no}' entered successfully!")

      return_mode = self.wait.until(
         EC.presence_of_element_located(self.return_mode)
      )
      return_mode.click()
      select_mode = Select(return_mode)
      select_mode.select_by_visible_text("Cash")
      print("Return mode 'Cash' selected successfully!")

      supplier = self.wait.until(
         EC.presence_of_element_located(self.supplier)
      )
      supplier.send_keys(Keys.ENTER)
      select_supplier = self.wait.until(
         EC.presence_of_element_located(self.select_supplier)
      )
      self.actions.double_click(select_supplier).perform()
      print("Supplier selected successfully!")

   def debit_note_test(self, driver:webdriver, item_code: str, enter_quantity: int):
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
      time.sleep(2)

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