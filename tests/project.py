import pytest
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load data from Excel file
def load_test_data(filename):
    # Read the Excel file
    data = pd.read_excel(filename)
    # Convert to list of tuples
    return [tuple(row) for row in data.to_numpy()]

# Parameterized test function for single product
@pytest.mark.parametrize("name, description, quantity, price, status", load_test_data('test_data.xlsx'))
def test_create_projects(driver, name, description, quantity, price, status):
    wait = WebDriverWait(driver, 10)

    # Wait and click on the add button
    nav_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//nav[@id='sidebar']/ul/li[2]/a/span")))
    nav_button.click()

    add_button = wait.until(EC.element_to_be_clickable((By.ID, "add-stock")))
    add_button.click()

    # Fill in the form fields
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "description").send_keys(description)
    driver.find_element(By.ID, "quantity").send_keys(quantity)
    driver.find_element(By.NAME, "price").send_keys(price)
    driver.find_element(By.NAME, "status").send_keys(status)

    driver.find_element(By.ID, "save").click()

