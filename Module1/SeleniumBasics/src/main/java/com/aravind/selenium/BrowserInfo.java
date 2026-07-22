package com.aravind.selenium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class BrowserInfo {

    public static void main(String[] args) {

        // Setup ChromeDriver
        WebDriverManager.chromedriver().setup();

        // Launch Chrome
        WebDriver driver = new ChromeDriver();

        // Open Google
        driver.get("https://www.google.com");

        // Print page title
        System.out.println("Title : " + driver.getTitle());

        // Print current URL
        System.out.println("URL : " + driver.getCurrentUrl());

        // Print page source length
        System.out.println("Page Source Length : " + driver.getPageSource().length());

        // Close browser
        driver.quit();
    }
}