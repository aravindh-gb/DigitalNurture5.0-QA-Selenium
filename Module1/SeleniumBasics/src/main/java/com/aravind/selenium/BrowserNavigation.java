package com.aravind.selenium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class BrowserNavigation {
    public static void main(String[] args) throws InterruptedException {

    // Setup ChromeDriver
    WebDriverManager.chromedriver().setup();

    // Launch Chrome browser
    WebDriver driver = new ChromeDriver();

    // Open Google
    driver.get("https://www.google.com");

    Thread.sleep(2000);

    // Navigate to GitHub
    driver.navigate().to("https://github.com");

    Thread.sleep(2000);

    // Go Back
    driver.navigate().back();

    Thread.sleep(2000);

    // Go Forward
    driver.navigate().forward();

    Thread.sleep(2000);

    // Refresh
    driver.navigate().refresh();

    Thread.sleep(2000);

    // Close browser
    driver.quit();
}
    
    
}
