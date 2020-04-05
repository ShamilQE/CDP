import unittest
from selenium import webdriver

class Challenge1 (unittest.TestCase):

    # code to startup webdriver
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    # code to close webdriver
    def tearDown(self):
        self.driver.close()

    # code for our test steps
    def test_Challenge1(self):
        self.driver.get("https://www.google.com/")
        self.assertIn("Google", self.driver.title)

if __name__ == '__main__':
    unittest.main()









