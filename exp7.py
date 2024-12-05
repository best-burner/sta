from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to Amazon India
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    print("Navigated to Amazon.")

    # Search for a product (e.g., laptop)
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    print("Searched for 'laptop'.")

    # Wait for search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".s-main-slot .s-result-item"))
    )

    # Click the first product
    first_product = driver.find_element(By.CSS_SELECTOR, ".s-main-slot .s-result-item h2 a")
    first_product.click()
    print("Clicked on the first product.")

    # Switch to the new tab with the product details
    driver.switch_to.window(driver.window_handles[1])
    print("Switched to product details tab.")

    # Extract and print product details
    try:
        product_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        ).text
        print("Product Title:", product_title)
    except:
        print("Unable to fetch product title.")

    try:
        product_price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen").text
        print("Product Price:", product_price)
    except:
        print("Unable to fetch product price.")

except Exception as e:
    print("An error occurred:", e)
finally:
    # Wait a few seconds to observe the actions
    time.sleep(5)
    driver.quit()
    print("Test completed and browser closed.")
