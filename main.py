import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import random
load_dotenv(dotenv_path='.env')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.instagram.com/')


your_username = os.getenv('USERNAME_INSTA')
your_password = os.getenv('PASSWORD_INSTA')
account_to_follow = os.getenv('ACCOUNT_TO_FOLLOW')
current_follower_count=os.getenv('CURRENT_FOLLOWER_COUNT')

time.sleep(5)
username_field = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
username_field.send_keys(your_username)
password_field = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
password_field.send_keys(your_password)
log_in_btn = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button')
log_in_btn.click()

time.sleep(10)
not_now_btn = driver.find_element(By.XPATH,'//div[contains(text(),"Not now")]')
not_now_btn.click()
time.sleep(5)
driver.get(f'https://www.instagram.com/{account_to_follow}/')
time.sleep(3)
follower_click= driver.find_element(By.XPATH,f'//span[contains(text(),"{current_follower_count}")]')
follower_click.click()
time.sleep(5)

follow_div=driver.find_elements(By.XPATH, "//div[text()='Follow']")
if follow_div:
    follow_div.pop(0)

def scroll():
    scroll_div=driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scroll_div)
    after_scroll_follow_div = driver.find_elements(By.XPATH, "//div[text()='Follow']")
    for i in range(len(after_scroll_follow_div)):
        if after_scroll_follow_div[i] not in follow_div:
            follow_div.append(after_scroll_follow_div[i])
    print(len(follow_div))
    return follow_div

for i in range(5):
    current_div=scroll()
    current_div[i].click()
    time.sleep(random.randint(1,15))



