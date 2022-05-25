from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
driver.implicitly_wait(3)
driver.get('https://lib.gnu.ac.kr/#/search/detail/4839550')

elements = driver.find_elements(by = By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[5]/div[2]/ng-include/div[1]/table/tbody[1]/tr[1]/td[5]/span[2]/span[1]')
for element in elements:
    print(element.text)
    print(element.text, file=open('gorio.txt', 'w', encoding='utf-8'))

elements = driver.find_elements(by = By.XPATH, value='/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[5]/div[2]/ng-include/div[1]/table/tbody[2]/tr[1]/td[5]/span[2]/span[1]')
for element in elements:
    print(element.text)
    print(element.text, file=open('gorio.txt', 'w', encoding='utf-8'))

driver.close()