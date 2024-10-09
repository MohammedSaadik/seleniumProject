from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class RegisterTests(unittest.TestCase):
    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # Go directly to the provided register URL
        self.driver.get("https://aim-game-frontend.vercel.app/register")

    # proceeds with the register test steps.
    def register(self, name, email, password, confirm_password):
        """Reusable function to perform registration"""
        self.driver.find_element(By.NAME,"name").send_keys(name)
        self.driver.find_element(By.NAME,"email").send_keys(email)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(By.NAME,"confirm_password").send_keys(confirm_password)
        self.driver.find_element(By.TAG_NAME, "button").click()

    def test_valid_registration(self):
        """Test registration with valid inputs"""
        self.register("Test User", "newuser@example.com", "Password@100", "Password@100")
        # Assertion for successful registration
        time.sleep(20)
        self.assertEqual(self.driver.current_url, "https://aim-game-frontend.vercel.app/register/landing")
        # success_message = self.driver.find_element(By.TAG_NAME, "successMessage").text
        # self.assertEqual(success_message, "Registration successful.")

    def test_invalid_emailFormat(self):
        """Test registration with invalid email format"""
        self.register("Test User", "newuserexample", "Password@100", "Password@100")
        time.sleep(10)
        # Assertion for successful registration
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Invalid email format.")

    def test_password_mismatch(self):
        """Test registration with mismatched passwords"""
        self.register("Test User2", "newuser2@example.com", "Password@101", "differentpass")
        time.sleep(5)
        # Assertion to check for an error message
        error_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(error_message, "Passwords do not match")

    def test_weak_password(self):
        """Test registration with weak password"""
        self.register("Test User3", "new3user@example.com", "password103", "password103")
        time.sleep(5)
        # Assertion for successful registration
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, a number, and a special character.")

    def test_existing_email(self):
        """Test registration with existing email"""
        self.register("Test User4", "msaadikali@gmail.com", "Password@104", "Password@104")
        time.sleep(10)
        # Assertion for successful registration
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Email already exists")

    def test_existing_name(self):
        """Test registration with existing name"""
        self.register("Test User", "newuser5@example.com", "Password@105", "Password@105")
        time.sleep(10)
        # Assertion for successful registration
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Username already exists")

    def test_empty_fields(self):
        """Test registration with empty fields"""
        self.register("", "", "", "")
        time.sleep(10)
        # Assertion for successful registration
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Each field is required.")

    def test_empty_name(self):
        """Test registration with empty name fields"""
        self.register("", "newuser6@example.com", "Password@106", "Password@106")
        time.sleep(20)
        # Assertion for successful registration
        success_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(success_message, "Name field is required.")

    def test_empty_password(self):
        """Test registration with empty fields"""
        self.register("Test User7", "newuser7@example.com", "", "")
        time.sleep(10)
        # Assertion for successful registration
        error_message = self.driver.find_element(By.CLASS_NAME, "text-red-500").text
        self.assertEqual(error_message, "Password field is required.")

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

