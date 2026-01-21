import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@allure.feature("Add Product Group Master")
class AddProductGroupMasterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    # --- Navigate to Add Product Group page ---
    @allure.step("Navigate to Add Product Group Master page")
    def navigate_to_add_product(self):
        try:
            inventory_info = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Inventory Info")))
        except TimeoutException:
            inventory_info = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Inventory Info')]")))
        ActionChains(self.driver).move_to_element(inventory_info).perform()
        time.sleep(2)

        product_master = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Product Group Master")))
        product_master.click()
        time.sleep(3)

        add_product_group_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='create' and contains(., 'Add Product Group')]")))
        add_product_group_button.click()
        print("Clicked on Add Product Group button.")
        time.sleep(2)

    # --- Select Parent Group ---
    @allure.step("Select Item Group as OCR test")
    def select_item_group(self):
        item_group_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-icon[normalize-space(text())='open_in_new']")))
        item_group_icon.click()
        time.sleep(1)

        main_group_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-autocomplete='list' and @type='text']")))
        main_group_input.send_keys("OCR")
        body_care_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='OCR test']")))
        body_care_option.click()
        ok_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Ok']")))
        ok_button.click()
        print("Selected parent group: OCR test.")
        time.sleep(2)

    # --- Fill Group Details ---
    @allure.step("Fill group details and save Product Group")
    def fill_group_details_and_save(self, group_name, recommended_margin, shelf_life):
        print("Filling Product Group details...")

        # --- Group Name ---
        group_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='groupName']")))
        group_name_field.clear()
        group_name_field.send_keys(group_name)
        print(f"Entered Group Name: {group_name}")

        # --- Recommended Margin ---
        margin_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='recommendedMargin']")))
        margin_field.clear()
        margin_field.send_keys(recommended_margin)
        print(f"Entered Recommended Margin: {recommended_margin}")

        # --- Shelf Life ---
        shelf_life_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='shelfLife']")))
        shelf_life_field.clear()
        shelf_life_field.send_keys(shelf_life)
        print(f"Entered Shelf Life: {shelf_life}")

        # --- Click Save Button ---
        save_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='save' and normalize-space(text())='SAVE']")))
        save_button.click()
        print("Clicked Save button.")
        time.sleep(2)