from selenium import webdriver

chrome_driver_path = "C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org")

# Find the event elements
event_elements = driver.find_elements_by_css_selector('#content div.section:nth-child(2) div.list-widgets.container ul.menu li a')

# Extract and print the dates of the events
for event_element in event_elements:
    date_element = event_element.find_element_by_tag_name("time")
    event_date = date_element.get_attribute("datetime").split("T")[0]
    print(event_date)

driver.close()
