from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# Navigate to Amazon
driver.get("https://www.amazon.com/")
# search box
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys(
    "sony wf-1000xm4"
)
## click search button
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

## Multiple items info, single item: name, price and more link #

item_blocks = driver.find_elements(
    By.XPATH,
    "//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/ancestor-or-self::div[5]",
)

## To calculate length of xpaths returned #
blocks_count = len(item_blocks)

## All Data #
data = []

for item in item_blocks:
    try:
        item_name = item.find_element(
            By.XPATH, ".//text()[contains(., 'Sony')]/parent::node()"
        ).text
        item_price = item.find_element(
            By.XPATH, './/descendant::span[@class="a-price-whole"][1]'
        ).text
        
        item_link = item.find_element(
            By.XPATH, ".//text()[contains(., 'Sony')]/ancestor-or-self::a[1][@href]"
        ).get_attribute("href")
        # print("=================================================================")
        # print("item_name: ", item_name)
        # print('item_price: ', item_price + ".99")
        # print("item_link: ", item_link)
        # print("=================================================================")
        data.append({
            'item_name': item_name,
            'item_price': item_price,
            'item_link': item_link
        })
    except NoSuchElementException:
        print("One element not found! skipping to next one!")
        continue
    
# print(data)

i=0
while i < len(data):
    # print(data[i]['item_name'])
    item_link = data[i]['item_link']
    try:
        driver.get(item_link)
        reviews = driver.find_elements(By.XPATH, '//*[@data-hook="review"]')
        print("===============================")
        for review in reviews:
            customer_name = review.find_element(By.XPATH, './/descendant::*[@class="a-profile-name"]').text
            print(customer_name)
    except NoSuchElementException:
        print("Review for one link for skipped")
        continue
    i=i+1
    

time.sleep(30000)
driver.close()



## Testing Area #

    ## this will get html, which prints #
    # item_price_html = item_price.get_attribute('outerHTML')
