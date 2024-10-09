import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class LoginTests(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Go directly to the provided login URL
        self.driver.get("https://aim-game-frontend.vercel.app/")

    # proceeds with the login test steps.
    def login(self, email, password):

        """Reusable function to perform registration"""
        self.driver.find_element(By.NAME,"email").send_keys(email)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(By.TAG_NAME, "button").click()

    def test_valid_login(self):
        """Test login with valid input"""
        self.login("msaadikali@gmail.com", "Ali@177a")
        time.sleep(15)
        self.assertEqual(self.driver.current_url, "https://aim-game-frontend.vercel.app/dashboard")

    def test_invalid_email(self):
        """Test login with invalid email"""
        self.login("newuser@gmail.com", "Ali@177a")
        time.sleep(10)
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Invalid email or password")

    def test_invalid_password(self):
        """Test login with invalid password"""
        self.login("newuser@gmail.com", "Password@101")
        time.sleep(10)
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Invalid email or password")


    def test_empty_field(self):
        """Test login with invalid password"""
        self.login("", "")
        time.sleep(10)
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Email and password are required in the request body")


    def test_empty_email(self):
        """Test login with invalid password"""
        self.login("", "Ali@177a")
        time.sleep(10)
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Email and password are required in the request body")


    def test_empty_password(self):
        """Test login with invalid password"""
        self.login("newuser@gmail.com", "")
        time.sleep(10)
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Email and password are required in the request body")


    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()
