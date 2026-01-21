from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PYTEST.pages.Login import login
from PYTEST.pages.Masters.Add_Vendor import addVendor
import random
import uuid
import csv
import os


def random_name():
    return "Vend_" + uuid.uuid4().hex[:8]

def random_address(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(letters) for _ in range(length))


def random_vat_no():
    return str(random.randint(100000000, 999999999))


def random_email():
    return "Vend_" + uuid.uuid4().hex[:8] + "@gmail.com"


def random_mobile():
    return "98" + str(random.randint(10000000, 99999999))


# ---------------- CSV Utility ----------------
def write_vendor_to_csv(data, file_name="vendors.csv"):
    file_exists = os.path.isfile(file_name)

    with open(file_name, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)


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

    vendor = addVendor(driver)
    vendor.add_vendor(
        vendor_name=random_name_str,
        vendor_address=random_addr,
        vendor_vat_no=random_vat,
        vendor_email=random_email_str,
        vendor_mobile=random_mobile_str
    )
    print("Vendor creation process completed")

    # Verify success message
    success_message = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Vendor saved successfully')]")
        )
    )
    assert success_message.is_displayed(), "Vendor creation failed"
    print("Vendor created successfully and verified.")

    # ---------------- Write data to CSV ----------------
    vendor_data = {
        "MainGroup": "SUPPLIER",
        "ACNAME": random_name_str,
        "Address": random_addr,
        "VATNO": random_vat,
        "PARTYTYPE": "Supplier"
    }

    write_vendor_to_csv(vendor_data)
    print("Vendor data written to CSV successfully")
