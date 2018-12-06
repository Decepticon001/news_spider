import time
from selenium import webdriver
class get_huangye:
    def get_type1(self):
        try:
            driver = webdriver.Chrome()
            driver.get('http://b2b.huangye88.com/')
            a = driver.find_elements_by_xpath("//ul[@class='qiyecont']/li/a")
            # print(a)
            # return a
            for i in a:
                url = i.get_attribute('href')
                self.get_type2(url)
                print(i.text)
                print(i.get_attribute('href'))
            # for i in range(0, 10):
            #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            #     time.sleep(2)
            # for link in driver.find_elements_by_xpath("//div[@class='channel-news channel-news-0']/a"):
            #     # print(link.get_attribute('href'))
            #     uril_list.append(link.get_attribute('href'))
            #     # print(link.find_element_by_class_name("doc-title").text)
        except Exception as e:
            print(e)
        finally:
            driver.close()

    def get_type2(self,url):
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            a = driver.find_elements_by_xpath("//div[@class='box']/ul/li/a")
            for i in a:
                url = i.get_attribute('href')
                self.get_type3(url)
        except Exception as e:
            print(e)
        finally:
            driver.close()

    def get_type3(self,url):
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            a = driver.find_elements_by_xpath("//div[@class='box']/ul/li/a")
            for i in a:
                url = i.get_attribute('href')
                self.get_type4(url)
        except Exception as e:
            print(e)
        finally:
            driver.close()

    def get_type4(self,url):
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            a = driver.find_elements_by_xpath("//div[@class='ad_list']/a")
            for i in a:
                url = i.get_attribute('href')
                self.get_name(url)
        except Exception as e:
            print(e)
        finally:
            driver.close()

    def get_name(self,url):
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            next_page = driver.find_elements_by_xpath("")
            a = driver.find_elements_by_xpath("//div[@class='mach_list2']/form/dl//dt/h4/a")
            for name in a:
                print(name.text)
        except Exception as e:
            print(e)
        finally:
            driver.close()

if __name__ == '__main__':
    d = get_huangye()
    d.get_type1()