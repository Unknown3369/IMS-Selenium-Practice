This Repository is for practice purpose only.

Selenium Basic Practice implementation - IMS Software

Tested Link:
  https://stc21.variantqa.himshang.com.np/#/pages/dashboard


Install framework:
  pip install selenium
  pip install pytest
  pip install allure-pytest

To Run the tests in Terminal:-
    To Run the Tests: 
      pytest --alluredir=allure-results -v -s --disable-warnings
    To View the Report:
      allure serve allure-results
    To Create HTML Reports:
      allure generate


Forder Structure:

├───.pytest_cache
│   └───v
│       └───cache
├───.vscode
├───Accounting_Module
│   └───__pycache__
├───allure-report
│   ├───data
│   │   ├───attachments
│   │   └───test-cases
│   ├───export
│   ├───history
│   ├───plugin
│   │   ├───behaviors
│   │   ├───packages
│   │   └───screen-diff
│   └───widgets
├───allure-results
├───IMS
├───PYTEST
│   ├───.pytest_cache
│   │   └───v
│   │       └───cache
│   ├───pages
│   │   ├───Accounting
│   │   │   └───__pycache__
│   │   ├───Masters
│   │   │   └───__pycache__
│   │   ├───Reports
│   │   │   ├───Inventory_Reports
│   │   │   │   └───__pycache__
│   │   │   ├───Purchase_Report
│   │   │   │   └───__pycache__
│   │   │   ├───Sales_Report
│   │   │   │   └───__pycache__
│   │   │   ├───Vat_Report
│   │   │   │   └───__pycache__
│   │   │   └───__pycache__
│   │   ├───Transactions
│   │   │   └───__pycache__
│   │   └───__pycache__
│   ├───tests
│   │   ├───.pytest_cache
│   │   │   └───v
│   │   │       └───cache
│   │   ├───Accounting
│   │   │   └───__pycache__
│   │   ├───Masters
│   │   │   └───__pycache__
│   │   ├───Reports
│   │   │   ├───Inventory_Report
│   │   │   │   └───__pycache__
│   │   │   ├───Purchase_Report
│   │   │   │   └───__pycache__
│   │   │   ├───Sales_Report
│   │   │   │   └───__pycache__
│   │   │   ├───Vat_Report
│   │   │   │   └───__pycache__
│   │   │   └───__pycache__
│   │   ├───Transactions
│   │   │   └───__pycache__
│   │   └───__pycache__
│   └───__pycache__
├───screenshots
└───__pycache__