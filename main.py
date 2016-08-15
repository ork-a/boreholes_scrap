from selenium import webdriver
import os
from parse_input import ParseInput

path = os.path.abspath(input('Enter location (path) of chromedriver :'))
browser = webdriver.Chrome(executable_path=path)

print('App accepts input in form X Y. \nX is lower limit of parameter, Y respectively is upper limit. \n'
      'For no lower/upper limit enter NL, eg. NL 1000, 2000 NL or NL NL. \nONLY POSITIVE NUMBERS')
drill_depth = ParseInput(input("Enter depths you're interested in: ")).return_limits()
years = ParseInput(input("Enter years you're interested in: ")).return_limits()

url = 'http://otworywiertnicze.pgi.gov.pl/'
browser.get(url)

#clear JS fields
browser.find_element_by_id('glebokosc1').clear()
browser.find_element_by_id('glebokosc2').clear()
browser.find_element_by_id('rokWiercenia1').clear()
browser.find_element_by_id('rokWiercenia2').clear()

#pass arguments
browser.find_element_by_id('glebokosc1').send_keys(drill_depth[0])
browser.find_element_by_id('glebokosc2').send_keys(drill_depth[1])
browser.find_element_by_id('rokWiercenia1').send_keys(years[0])
browser.find_element_by_id('rokWiercenia2').send_keys(years[1])

#pass greater-than & smaller-than operators
browser.find_element_by_xpath('//*[@id="glebokosc1Oper"]/option[contains(text(), ">=")]').click()
browser.find_element_by_xpath('//*[@id="glebokosc2Oper"]/option[contains(text(), "<=")]').click()

browser.find_element_by_xpath('//*[@id="rokWiercenia1Oper"]/option[contains(text(), ">=")]').click()
browser.find_element_by_xpath('//*[@id="rokWiercenia2Oper"]/option[contains(text(), "<=")]').click()

#call
browser.find_element_by_css_selector('span[class=\"ui-button-text\"]').click()

