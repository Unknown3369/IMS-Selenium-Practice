from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PYTEST.tests.test_1_login import test_login_to_ims
import keyboard
import time

class Add_prod:
   def __init__(self, driver: webdriver):
      self.driver =driver
      self.wait = WebDriverWait(driver, 25)
      self.actions = ActionChains(driver)
      self.master = (By.XPATH, "//span[contains(text(),'Masters')]")
      self.inventory_info = (By.LINK_TEXT, "Inventory Info")
      self.product_master = (By.XPATH, "//a[contains(@href, '/vendor-master/product')]")
      self.add_prod_btn = (By.XPATH, "//button[contains(text(), 'Add Product')]")
      self.add_prod_label = (By.XPATH, "//label[contains(text(), 'Add Product')]")
      self.item_group_input = (By.XPATH, "//input[@placeholder='-- Press Enter For Item Group --']")
      self.ng_select_box = (By.XPATH, "//ng-select[@bindlabel='DESCA']")
      self.select_option = (By.XPATH, "//div[@class='ng-option ng-star-inserted']//span[normalize-space(text())='Chocolate']")
      self.ok_btn = (By.XPATH, "//button[.//span[contains(text(), 'Ok')]]")
      self.item_code_input = (By.XPATH, "//input[@placeholder='Enter Item Code']")
      self.item_name_input = (By.XPATH, "//input[@placeholder='Enter Item Name']")
      self.hs_code_input = (By.XPATH, "//input[@placeholder='Enter HS Code']")
      self.vatable_checkbox = (By.XPATH, "//input[@type='checkbox' and contains(@class, 'form-check-input')]")
      self.unit_dropdown = (By.XPATH, "//select[@id='unit']")
      self.description_input = (By.XPATH, "//input[@placeholder='Enter Product Description']")
      self.short_name = (By.XPATH, "//input[@placeholder='Enter Short Name']")
      self.purchase_price = (By.XPATH, "//input[@placeholder='Enter Purchase Price']")
      self.select_input = (By.XPATH, "//input[@placeholder='Press Enter to select']")
      self.supplier = (By.XPATH, "//td[contains(@class,'mat-column-ACNAME') and normalize-space(text())='testprodsupp']")
      self.sales_price = (By.XPATH, "//input[@type='number' and @placeholder='0']")
      self.save_button = (By.XPATH, "//button[@id='save' and text()='SAVE']")

   def masters_click_test(self, driver: webdriver):
      # Click on “Masters” menu
      masters = self.wait.until(
         EC.presence_of_element_located(self.master)
      )
      driver.execute_script("arguments[0].scrollIntoView(true);", masters)
      time.sleep(1)
      driver.execute_script("arguments[0].click();", masters)
      print("Masters clicked successfully!")

      # Hover over "Inventory Info" before clicking
      inventory_info = self.wait.until(
         EC.presence_of_element_located(self.inventory_info)
      )
      self.actions.move_to_element(inventory_info).perform()
      time.sleep(2)  # give some time for the submenu to appear

      # Click after hovering
      inventory_info.click()
      print("Inventory Info hovered and clicked successfully!")

      # Click on “Product Master” link
      product_master_link = self.wait.until(
         EC.presence_of_element_located(self.product_master)
      )
      driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_master_link)
      time.sleep(2)
      driver.execute_script("arguments[0].click();", product_master_link)
      print("Product Master clicked successfully!")

      # Click on “Add Product” button
      add_product_btn = self.wait.until(
         EC.element_to_be_clickable(self.add_prod_btn)
      )
      add_product_btn.click()
      print("Add Product button clicked successfully!")

      # Wait for the "Add Product" label
      add_product_label = self.wait.until(
         EC.visibility_of_element_located(self.add_prod_label)
      )
      print("Add Product label is visible")
      time.sleep(1)
      add_product_label.click()
      print("Add Product label clicked successfully!")

   def add_prod_test(self, driver: webdriver,input_itemname: str, input_hscode: str, input_description: str, input_purchase_price: int):
      # Wait for the item group input box
      item_group_input = self.wait.until(
         EC.presence_of_element_located(self.item_group_input)
      )
      item_group_input.send_keys(Keys.ENTER)
      time.sleep(1)

      # Wait for the ng-select dropdown
      ng_select_box = self.wait.until(
         EC.element_to_be_clickable(self.ng_select_box)
      )
      ng_select_box.click()
      print("ng-select box clicked successfully!")

      # Select the option
      select_option = self.wait.until(
         EC.element_to_be_clickable(self.select_option)
         )
      select_option.click()
      print("option selected successfully!")

      # Click OK button
      ok_button = self.wait.until(
         EC.element_to_be_clickable(self.ok_btn)
      )
      ok_button.click()
      print("OK button clicked successfully!")

      # Wait for the "Enter Item Name" input box
      item_name_input = self.wait.until(
         EC.visibility_of_element_located(self.item_name_input)
      )
      item_name_input.send_keys(input_itemname)
      print("Item Name entered successfully!")

      # Wait for the "Enter HS Code" input box
      hs_code_input = WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located(self.hs_code_input)
      )
      hs_code_input.send_keys(input_hscode)
      print("HS Code entered successfully!")

      # Click on "is Vatable Item" Checkbox
      checkbox = self.wait.until(
         EC.element_to_be_clickable(self.vatable_checkbox)
      )
      checkbox.click()
      print("Checkbox clicked successfully!")

      # Wait until the Stock Unit is visible
      unit_dropdown = self.wait.until(
         EC.visibility_of_element_located(self.unit_dropdown)
      )
      unit_dropdown.click()
      print("Unit dropdown clicked successfully!")

      stock = Select(unit_dropdown)

      stock.select_by_visible_text("Pkt.")
      print("Stock Unit selected successfully!")

      # Wait for the "Enter Product Description" input box
      description_input = self.wait.until(
         EC.visibility_of_element_located(self.description_input)
      )
      description_input.send_keys(input_description)
      print("Product Description entered successfully!")

      # Wait for the "Enter Short Name" input box
      short_name = self.wait.until(
         EC.visibility_of_element_located(self.short_name)
      )
      short_name.send_keys("TestProd")
      print("Short Name entered successfully!")

      category_dropdown = self.wait.until(
         EC.element_to_be_clickable((By.XPATH, "//select[@id='Category']"))
      )
      select_category = Select(category_dropdown)
      select_category.select_by_visible_text("N/A")
      print("Category selected successfully!")

      purchase_price = self.wait.until(
         EC.visibility_of_element_located(self.purchase_price)
      )
      purchase_price.send_keys(input_purchase_price)
      print("Purchase Price entered successfully!")

      # Wait for the input field to appear
      select_input = self.wait.until(
         EC.visibility_of_element_located(self.select_input)
      )

      # Click the input field (since it is read-only, we simulate a click or press Enter)
      select_input.send_keys(Keys.ENTER)
      print("Triggered dropdown selection successfully!")

      time.sleep(5)

      # Wait for the cell with text "ABC Camp 2" to appear and be clickable
      supplier = self.wait.until(
         EC.element_to_be_clickable(self.supplier)
      )

      # Click the cell
      self.actions.double_click(supplier).perform()
      print(f"Supplier {supplier} selected successfully!")

      # Wait for the Sales Price input box
      sales_price = WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located(self.sales_price)
      )  
      sales_price.send_keys("150")
      print("Sales Price entered successfully!")

      # Wait for the SAVE button to be clickable
      save_button =self.wait.until(
         EC.element_to_be_clickable(self.save_button)
      )

      # Click the SAVE button
      save_button.click()
      print("SAVE button clicked successfully!")

      self.wait.until(EC.alert_is_present())
      alert = driver.switch_to.alert

      # Print the alert text (optional)
      print("Alert says:", alert.text)

      # Alert handling
      #alert.accept() 
      alert.dismiss()  

