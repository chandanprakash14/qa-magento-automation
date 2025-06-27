import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.account_page import AccountPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    yield driver
    driver.quit()

def test_change_password(setup):
    login = LoginPage(setup)
    login.login("chandan_test1234@gmail.com", "Test@12345")
    account = AccountPage(setup)
    account.change_password("Test@12345", "Test@54321")
    assert "You saved the account information." in setup.page_source
