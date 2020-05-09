from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Fridge:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def check_home_depot(self): # check home depot website for current price
        try:
            driver = webdriver.Chrome()
            driver.get("http://www.homedepot.com")
            assert "Home Depot" in driver.title  # checks that website title is "Home Depot"
            elem = driver.find_element_by_class_name("SearchBox__input") # select search box on page
            elem.clear()
            elem.send_keys(str(self.model)) # input model number into search box
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source # make assertion if no results
            time.sleep(3) # seconds
            price = driver.find_element_by_class_name("price__dollars") # locate current price
            return price.get_attribute("textContent")
        finally:
            driver.quit() # close browser
    
    def check_lowes(self): # check lowes website for current price
        try:
            driver = webdriver.Chrome()
            driver.get("http://www.lowes.com")
            assert "Home Improvement" in driver.title  # checks website title
            #elem = driver.find_element_by_class_name("input-group btn-left") # select search box on page
            elem = driver.find_element_by_xpath(".//div[@class='input-group btn-left']/input")
            elem.clear()
            elem.send_keys(str(self.model)) # input model number into search box
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source # make assertion if no results
            time.sleep(3) # seconds
            price = driver.find_element_by_class_name("aria-hidden")
            return price
        finally:
            driver.quit() # close browser

if __name__ == "__main__":
    samsung = Fridge('Samsung','RF23R6201WW')
    print(samsung.check_home_depot())