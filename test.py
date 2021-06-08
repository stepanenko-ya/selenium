from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
from random import choice
from fake_useragent import UserAgent
from proxy import proxy_list

ua = UserAgent()


def content():
    with open("page_source.html") as file:
        f = file.read()
        soup = BeautifulSoup(f, "html.parser")
        name = soup.find(class_='nazwa naglowek').find("a").get("href")
        cena = soup.find(class_='cena').find("b")
        if cena:
           coast = cena.get_text().strip()
        else:
            coast = ' '
        result = open("iparts.csv", "a+")
        result.write(f"https://www.iparts.pl/{name}|{coast}\n")
        result.close()


def selenium_pars(url):
    x = True
    while x:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-agent={ua.random}")
            options.add_argument(f"--proxy-server={random.choice(proxy_list)}")
            print(random.choice(proxy_list))
            driver = webdriver.Chrome(options=options)
            print(url)
            driver.get(url)
            time.sleep(5)
            # try:
            #     link = driver.find_element_by_class_name("nazwa naglowek").get_attribute('href')
            #     print(link)

            # pageSource = driver.page_source
            # fileToWrite = open("page_source.html", "w")
            # fileToWrite.write(pageSource)
            # fileToWrite.close()
            # content()

                # name = driver.find_element_by_class_name("productname")
                # print(name)
                # button = driver.find_element_by_xpath("//*[@id='buttonszukaj']")
                # button.click()
                # x = False
                # items = driver.find_elements_by_class_name("nazwa naglowek")
                # print(items)
                # time.sleep(6)
                # print(driver.current_url)
            #     items[0].click()
            #
            #     driver.implicitly_wait(5)
            #     # driver.switch_to.window(driver.window_handles[1])
            #     # print(driver.current_url)
            #     # name = driver.find_element_by_class_name('seller-info-name').text
            #     # print(name)
            #     # driver.close()
            #     # driver.switch_to.window(driver.window_handles[0])
            #     # print(driver.current_url)
        except Exception as ex:
            print(ex)
            x = True
            driver.close()
            driver.quit()
        finally:
            x = False
            driver.close()
            driver.quit()



if __name__ =="__main__":
    with open("result.csv")as finders_url:
        urls = finders_url.readlines()
        for url in urls[3:8]:
            selenium_pars(url.strip())
