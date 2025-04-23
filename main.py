from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os


# Replace the setup_driver function with this:
def setup_driver():
    """Setup and return a Chrome WebDriver instance."""
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start maximized

    # Use Service Manager to automatically download and manage ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)

    return driver

def google_search_example(driver, search_query):
    """Perform a simple Google search."""
    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search box
    try:
        # Accept cookies if the dialog appears (common in EU)
        cookies_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept all')]"))
        )
        cookies_button.click()
    except:
        # If no cookie dialog or it's different, just continue
        pass

    # Find and interact with the search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Type the search query and press Enter
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Get search results
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")

    # Print the titles of the first 5 search results
    print(f"Search results for '{search_query}':")
    for i, result in enumerate(search_results[:5], 1):
        try:
            title = result.find_element(By.CSS_SELECTOR, "h3").text
            print(f"{i}. {title}")
        except:
            continue


def take_screenshot(driver, filename="screenshot.png"):
    """Take a screenshot and save it to the given filename."""
    driver.save_screenshot(filename)
    print(f"Screenshot saved as {filename}")


def main():
    """Main function to run the automation script."""
    driver = setup_driver()

    try:
        # Perform a Google search
        google_search_example(driver, "Python Selenium automation")

        # Take a screenshot
        take_screenshot(driver, "search_results.png")

        # Wait for 3 seconds to see the results
        time.sleep(3)

    finally:
        # Always close the browser
        driver.quit()


if __name__ == "__main__":
    main()
