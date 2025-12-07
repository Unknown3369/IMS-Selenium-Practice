import pytest
from PYTEST.pages.Login import login
from PYTEST.pages.Add_customer import addCustomer
import random
import uuid

def random_name():
   # short unique string using uuid
   return "cust_" + uuid.uuid4().hex[:8]

def random_address(length):
   letters = "abcdefghijklmnopqrstuvwxyz"
   return "".join(random.choice(letters) for _ in range(length))

def test_add_customer(driver):
   login_page = login(driver)
   add_customer = addCustomer(driver)

   login_page.perform_login("Testuser", "Test@1234")
   add_customer.open_add_customer()

   random_string = random_name()
   random_addr = random_address(12) 
   random_telephone = random.randint(00000000, 99999999)

   add_customer.add_customer(random_string, random_addr, "98" + str(random_telephone))
   print ("Customer added successfully!")
   