from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://gabrielecirulli.github.io/2048/")
element = driver.find_element_by_tag_name('body')
direction = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3:Keys.LEFT}
driver.find_element_by_class_name('grid-container').click()
for i in range(100):
    element.send_keys(direction[i % 4])
    print("Playing")
    time.sleep(0.3)