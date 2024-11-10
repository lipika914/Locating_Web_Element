from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class LoginValidation:
    def test_login(self):
        baseURL = "https://rahulshettyacademy.com/loginpagePractise/"
        driver = webdriver.Chrome()

        driver.get(baseURL)

        driver.implicitly_wait(20)

        # Find elements
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.NAME, "password")
        # Input data
        username.send_keys("rahulshettyacademy")
        password.send_keys("learning")
        singin = driver.find_element(By.XPATH,"//input[@name='signin']").click()

        checkout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='nav-item active']"))
        )
        if checkout_button.is_displayed():
            print("User logged in successfully.")
        else:
            print("Login failed or something went wrong.")




        driver.quit()


# Running the test
login = LoginValidation()
login.test_login()
