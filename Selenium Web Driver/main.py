from selenium import webdriver


chrome_driver_path = "C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.google.com")
