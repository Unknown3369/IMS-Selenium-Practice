from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

class Add_prod:
   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 30)
      self.actions = ActionChains(driver)
      # locators (kept as you provided)
      self.master = (By.XPATH, "//span[contains(text(),'Masters')]")
      self.inventory_info = (By.LINK_TEXT, "Inventory Info")
      self.product_master = (By.XPATH, "//a[contains(@href, '/vendor-master/product')]")
      self.add_prod_btn = (By.XPATH, "//button[contains(text(), 'Add Product')]")
      self.add_prod_label = (By.XPATH, "//label[contains(text(), 'Add Product')]")
      self.item_group_input = (By.XPATH, "//input[@placeholder='-- Press Enter For Item Group --']")
      self.ng_select_box = (By.XPATH, "//ng-select[contains(@class,'ng-select-single')]//div[@role='combobox']")
      self.select_option = (By.XPATH, "//div[contains(@class,'ng-option')]//span[normalize-space()='0110']")
      self.ok_btn = (By.XPATH, "//button[.//span[contains(text(), 'Ok')]]")
      self.item_code_input = (By.XPATH, "//input[@placeholder='Enter Item Code']")
      self.item_name_input = (By.XPATH, "//input[@placeholder='Enter Item Name']")
      self.hs_code_input = (By.XPATH, "//input[@placeholder='Enter HS Code']")
      self.unit_dropdown = (By.XPATH, "//select[@id='unit']")
      self.description_input = (By.XPATH, "//input[@placeholder='Enter Product Description']")
      self.short_name = (By.XPATH, "//input[@placeholder='Enter Short Name']")
      self.purchase_price = (By.XPATH, "//input[@placeholder='Enter Purchase Price']")
      self.select_input = (By.XPATH, "//input[@placeholder='Press Enter to select']")
      self.supplier = (By.XPATH, "//td[normalize-space()='11 QA Vendor']")
      self.sales_price = (By.XPATH, "//input[@type='number' and @placeholder='0']")
      self.save_button_locator = (By.XPATH, "//button[@id='save' and text()='SAVE']")
   # nvigation / open form
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
      time.sleep(2)

      # Click on “Add Product” button
      add_product_btn = self.wait.until(
         EC.element_to_be_clickable(self.add_prod_btn)
      )
      print("Add Product button located")
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

   def add_prod_test(self, driver: webdriver, input_itemname: str, input_hscode: str, input_description: str, input_purchase_price: int, input_sales_price: int):
      # Item Group - press enter to open list, choose value
      item_group_input = self.wait.until(
         EC.presence_of_element_located(self.item_group_input)
         )
      item_group_input.send_keys(Keys.ENTER)
      time.sleep(1)

      # ng-select choose
      ng_select_box = self.wait.until(
         EC.element_to_be_clickable(self.ng_select_box)
         )
      ng_select_box.click()
      print("ng-select box clicked")

      self.wait.until(
         EC.element_to_be_clickable(self.select_option)
         ).click()
      print("option selected")

      self.wait.until(
         EC.element_to_be_clickable(self.ok_btn)
         ).click()
      print("OK button clicked")
      # Item Name
      item_name_input = self.wait.until(
         EC.visibility_of_element_located(self.item_name_input)
         )
      item_name_input.clear()
      item_name_input.send_keys(input_itemname)
      print("Item Name entered:", input_itemname)

      # HS Code
      hs_code_input = WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located(self.hs_code_input)
         )
      hs_code_input.send_keys(input_hscode)
      print("HS Code entered:", input_hscode)

      unit_dropdown = self.wait.until(
         EC.visibility_of_element_located(self.unit_dropdown)
         )
      unit_dropdown.click()
      print("Unit dropdown clicked")

      Select(unit_dropdown).select_by_visible_text("Pkt.")
      print("Unit 'Pkt.' selected")


      description_input = self.wait.until(
         EC.visibility_of_element_located(self.description_input)
         )
      description_input.send_keys(input_description)
      print("Description entered:", input_description)

      short_name = self.wait.until(
         EC.visibility_of_element_located(self.short_name)
         )
      short_name.send_keys("TestProd")
      print("Short Name entered: TestProd")

      category_dropdown = self.wait.until(
         EC.element_to_be_clickable((By.XPATH, "//select[@id='Category']"))
         )
      Select(category_dropdown).select_by_visible_text("N/A")
      print("Category 'N/A' selected")

      # Purchase price
      purchase_price = self.wait.until(
         EC.visibility_of_element_located(self.purchase_price)
         )
      purchase_price.clear()
      purchase_price.send_keys(str(input_purchase_price))
      print("Purchase Price entered:", input_purchase_price)

      # Supplier selection (read-only input triggers list)
      select_input = self.wait.until(
         EC.visibility_of_element_located(self.select_input)
         )
      select_input.send_keys(Keys.ENTER)
      time.sleep(1)
      print("Triggered dropdown selection successfully!")

      supplier = self.wait.until(
         EC.element_to_be_clickable(self.supplier)
         )
      # double click to select as original script did
      self.actions.double_click(supplier).perform()
      print(f"Supplier {supplier} selected successfully!")

      sales_price = self.wait.until(
         EC.visibility_of_element_located(self.sales_price)
      )
      sales_price.clear()
      sales_price.send_keys(str(input_sales_price))
      time.sleep(0.5)
      print("Sales Price entered successfully!")

      # Wait for item code generation (readonly input)
      item_code_element = self.wait.until(
         EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Item Code' and @readonly]"))
         )
      self.wait.until(lambda d: item_code_element.get_attribute("value").strip() != "")
      item_code = item_code_element.get_attribute("value").strip()
      return item_code
      print("Generated Item Code:", item_code)
   # sfe field readers (helper)
   def _safe_get_value(self, by_locator):
      try:
         el = self.driver.find_element(*by_locator)
         return el.get_attribute("value") if el.get_attribute("value") is not None else el.text
      except Exception:
         return ""

   def _safe_get_text(self, by_locator):
      try:
         el = self.driver.find_element(*by_locator)
         return el.text.strip()
      except Exception:
         return ""

   def _safe_select_first_text(self, by_locator):
      try:
         el = self.driver.find_element(*by_locator)
         sel = Select(el)
         opts = sel.all_selected_options
         if opts:
            return opts[0].text.strip()
         # fallback: maybe first option
         options = sel.options
         if options:
            return options[0].text.strip()
         return ""
      except Exception:
         return ""

   # read all visible fields (safe — won't raise if optional element missing)
   def read_all_product_fields(self):
      data = {}
      # Basic inputs
      data["Item Group"] = self._safe_get_value(
         (By.XPATH, "//input[@placeholder='-- Press Enter For Item Group --']")
         )
      data["Item Code"] = self._safe_get_value(self.item_code_input)
      data["Item Name"] = self._safe_get_value(self.item_name_input)
      data["HS Code"] = self._safe_get_value(self.hs_code_input)
      # Stock Unit (select) safe
      data["Stock Unit"] = self._safe_select_first_text(
         (By.XPATH, "//select[@id='unit']")
         )
      # VAT checkbox (safe)
      try:
         vat_el = self.driver.find_element(
            By.XPATH, "//input[@type='checkbox']"
            )
         data["Is Vatable Item"] = "Yes" if vat_el.is_selected() else "No"
      except Exception:
         data["Is Vatable Item"] = ""
      # Item Type (optional — may not exist)
      try:
         data["Item Type"] = self._safe_select_first_text(
            (By.XPATH, "//select[@id='ptype']/option[@selected]/text()")
            )
      except Exception:
         data["Item Type"] = ""
      # Other fields
      data["Description"] = self._safe_get_value(self.description_input)
      data["Short Name"] = self._safe_get_value(self.short_name)
      data["Category"] = self._safe_select_first_text(
         (By.XPATH, "//select[@id='Category']")
         )
      data["Purchase Price Excl VAT"] = self._safe_get_value(self.purchase_price)
      # purchase price incl VAT may be rendered differently — try following input
      try:
         data["Purchase Price Incl VAT"] = self.driver.find_element(
            By.XPATH, "//input[@placeholder='Enter Purchase Price']/following::input[1]"
            ).get_attribute("value")
      except Exception:
         data["Purchase Price Incl VAT"] = ""
      # Supplier name (table cell)
      try:
         supplier_cell = self.driver.find_element(
            By.XPATH, "//td[contains(@class,'ng-star-inserted') and normalize-space(text())!='']"
            )
         data["Supplier Name"] = supplier_cell.text.strip()
      except Exception:
         data["Supplier Name"] = ""
      # Sales prices (safe)
      try:
         data["Sales Price Incl VAT"] = self.driver.find_element(
            By.XPATH, "(//input[@type='number'])[1]"
            ).get_attribute("value")
      except Exception:
         data["Sales Price Incl VAT"] = ""
      try:
         data["Sales Price Excl VAT"] = self.driver.find_element(
            By.XPATH, "(//input[@type='number'])[2]"
            ).get_attribute("value")
      except Exception:
         data["Sales Price Excl VAT"] = ""
      # Margin fields optional
      try:
         data["Recommended Margin"] = self.driver.find_element(
            By.XPATH, "//div[contains(text(),'Recommended Margin')]/following::input[1]"
            ).get_attribute("value")
      except Exception:
         data["Recommended Margin"] = ""
      try:
         data["Actual Margin"] = self.driver.find_element(
            By.XPATH, "//div[contains(text(),'Actual Margin')]/following::div"
            ).text.strip()
      except Exception:
         data["Actual Margin"] = ""
      return data
      print("All product fields read successfully.")

   # click save and handle popups (robust)
   def save_button(self):
      save_button = self.wait.until(
         EC.element_to_be_clickable(self.save_button_locator)
         )
      save_button.click()

      # First handle browser alert if present
      try:
         self.wait.until(
            EC.alert_is_present(), timeout=5
            )
         alert = self.driver.switch_to.alert
         try:
            # accept (works for typical ok dialogs)
            alert.accept()
         except Exception:
            try:
               alert.dismiss()
            except Exception:
               pass
      except Exception:
         # no alert found within short time
         pass

      # Then handle in-page modal with OK (text may be 'OK' or 'Ok' or 'Ok ' etc.)
      try:
         ok_modal = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='OK' or normalize-space(text())='Ok' or normalize-space(text())='Ok ']")
               )
            )
         ok_modal.click()
      except Exception:
            # try a more generic button that closes a modal
         try:
            ok_modal = WebDriverWait(self.driver, 5).until(
               EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'btn') and (normalize-space(text())='OK' or normalize-space(text())='Ok' or normalize-space(text())='Close' or normalize-space(text())='Close')]"))
            )
            ok_modal.click()
         except Exception:
            pass

      # small pause to let UI stabilize
      time.sleep(1)
