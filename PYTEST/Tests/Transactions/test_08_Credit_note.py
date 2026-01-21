import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Transactions.Credit_note import CreditNotePage

@allure.title("Generate Credit Note in IMS Application")
@allure.description("Logs in, navigates to the Credit Note section, selects a Ref Bill, and saves the Credit Note.")
def test_generate_credit_note(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        credit_note_page = CreditNotePage(driver)
        credit_note_page.create_credit_note()
        print("Credit Note created successfully.")

        allure.attach(driver.get_screenshot_as_png(), name="Credit_Note_Success_Screenshot",
            attachment_type=allure.attachment_type.PNG)
        print("Screenshot captured for successful Credit Note creation.")

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot",
            attachment_type=allure.attachment_type.PNG)
        allure.attach(str(e), name="Error Details",
            attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Credit Note test failed due to: {e}")
