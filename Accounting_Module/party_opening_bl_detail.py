from login_details import login_to_ims
from party_opening_bl import MainPage
from selenium.webdriver.common.by import By
import time

def party_opening_bl_details():
    # Login and get driver
    driver = login_to_ims()
    # Initialize MainPage with the logged-in driver
    party_opening = MainPage(driver)
    # Navigate through the app
    party_opening.open_accounting_module()
    party_opening.open_party_opening_bl()
    # Add party opening details
    party_opening.add_party_opening_details("REF62201585", 250000, "Automation Test Party Opening")
    # Wait before closing
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    party_opening_bl_details()