from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver.get('https:www.google.com.br')
time.sleep(60)