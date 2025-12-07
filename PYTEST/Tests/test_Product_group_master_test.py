import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Add_Product_Group_Master import AddProductGroupMasterPage
import random

# noinspection PyBroadException
@allure.title("Add Product Group in IMS Application")
@allure.description("Logs in, navigates to Product Group Master page, selects parent group, and adds a new product group named 'Hygiene'.")

def random_group_name():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "Group_"+"".join(random.choice(letters) for _ in range(6))

def test_add_product_group_master(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("✅ Logged into IMS")

        add_group = AddProductGroupMasterPage(driver)
        add_group.navigate_to_add_product()

        add_group.select_item_group()

        add_group.fill_group_details_and_save(
            group_name=random_group_name(),
            recommended_margin=str(random.randint(5, 20)),
            shelf_life=str(random.randint(15, 90))
        )
        print("✅ Product group added successfully.")

        # Screenshot for success proof
        allure.attach(driver.get_screenshot_as_png(), name="Add_Product_Group_Success", attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        # Capture screenshot and log error details for Allure
        allure.attach(driver.get_screenshot_as_png(), name="Add_Product_Group_Error", attachment_type=allure.attachment_type.PNG)
        allure.attach(str(e), name="Error Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"❌ Test failed due to: {e}")
