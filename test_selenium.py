from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
print("SUCCESS:", driver.title)
driver.quit()