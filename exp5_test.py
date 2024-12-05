from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the product display page with local file path
file_path = "file:///F:\sta\exp3\index.html"
driver.get(file_path)
time.sleep(3)

# Find all products on the page
products = driver.find_elements(By.CLASS_NAME, "product")
print(f"Total products found: {len(products)}")

# Loop through each product to check required elements
for i, product in enumerate(products, start=1):
    print(f"\nChecking Product {i}...")

    # Check for missing product name
    try:
        product_name = product.find_element(By.CLASS_NAME, "product-name")
        if not product_name.text.strip():
            print(f"Product {i} Failed: Name is missing.")
        else:
            print(f"Product {i} Passed: Name is present.")
    except Exception:
        print(f"Product {i} Failed: Could not find the product name.")

    # Check for missing price
    try:
        product_price = product.find_element(By.CLASS_NAME, "product-price")
        if not product_price.text.strip():
            print(f"Product {i} Failed: Price is missing.")
            if i == 3:
                print(f"Product {i}: Custom alert for missing price.")
                # Trigger a custom alert for the third product
                driver.execute_script("alert('Cannot proceed to buy because price not found');")
                time.sleep(20)  # Wait for the alert to display
                alert = driver.switch_to.alert
                alert.accept()  # Close the alert after displaying the message
        else:
            print(f"Product {i} Passed: Price is present.")
    except Exception:
        print(f"Product {i} Failed: Could not find the product price.")

    # Check for broken image
    try:
        product_img = product.find_element(By.CLASS_NAME, "product-img")
        if product_img.get_attribute("naturalWidth") == "0":
            print(f"Product {i} Failed: Image is broken.")
        else:
            print(f"Product {i} Passed: Image is present.")
    except Exception:
        print(f"Product {i} Failed: Could not find the product image.")
time.sleep(20)
# Keep the browser open for manual inspection
#print("Testing complete. The browser will remain open until you manually close it.")