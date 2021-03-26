from selenium import webdriver
from selenium.webdriver.common.by import By
from Framework.pages.home.login_page import LoginPage
import unittest
import pytest

import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.refresh()
        self.lp.login("standard_user", "secret_sauce")
        result = self.lp.verifyLoginSuccessful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("standard_user", "secret_sauce1")
        result = self.lp.verifyLoginFailed()
        assert result == True

