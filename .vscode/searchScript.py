from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:/Users/huytr/Downloads/chromedriver_win32/chromedriver")

browser.get('https://en.wikipedia.org/wiki/Main_Page')

print("Enter a keyword to search on wikipedia: ", end='')
keyword = input()

elem = browser.find_element_by_id('searchInput')  # Find the search box
elem.send_keys(keyword + Keys.RETURN)


browser.quit()
# do something with the opened page
