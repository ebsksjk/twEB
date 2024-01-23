from selenium import webdriver 
  
# Create a FirefoxOptions object 
options = webdriver.FirefoxOptions() 
  
# Set the Firefox browser to run in headless mode 
options.headless = True
  
# Create a WebDriver instance with the specified options 
driver = webdriver.Firefox(options=options) 
  
# Navigate to a website 
driver.get("http://dr-navigator.de") 
  
# Perform some automation tasks 
title = driver.title 
print("Title of the webpage:", title) 
  
# Close the WebDriver when done 
driver.quit() 

