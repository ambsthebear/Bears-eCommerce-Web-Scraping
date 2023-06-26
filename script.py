from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# CSV setup
file=open("laptops.csv", "w", newline="")
writer=csv.writer(file)
writer.writerow(["id", "name", "price", "specifications", "number of reviews"])

# SCRAPER setup for page
browser_driver=Service("C:\\Users\\16306\\OneDrive\\Desktop\\chromedriver.exe")
scraper=webdriver.Chrome(service=browser_driver)
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

# FIND elements using developer tools
    # laptop card is class of "col-sm-4 col-lg-4 col-md-4"
    # name is class of "title"
    # price is class of "pull-right price"
    # spec is class of "description"
    # review number is class of "pull-right"
    # page turner is 

# CREATE wait to make sure data loads before scraping
# wait = WebDriverWait(scraper, 10)
# element_to_watch = scraper.find_element(By.CLASS_NAME, "row")
# wait.until(EC.visibility_of(element_to_watch))

# SCRAPE the page
unique_id=1
while True:
    gadgets=scraper.find_elements(By.CLASS_NAME, "col-sm-4 col-lg-4 col-md-4")
    for gadget in gadgets:
        name=gadget.find_element(By.CLASS_NAME, "title")
        price=gadget.find_element(By.CLASS_NAME, "pull-right price")
        specifications=gadget.find_element(By.CLASS_NAME, "description")
        number_of_reviews=gadget.find_element(By.CLASS_NAME, "pull-right")
        writer.writerow(
            [unique_id, name.text, price.text, specifications.text, number_of_reviews.text])
        unique_id +=1
    try:
        element=scraper.find_element(By.CSS_SELECTOR, "body > div.wrapper > div.container.test-site > div > div.col-md-9 > nav > ul > li:nth-child(15) > a")
        element.click()
    except NoSuchElementException:
        break

# QUIT browser and close file
