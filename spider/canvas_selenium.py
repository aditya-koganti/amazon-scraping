from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Navigate to Amazon
driver.get('https://canvas.slu.edu/')

# username & password
driver.find_element(By.XPATH, '//input[@name = "username"]').send_keys("akoganti")
driver.find_element(By.XPATH, '//*[@id="okta-signin-password"]').send_keys("Fall2022@@@@")
# submit button
driver.find_element(By.XPATH, '//*[@id="okta-signin-submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="form71"]/div[2]/input').click()
time.sleep(15)

# assignment link
driver.get('https://canvas.slu.edu/courses/43644/assignments/355313')
# click perusual
driver.find_element(By.XPATH, '//*[@id="tool_form"]/div/div[1]/div/button').click()
time.sleep(3)

# shift to old tab and then to persual tab back
window_handles = driver.window_handles
driver.switch_to.window(window_handles[0])
driver.switch_to.window(window_handles[1])

time.sleep(7)
# 


element = driver.find_element(By.XPATH, '//*[@id="viewer"]')
element.click()
sample_inpage_e = driver.find_element(By.XPATH, '//*[@id="pages-container"]/div[3]/div[1]/span[2]')
print('sample_inpage_e.text: ', sample_inpage_e.text)
sample_inpage_e.click()
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", sample_inpage_e)
# driver.execute_script("arguments[0].scrollIntoView();", sample_inpage_e)

x=1
# height = len(driver.find_element(By.XPATH, '//*[@id="pages-container"]//text()'))
height = 800
while True:
    s_xpath = f'(//*[@id="pages-container"]//span)[{x}]'
    sample_inpage_es = driver.find_element(By.XPATH, s_xpath )
    driver.execute_script("arguments[0].scrollIntoView();", sample_inpage_es)
    time.sleep(25)
    x = x+1
    s_xpath = f'(//*[@id="pages-container"]//span)[{x}]'
    if not driver.find_element(By.XPATH, s_xpath):
        break





# page_height = driver.execute_script("return document.body.scrollHeight")
# n = 0
# while True:
#     current_position = driver.execute_script('return window.scrollY')
#     print(current_position)
#     new_position = current_position + page_height/10
#     print(new_position)
#     print(page_height)
#     c=n
#     n+=100
#     scroll_script = f"window.scrollTo({c}, {n});"
#     driver.execute_script(scroll_script)
#     time.sleep(5)
#     max = current_position
    
#     if max >= page_height:
#         break
    

time.sleep(3000)
driver.close()

