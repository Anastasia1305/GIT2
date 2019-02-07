from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открываем www.google.ru
driver.get("https://www.google.ru")

try:
    # ждем загрузки поисковой строки 5 сек max
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.gLFyf')))

    # Вводим Selenide
    element.send_keys("Selenide", Keys.ENTER)

    # первая ссылка и сохранение
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.r>a')))
    checklink = element.get_attribute('href')
    assert "https://ru.selenide.org/" in checklink
    print(checklink + " first result is correct")

    # переход в раздел еще
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.Cq34nf')))
    element.click()

    # переход в раздел картинки
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[id=lb]>div>a')))
    element.click()

    # ссылка  соотношение картинки сохранение
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.nJGrxf')))
    checkpicture = element.text.strip()
    assert checkpicture in "selenide.org"
    print("First picture is corresponded to Selenide website")

    # возврат на вкладку все
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.q')))
    element.click()

    # Сравнение ссылок
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.r>a')))
    checkfirstlinkagain = element.get_attribute('href')
    assert checkfirstlinkagain in checklink
    print(checkfirstlinkagain + "Result is correct")

finally:
    driver.quit()