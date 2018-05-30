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

sleep(1)
f = open('out.txt','w')
sys.stdout = f

mnm = {}

#moves curser to year and starts for loop
walker = browser.find_element_by_xpath("//*[@id='yearDropdown0']")
walker.click()
years = walker.find_elements_by_tag_name('option')

for option in range(0,len(years)-1):
    walker.send_keys(Keys.ARROW_DOWN)
    walker.send_keys(Keys.ENTER)

    maker = browser.find_element_by_xpath("//*[@id='makeDropdown0']")
    maker.click()
    makes = maker.find_elements_by_tag_name('option')

    theMakes = maker.text.split()
    theMakes.pop(0)

    #now we start on the makes
    for y in range(0,len(makes)-1):
        maker.send_keys(Keys.ARROW_DOWN)
        maker.send_keys(Keys.ENTER)
        #checks each make from the list and adds it to the dict of makes with an empty model lsit
        for x in theMakes:
            if x not in mnm:
                mnm[x] = []
        #now we can check all the models
        modeler = browser.find_element_by_xpath("//*[@id='modelDropdown0']")
        modeler.click()
        models = modeler.find_elements_by_tag_name('option')

        theModels = modeler.text.split()
        theModels.pop(0)
        print(theModels)


    #if option == 0:
    #    adam = walker.text.split()
    #    adam.pop(0)
