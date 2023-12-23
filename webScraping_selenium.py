from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://automatetheboringstuff.com")
element = browser.find_elements('p')
print(element)
element.click()