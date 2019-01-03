from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from selenium.webdriver.support.select import Select

#from ghost import Ghost

#opens the browser to this page
browser = webdriver.Chrome()
browser.get('https://www.kbb.com/used-cars/')

sleep(1)#need to sleep while waiting for webpage
f = open('out.txt','w')
sys.stdout = f

mnmbyYear = {}

#moves curser to year and starts for loop
walker = browser.find_element_by_xpath("//*[@id='yearDropdown0']")
walker.click()
years = walker.find_elements_by_tag_name('option')

for year in years:
    mnmbyYear[year.text] = {}

    walker.send_keys(Keys.ARROW_DOWN)
    walker.send_keys(Keys.ENTER)

    maker = browser.find_element_by_xpath("//*[@id='makeDropdown0']")
    maker.click()
    makes = maker.find_elements_by_tag_name('option')

    theMakes = maker.text.split()
    theMakes.pop(0)
    #print(year.text)
    #now we start on the makes
    for make in makes[1:]:

        maker.send_keys(Keys.ARROW_DOWN)
        maker.send_keys(Keys.ENTER)

        #now we can check all the models
        modeler = browser.find_element_by_xpath("//*[@id='modelDropdown0']")
        modeler.click()
        models = modeler.find_elements_by_tag_name('option')

        theModels = modeler.text.splitlines()
        theModels.pop(0)

        mnmbyYear[year.text][make.text] = theModels
        #print(make.text, theModels)
    print(mnmbyYear[year.text])
