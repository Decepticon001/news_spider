import time
from selenium import webdriver

def get_yidian_url():
    browser = webdriver.PhantomJS()
    browser.get('http://www.yidianzixun.com/channel/u8453')
    # browser = webdriver.Chrome()
    # browser.get("http://www.yidianzixun.com/channel/u8453")
    uril_list=[]
    for i in range(0, 10):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
    for link in browser.find_elements_by_xpath("//div[@class='channel-news channel-news-0']/a"):
        # print(link.get_attribute('href'))
        uril_list.append(link.get_attribute('href'))
        # print(link.find_element_by_class_name("doc-title").text)
    browser.close()
    return uril_list

list = get_yidian_url()
print(list)