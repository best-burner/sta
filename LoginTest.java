
package test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class LoginTest {

    @DataProvider(name = "loginData")
    public Object[][] readCsvData() throws IOException {
        String filePath = "src/testdata/testdata.csv";
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;
        int rowCount = 0;
        while ((line = reader.readLine()) != null) {
            rowCount++;
        }
        reader.close();

        Object[][] data = new Object[rowCount - 1][2]; // Skip header row
        reader = new BufferedReader(new FileReader(filePath));
        reader.readLine(); // Skip the header

        int index = 0;
        while ((line = reader.readLine()) != null) {
            String[] fields = line.split(",");
            data[index][0] = fields[0];
            data[index][1] = fields[1];
            index++;
        }
        reader.close();
        return data;
    }

    @Test(dataProvider = "loginData")
    public void loginTest(String username, String password) {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\sarve\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"); // Replace with your ChromeDriver path
        WebDriver driver = new ChromeDriver();

        try {
            // Navigate to Sauce Demo login page
            driver.get("https://www.saucedemo.com/");

            // Find and interact with login elements
            WebElement usernameField = driver.findElement(By.id("user-name"));
            WebElement passwordField = driver.findElement(By.id("password"));
            WebElement loginButton = driver.findElement(By.id("login-button"));

            // Perform login
            usernameField.sendKeys(username);
            passwordField.sendKeys(password);
            loginButton.click();

            // Validate login success or failure
            boolean isSuccess = driver.getCurrentUrl().contains("inventory");
            if (isSuccess) {
                System.out.println("Login successful for Username: " + username);
            } else {
                WebElement errorMessage = driver.findElement(By.cssSelector("h3[data-test='error']"));
                System.out.println("Login failed for Username: " + username + ". Error: " + errorMessage.getText());
            }
        } catch (Exception e) {
            System.err.println("Error during login test: " + e.getMessage());
        } finally {
            // Close the browser
            driver.quit();
        }
    }
}

