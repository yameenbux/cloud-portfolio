from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ✅ Path to your actual chromedriver.exe file
driver_path = "C:/Users/ybux/Documents/Tools/chromedriver-win64/chromedriver.exe"

# ✅ Launch the Chrome browser using Selenium
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# ✅ Open the Argos Laptops category page
driver.get("https://www.argos.co.uk/browse/technology/laptops-and-pcs/laptops/c:30049/")

# ⏱️ Wait for 5 seconds to allow the page to fully load
time.sleep(5)

# ✅ Scrape all product titles using their CSS class
products = driver.find_elements(By.CSS_SELECTOR, "div.ProductCardstyles__Title-sc-__sc-1ivm0s7-6")

# ✅ Scrape all prices using their CSS class
prices = driver.find_elements(By.CSS_SELECTOR, "div.ProductCardPriceNowstyles__Price-sc-__sc-1o2ay8a-1")

# ✅ Print each product name + price pair
for i in range(min(len(products), len(prices))):
    print(f"{products[i].text} - {prices[i].text}")

# Print HTML to check if product info is there
print(driver.page_source)

driver.quit()


# ✅ Close the browser after scraping
driver.quit()
