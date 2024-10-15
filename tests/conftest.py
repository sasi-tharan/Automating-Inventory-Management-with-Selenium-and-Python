import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Fixture to set up the Chrome WebDriver session
@pytest.fixture(scope="session")
def driver():
    # ChromeOptions for customizing Chrome WebDriver
    chrome_options = webdriver.ChromeOptions()
    # Use ChromeDriverManager to handle Chrome WebDriver setup
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()  # Maximize browser window
    yield driver  # Provide the WebDriver instance to tests
    driver.quit()  # Teardown: close browser after tests finish

@pytest.fixture(scope="module", autouse=True)
def login(driver):
    # Ensure login page is loaded
    driver.get("http://127.0.0.1:8000/")
    # Fill email and password fields and submit form
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email")))
    email_input.send_keys("admin@gmail.com")
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("admin@gmail.com")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "login")))
    login_button.click()
    yield  # No teardown needed for login state
# Fixture to refresh browser state after each test in the module
@pytest.fixture(scope="function", autouse=True)
def refresh_browser(driver):
    yield  # Allow the test to run
    # Refresh browser by navigating to the URL after each test function
    driver.get("http://127.0.0.1:8000/inventory/create")
