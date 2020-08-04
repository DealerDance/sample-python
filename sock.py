# coding:utf-8
from selenium import webdriver

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);



driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
url = "http://10.10.15.120:30001"

driver.get(url)


# d1= driver.find_element_by_xpath("/html/body")
# d1.click()
#
# d2 = driver.find_element_by_id("register-username-modal")
# d2.click()
# d2.send_keys('aaa')
#
# d3 = driver.find_element_by_id("register-first-modal")
# d3.click()
# d3.send_keys('aaa')
#
# d4 =driver.find_element_by_id("register-last-modal")
# d4.click()
# d4.send_keys('aaa')
#
# d5 = driver.find_element_by_id("register-email-modal")
# d5.click()
# d5.send_keys('aaa')
#
# d6 = driver.find_element_by_id("register-password-modal")
# d6.click()
# d6.send_keys('aaa')
#
# d7 = driver.find_element_by_id("register-modal")
# d7.click()





