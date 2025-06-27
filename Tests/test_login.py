import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    yield driver
    driver.quit()

def test_login(setup):
    page = LoginPage(setup)
    page.login("chandan_test1234@gmail.com", "Test@12345")
    assert "My Account" in setup.title
