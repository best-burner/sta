from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()  # Specify the path to your chromedriver

try:
    # Navigate to Amazon homepage
    driver.get("https://www.amazon.in")
    start_time = time.time()

    # Wait for the search box to be clickable
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox')))
    
    # Enter search keyword and submit
    keyword = "laptop"
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(keyword)
    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()
    
    # Measure the page load time
    end_time = time.time()
    page_load_time = (end_time - start_time) * 1000
    print(f"Page Load Time: {page_load_time:.2f} milliseconds")

finally:
    # Close the browser
    driver.quit()
