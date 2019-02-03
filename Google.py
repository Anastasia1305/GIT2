import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Search(unittest.TestCase):

    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.get("http://www.google.ru")

    def test_search(self):
        assert 'Google' in self.drv.title
        #ввод слова в поле поиска
        elm = self.drv.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
        elm.send_keys('Selenide',Keys.ENTER)
        #первая ссылка и сохранение
        elm = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a')
        checklink = elm.get_attribute('href')
        assert "https://ru.selenide.org/" in checklink
        #переход в раздел еще
        elm = self.drv.find_element_by_xpath('//*[@id="ow16"]/a')
        elm.click()
        #переход в раздел картинки
        elm = self.drv.find_element_by_xpath('//*[@id="lb"]/div/a[1]')
        elm.click()
        print(2)
        #ссылка  соотношение картинки сохранение
        elm = self.drv.find_element_by_xpath('//*[@id="rg_s"]/div[1]/a[2]')
        checkpicture = elm.text.strip()
        assert "selenide.org" in checkpicture
        #возврат на вкладку все
        elm = self.drv.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[1]/a')
        elm.click()
        elm = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a')
        checkfirstlinkagain = elm.get_attribute('href')
        assert checkfirstlinkagain in checklink

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()