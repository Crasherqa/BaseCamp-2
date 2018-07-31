from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys





import time



def main():

    #driver = webdriver.Safari()

    driver = webdriver.Safari()

    driver.maximize_window()

    driver.implicitly_wait(2)

    baseurl = "https://www.google.com"

    driver.get(baseurl)

    element = driver.find_element_by_id("lst-ib")

    element.send_keys("hello world")

    searchBar = driver.find_element_by_name("btnK")

    searchBar.submit()

    time.sleep(3)

    snippets = driver.find_elements(By.XPATH, '//span[@class="st"]')

    all_has = True

    for s in snippets:

        if not ('hello' in s.text.lower()

                and 'world' in s.text.lower()):

            all_has = False

            break

    if all_has:

        print('all snippets say "hello world"')

    else:

        print('Some snippets do not say "hello world"')

        print(s.text)



main()