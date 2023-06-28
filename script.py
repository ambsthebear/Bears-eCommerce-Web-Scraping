from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# FIND elements using developer tools
    # laptop card is class of "col-sm-4 col-lg-4 col-md-4" or "thumbnail" or "caption"
    # name is class of "title"
    # price is class of "pull-right price" or plt "$" or selector "body > div.wrapper > div.container.test-site > div > div.col-md-9 > div > div:nth-child(2) > div > div.caption > h4.pull-right.price"
    # spec is class of "description"
    # review number is class of "pull-right"
    # page turner is plt "Next »" or "›"
    # cookies banner is class of "acceptCookies"
    
# CSV setup
file=open("laptops.csv", "w", newline="")
writer=csv.writer(file)
writer.writerow(["id", "name", "price", "specifications", "number of reviews"])

# SCRAPER setup for page
browser_driver=Service("C:\\Users\\16306\\OneDrive\\Desktop\\chromedriver.exe")
scraper=webdriver.Chrome(service=browser_driver)
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

# CREATE wait to make sure data loads before scraping
wait = WebDriverWait(scraper, 10)
element_to_watch = scraper.find_element(By.CLASS_NAME, "acceptCookies")
wait.until(EC.element_to_be_clickable(element_to_watch))
element_to_watch.click()

# SCRAPE the page
unique_id=1
while True:
    gadgets=scraper.find_elements(By.CLASS_NAME, "col-sm-4.col-lg-4.col-md-4")
    for gadget in gadgets:
        name=gadget.find_element(By.CLASS_NAME, "title")
        price=gadget.find_element(By.CLASS_NAME, "pull-right.price")
        specifications=gadget.find_element(By.CLASS_NAME, "description")
        number_of_reviews=gadget.find_element(By.CLASS_NAME, "ratings").find_element(By.CLASS_NAME, "pull-right")
        writer.writerow(
            [unique_id, name.text, price.text, specifications.text, number_of_reviews.text])
        unique_id +=1
    try:
        element=scraper.find_element(By.PARTIAL_LINK_TEXT, "›")
        element.click()
    except NoSuchElementException:
        break

# QUIT browser and close file
file.close()
scraper.quit()
