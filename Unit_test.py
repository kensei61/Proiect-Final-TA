import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class TestDemoBlaze(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_01_deschide_website(self):
        self.driver.get("https://demoblaze.com/")
        self.assertIn("STORE", self.driver.title)

    def test_02_login(self):
        self.driver.get("https://demoblaze.com/")
        self.driver.find_element(By.ID, "login2").click()
        sleep(1)
        self.driver.find_element(By.ID, "loginusername").send_keys("Ioan_TA37")
        self.driver.find_element(By.ID, "loginpassword").send_keys("ta37")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
        sleep(1)

#aici urmeaza restul testelor

if __name__ == "__main__":
    unittest.main()
