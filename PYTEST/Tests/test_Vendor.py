# tests/test_Vendor.py
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PYTEST.pages.Login import login
from PYTEST.pages.Add_Vendor import Vendor
import random
import uuid

# noinspection PyBroadException
@allure.title("Create Vendor in IMS Application")
@allure.description("Logs in, navigates to Vendor Master, and creates a new vendor record.")

def random_name():
    return "Vend_" + uuid.uuid4().hex[:8]

def random_address(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for _ in range(length))

def random_vat_no():
    random_vat = random.randint(100000000, 999999999)
    return str(random_vat)

def random_email():
    return "Vend_" + uuid.uuid4().hex[:8] + "@gmail.com"

def random_mobile():
    return "98" + str(random.randint(10000000, 99999999))


def test_create_vendor(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    login_page.perform_login("Testuser", "Test@1234")
    print("Logged into IMS")

    random_name_str = random_name()
    random_addr = random_address(12)
    random_vat = random_vat_no()
    random_email_str = random_email()
    random_mobile_str = random_mobile()

    vendor = Vendor(driver)
    vendor.create_vendor(
        name=random_name_str,
        address=random_addr,    
        vat_no=random_vat,
        email=random_email_str,
        mobile=random_mobile_str)
    print("Vendor creation process completed")

    # --- Step 3: Verify success message ---
    success_message = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Vendor saved successfully')]"))
    )
    assert success_message.is_displayed(), "Vendor creation failed"
    print("Vendor created successfully and verified.")
