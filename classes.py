from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Fridge:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def check_home_depot(self): # check home depot for current price
        try:
            driver = webdriver.Chrome()
            driver.get("http://www.homedepot.com")
            assert "Home Depot" in driver.title  # checks that website title is "Home Depot"
            elem = driver.find_element_by_class_name("SearchBox__input") # select search box on page
            elem.clear()
            elem.send_keys(str(self.model)) # input model number into search box
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source # make assertion if no result
            time.sleep(1) # wait 1 second for page to load
            price = driver.find_element_by_class_name("price__dollars") # locate price
            return price.get_attribute("textContent")
        finally:
            driver.quit() # close browser
    
    def check_lowes(self): # check lowes for current price
        try:
            # # change user agent to not headless browser
            # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            # options = webdriver.ChromeOptions()
            # options.add_argument(f'user-agent={user_agent}') # specify desired user agent
            # driver = webdriver.Chrome(chrome_options=options)
            driver = webdriver.Chrome()
            driver.get("https://www.lowes.com/search?searchTerm=" + str(self.model))
            time.sleep(1) # wait 1 second for page to load
            assert "No results found." not in driver.page_source # make assertion if no result 
            price = driver.find_element_by_xpath(".//span[@class='aPrice large']/aria-hidden") # locate price with span class
            return price.get_attribute("aria-hidden")
        finally:
            driver.quit() # close browser

    def check_samsung(self):
        if self.brand.upper() == "SAMSUNG":
            try:
                driver = webdriver.Chrome()
                driver.get("https://www.samsung.com/us/search/searchMain?listType=g&searchTerm=" + str(self.model))
                time.sleep(1) # wait 1 second for page to load
                assert "No results found." not in driver.page_source # make assertion if no result
                price = driver.find_element_by_xpath(".//span[@class='after epp-price']") # locate price with span class 
                return price.get_attribute("Content")
            finally:
                driver.quit() # close browser
        else:
            pass


if __name__ == "__main__":
    samsung = Fridge('Samsung','RF23R6201WW')
    print(samsung.check_lowes())