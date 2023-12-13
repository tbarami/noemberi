from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("http://www.google.com")

# You can add additional actions here if needed

# Close the browser window
driver.quit()