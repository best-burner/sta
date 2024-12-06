from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000")
# Test case: Attempt to log in with invalid credentials
def test_invalid_login():
   driver.get("http://127.0.0.1:5000")

   username_field = driver.find_element("name", "username")
   password_field = driver.find_element("name", "password")
# Input invalid credentials
   username_field.send_keys("wronguser")
   password_field.send_keys("wrongpass")
# Submit the login form
   password_field.send_keys(Keys.RETURN)
# Wait for the alert to show up
   time.sleep(2)
# Check for alert by switching to alert and getting the text
   alert_text = driver.switch_to.alert.text

   if "Invalid username or password" in alert_text:
      print("Test Case Passed: Invalid login warning displayed.")
   else:
      print("Test Case Failed: No invalid login warning displayed.")
# Close the alert
   driver.switch_to.alert.accept()

def test_valid_login():
   driver.get("http://127.0.0.1:5000") 
   username_field = driver.find_element("name", "username")
   password_field = driver.find_element("name", "password")
# Input valid credentials
   username_field.send_keys("admin")
   password_field.send_keys("password123")
# Submit the login form
   password_field.send_keys(Keys.RETURN)
# Wait for the alert to show up
   time.sleep(2)
# Check for alert by switching to alert and getting the text
   alert_text = driver.switch_to.alert.text
   if "Login successful" in alert_text:
       print("Test Case Passed: Valid login successful.")
   else:
       print("Test Case Failed: No success message displayed.")
   driver.switch_to.alert.accept()
test_invalid_login() 
time.sleep(1) # Short pause between tests
test_valid_login() # Test with valid credentials
# Close the browser
driver.quit()