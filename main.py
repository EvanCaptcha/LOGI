from selenium import webdriver
import threading
import requests
from random import randrange, randint
import random
import time
import string
import names
from selenium.webdriver.support.ui import Select
threads = 3
link = input("PATE THE LINK ASAP ROCKY! ")
def task():

    driver = webdriver.Chrome(executable_path=r'C:\Users\Evan\PycharmProjects\NDC\chromedriver.exe')
    while True:
        try:
            driver.delete_all_cookies()
            driver.get(link)
            r = requests.get(link)
            sku =r.text.split('"product_sku":["')[1].split('"],"')[0]
            driver.find_element_by_xpath('/html/body').click()
            time.sleep(0.2)
            driver.find_element_by_xpath('/html/body').click()
            time.sleep(0.26)
            driver.find_element_by_xpath('/html/body').click()
            driver.get(f'https://www.logitechg.com/bin/cart/create?sku_id={sku}&productId={sku}&quantity=3')
            time.sleep(2)
            driver.get('https://www.logitechg.com/bin/cart/view?t=1579859873184')
            time.sleep(3)
            try:
                driver.find_element_by_xpath('//*[@id="mm_modal"]/div[2]/div/div[3]/a').click()
            except:
                pass
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="dr_checkoutButton"]/div[1]/a').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="btnCreateAccount"]').click()
            time.sleep(1)
            def random_string_generator_variable_size(min_size, max_size, allowed_chars):
                return ''.join(random.choice(allowed_chars) for x in range(randint(min_size, max_size)))
            chars = string.ascii_letters
            rando = random_string_generator_variable_size(6, 12, chars)
            driver.find_element_by_xpath('//*[@id="email"]').send_keys(f'{rando}@evxn.io')
            name = names.get_full_name(gender='male')
            list = name.split(' ')
            first = list[0]
            last = list[1]
            driver.find_element_by_xpath('//*[@id="shippingName1"]').send_keys(first)
            driver.find_element_by_xpath('//*[@id="shippingName2"]').send_keys(last)
            randoAddy = random_string_generator_variable_size(3, 3, chars)
            driver.find_element_by_xpath('//*[@id="shippingAddress1"]').send_keys(f'{randoAddy} 21 Quaker Ln')
            apt = randrange(99)
            driver.find_element_by_xpath('//*[@id="shippingAddress2"]').send_keys(f'APT #{apt}')
            driver.find_element_by_xpath('//*[@id="shippingCity"]').send_keys('Chappaqua')
            driver.find_element_by_xpath('//*[@id="shippingPostalCode"]').send_keys('10514')

            def random_with_N_digits(n):
                range_start = 10 ** (n - 1)
                range_end = (10 ** n) - 1
                return randint(range_start, range_end)

            phoneNumber = random_with_N_digits(10)
            driver.find_element_by_xpath('//*[@id="shippingPhoneNumber"]').send_keys(phoneNumber)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="continueToPayment"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="ccNum"]').send_keys('4197394215553472')
            select = Select(driver.find_element_by_xpath('//*[@id="ccMonth"]'))
            select.select_by_value('10')
            select2 = Select(driver.find_element_by_xpath('//*[@id="ccYear"]'))
            select2.select_by_value('2024')
            driver.find_element_by_xpath('//*[@id="cardSecurityCode"]').send_keys('073')
            driver.find_element_by_xpath('//*[@id="checkoutButton"]').click()
            time.sleep(1)
            try:
                driver.find_element_by_xpath('//*[@id="rtavContinueButton"]').click()

            except:
                pass
            driver.find_element_by_xpath('//*[@id="submitBottom"]').click()
            driver.delete_all_cookies()
            time.sleep(10)


        except:
            print("An error has occured... Retrying!")



jobs = []
for i in range(0, int(threads)):
    jobs.append(threading.Thread(target=task))

# start  threads
for j in jobs:
    j.start()

# ensure all threads have been finished
for j in jobs:
    j.join()

