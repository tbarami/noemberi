from selenium import webdriver

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

# Open Google
driver.get("http://www.google.com")

# You can add additional actions here if needed

# Close the browser window
driver.quit()
