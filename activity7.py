import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class efs_funds_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_efs_funds(self):
        user = "groyce"
        pwd = "instructor1a"
        id_customer = "12056"
        id_category = "fund"
        id_description = "Fidelity Contrafund"
        id_acquired_value = "120000"
        id_acquired_date = "2014-06-12"
        id_recent_value = "160000"
        id_recent_date = "2017-10-31"
        timing = 5

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(timing)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(timing)
        driver.get("http://127.0.0.1:8000/investment")
        time.sleep(timing)
        driver.get("http://127.0.0.1:8000/investment/create")
        time.sleep(timing)
        elem = driver.find_element_by_id("id_customer")
        elem.send_keys(id_customer)
        elem = driver.find_element_by_id("id_category")
        elem.send_keys(id_category)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(id_description)
        elem = driver.find_element_by_id("id_acquired_value")
        elem.send_keys(id_acquired_value)
        elem = driver.find_element_by_id("id_acquired_date")
        elem.clear()
        elem.send_keys(id_acquired_date)
        elem = driver.find_element_by_id("id_recent_value")
        elem.send_keys(id_recent_value)
        elem = driver.find_element_by_id("id_recent_date")
        elem.clear()
        elem.send_keys(id_recent_date)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/form/button").click()
        time.sleep(timing)



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()