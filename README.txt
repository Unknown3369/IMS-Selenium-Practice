This Repository is for practice purpose only.

Selenium Basic Practice implementation - IMS Software

Tested Link:
  https://redmiims.webredirect.himshang.com.np/#/pages/dashboard
  https://redmiims.variantqa.himshang.com.np/#/pages/dashboard

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
├───allure-results
├───IMS
├───PYTEST
│   ├───.pytest_cache
│   │   └───v
│   │       └───cache
│   ├───pages
│   │   └───__pycache__
│   ├───tests
│   │   ├───.pytest_cache
│   │   │   └───v
│   │   │       └───cache
│   │   └───__pycache__
│   └───__pycache__
├───screenshots
└───__pycache__