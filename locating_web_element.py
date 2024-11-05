from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class locateElement:
    def test(self):
        baseURL = "https://rahulshettyacademy.com/loginpagePractise/"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.NAME,"password")
        userType = driver.find_element(By.CSS_SELECTOR, "#usertype")
        selectClass = driver.find_element(By.CLASS_NAME,"form-control")
        sending = driver.find_element(By.XPATH,"//input[@name='signin']")
        if username:
            print("Found element: Username ")

        if password:
            print("Found element: Password")

        if userType:
            print("Found element: User Type")

        if selectClass:
            print("Found element: Select Class")

        if sending:
            print("Found element: Sending")

       # time.sleep(5)


find_element = locateElement()
find_element.test()