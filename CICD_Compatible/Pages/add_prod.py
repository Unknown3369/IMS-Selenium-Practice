from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time

class Add_prod:

   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 30)
      self.actions = ActionChains(driver)
      self.master = (By.XPATH, "//span[contains(text(),'Masters')]")
      self.inventory_info = (By.LINK_TEXT, "Inventory Info")
      self.product_master = (By.XPATH,"//a[contains(@href, '/vendor-master/product')]")
      self.add_prod_btn = (By.XPATH,"//button[contains(text(), 'Add Product')]")
      self.add_prod_label = (By.XPATH,"//label[contains(text(), 'Add Product')]")
      self.item_group_input = (By.XPATH,"//input[@placeholder='-- Press Enter For Item Group --']")
      self.ng_select_box = (By.XPATH,"//ng-select[contains(@class,'ng-select-single')]//div[@role='combobox']")
      self.select_option = (By.XPATH,"//div[contains(@class,'ng-option')]//span[normalize-space()='0110']")
      self.ok_btn = (By.XPATH,"//button[.//span[contains(text(), 'Ok')]]")
      self.item_code_input = (By.XPATH,"//input[@placeholder='Enter Item Code']")
      self.item_name_input = (By.XPATH,"//input[@placeholder='Enter Item Name']")
      self.hs_code_input = (By.XPATH,"//input[@placeholder='Enter HS Code']")
      self.unit_dropdown = (By.XPATH,"//select[@id='unit']")
      self.description_input = (By.XPATH,"//input[@placeholder='Enter Product Description']")
      self.short_name = (By.XPATH,"//input[@placeholder='Enter Short Name']")
      self.purchase_price = (By.XPATH,"//input[@placeholder='Enter Purchase Price']")
      self.select_input = (By.XPATH,"//input[@placeholder='Press Enter to select']")
      self.supplier = (By.XPATH,"//td[normalize-space()='11 QA Vendor']")
      self.sales_price = (By.XPATH,"//input[@type='number' and @placeholder='0']")
      self.category_dropdown = (By.XPATH,"//select[@id='Category']")
      self.save_button_locator = (By.XPATH,"//button[@id='save' and text()='SAVE']")
      self.vat_checkbox = (By.XPATH,"//input[@type='checkbox']")

   def masters_click_test(self, driver: webdriver):

      masters = self.wait.until(
         EC.presence_of_element_located(self.master)
      )
      driver.execute_script(
         "arguments[0].scrollIntoView(true);",
         masters
      )
      time.sleep(1)

      driver.execute_script(
         "arguments[0].click();",
         masters
      )
      print("Masters clicked successfully!")

      inventory_info = self.wait.until(
         EC.presence_of_element_located(self.inventory_info)
      )
      self.actions.move_to_element(inventory_info).perform()
      time.sleep(2)
      inventory_info.click()
      print("Inventory Info hovered and clicked successfully!")

      product_master_link = self.wait.until(
         EC.presence_of_element_located(self.product_master)
      )

      driver.execute_script(
         "arguments[0].scrollIntoView({block: 'center'});",
         product_master_link
      )
      time.sleep(2)

      driver.execute_script(
         "arguments[0].click();",
         product_master_link
      )
      print("Product Master clicked successfully!")
      time.sleep(2)

      add_product_btn = self.wait.until(
         EC.element_to_be_clickable(self.add_prod_btn)
      )
      add_product_btn.click()
      print("Add Product button clicked successfully!")

      add_product_label = self.wait.until(
         EC.visibility_of_element_located(self.add_prod_label)
      )

      add_product_label.click()
      print("Add Product label clicked successfully!")

   # Add Product Form Fill
   def add_prod_test(self,driver: webdriver,input_itemname: str,input_hscode: str,input_description: str,input_purchase_price: int,input_sales_price: int):

      # Item Group Selection
      item_group_input = self.wait.until(
         EC.presence_of_element_located(self.item_group_input)
      )
      item_group_input.send_keys(Keys.ENTER)
      time.sleep(1)
      ng_select_box = self.wait.until(
         EC.element_to_be_clickable(self.ng_select_box)
      )
      driver.execute_script("arguments[0].click();",ng_select_box)
      print("ng-select box clicked")

      select_option = self.wait.until(
         EC.element_to_be_clickable(self.select_option)
      )

      driver.execute_script(
         "arguments[0].click();",
         select_option
      )
      print("Option selected")

      ok_btn = self.wait.until(
         EC.element_to_be_clickable(self.ok_btn)
      )
      ok_btn.click()
      print("OK button clicked")

      # Item Name
      item_name_input = self.wait.until(
         EC.visibility_of_element_located(self.item_name_input)
      )
      item_name_input.clear()
      item_name_input.send_keys(input_itemname)
      print(f"Item Name entered: {input_itemname}")

      # HS Code
      hs_code_input = self.wait.until(
         EC.visibility_of_element_located(self.hs_code_input)
      )
      hs_code_input.clear()
      hs_code_input.send_keys(str(input_hscode))
      print(f"HS Code entered: {input_hscode}")

      # Stock Unit
      unit_dropdown = self.wait.until(
         EC.visibility_of_element_located(self.unit_dropdown)
      )
      Select(unit_dropdown).select_by_visible_text("Pkt.")
      print("Stock Unit selected successfully!")

      # Description
      description_input = self.wait.until(
         EC.visibility_of_element_located(self.description_input)
      )
      description_input.clear()
      description_input.send_keys(input_description)
      print("Description entered successfully!")

      # Short Name
      short_name = self.wait.until(
         EC.visibility_of_element_located(self.short_name)
      )
      short_name.clear()
      short_name.send_keys("TestProd")
      print("Short Name entered successfully!")

      # Category
      category_dropdown = self.wait.until(
         EC.element_to_be_clickable(self.category_dropdown)
      )
      Select(category_dropdown).select_by_visible_text("N/A")
      print("Category selected successfully!")

      # Purchase Price
      purchase_price = self.wait.until(
         EC.visibility_of_element_located(self.purchase_price)
      )
      purchase_price.clear()
      purchase_price.send_keys(str(input_purchase_price))
      print(f"Purchase Price entered: {input_purchase_price}")

      # Supplier Selection
      select_input = self.wait.until(
         EC.visibility_of_element_located(self.select_input)
      )
      select_input.send_keys(Keys.ENTER)
      time.sleep(1)
      supplier = self.wait.until(
         EC.element_to_be_clickable(self.supplier)
      )
      self.actions.double_click(supplier).perform()
      print("Supplier selected successfully!")

      # Sales Price
      sales_price = self.wait.until(
         EC.visibility_of_element_located(self.sales_price)
      )
      sales_price.clear()
      sales_price.send_keys(str(input_sales_price))
      print(f"Sales Price entered: {input_sales_price}")

      # Item Code Read
      item_code_element = self.wait.until(
         EC.presence_of_element_located(self.item_code_input)
      )
      self.wait.until(
         lambda d: item_code_element.get_attribute("value").strip() != ""
      )
      item_code = item_code_element.get_attribute("value").strip()
      print("Generated Item Code:", item_code)
      return item_code

   # Utility Functions
   def _safe_get_value(self, locator):
      try:
         element = self.driver.find_element(*locator)
         value = element.get_attribute("value")
         if value is not None:
            return value.strip()
         return element.text.strip()
      except Exception:
         return ""

   def _safe_select_value(self, locator):
      try:
         element = self.driver.find_element(*locator)
         select = Select(element)
         return select.first_selected_option.text.strip()
      except Exception:
         return ""

   # Read All Product Fields
   def read_all_product_fields(self):
      data = {}
      data["Item Group"] = self._safe_get_value(
         self.item_group_input)
      data["Item Code"] = self._safe_get_value(
         self.item_code_input)
      data["Item Name"] = self._safe_get_value(
         self.item_name_input)
      data["HS Code"] = self._safe_get_value(
         self.hs_code_input)
      data["Stock Unit"] = self._safe_select_value(
         self.unit_dropdown)
      data["Description"] = self._safe_get_value(
         self.description_input)
      data["Short Name"] = self._safe_get_value(
         self.short_name)
      data["Category"] = self._safe_select_value(
         self.category_dropdown)
      data["Purchase Price Excl VAT"] = self._safe_get_value(
         self.purchase_price)
      data["Sales Price Incl VAT"] = self._safe_get_value(
         self.sales_price)

      # VAT checkbox
      try:
         vat_checkbox = self.driver.find_element(*self.vat_checkbox)
         data["Is Vatable Item"] = (
            "Yes" if vat_checkbox.is_selected() else "No")
      except Exception:
         data["Is Vatable Item"] = ""

      # Supplier Name
      try:
         supplier_name = self.driver.find_element(
            By.XPATH,
            "//td[normalize-space()='11 QA Vendor']"
         ).text.strip()
         data["Supplier Name"] = supplier_name
      except Exception:
         data["Supplier Name"] = ""

      # Default Values
      data["Group Code"] = "14"
      data["Item Type"] = "Product"
      print("All product fields read successfully.")
      return data

   # Save Product
   def save_button(self):
      save_button = self.wait.until(
         EC.element_to_be_clickable(self.save_button_locator)
      )
      save_button.click()
      print("SAVE button clicked successfully!")

      # Browser Alert Handling
      try:
         WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
         )
         alert = self.driver.switch_to.alert
         print("Alert says:", alert.text)
         alert.accept()
         print("Alert accepted successfully!")
      except TimeoutException:
         print("No browser alert found.")

      # Modal OK Button Handling
      try:
         ok_modal = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
               (
                  By.XPATH,
                  "//button[normalize-space()='OK' or normalize-space()='Ok']"
               )
            )
         )
         ok_modal.click()
         print("Modal OK clicked.")
      except Exception:
         print("No modal popup found.")
      time.sleep(2)
