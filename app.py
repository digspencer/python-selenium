from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


navegador = webdriver.Chrome()

navegador.get(f'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in')
time.sleep(2)

navegador.find_element('xpath', '//*[@id="username"]').send_keys("exemplo@hotmail.com")
navegador.find_element('xpath', '//*[@id="password"]').send_keys("maria123")
navegador.find_element('xpath', '//*[@id="organic-div"]/form/div[3]/button').click()
navegador.find_element('xpath', '//*[@id="global-nav-typeahead"]/input').send_keys("Tech Recuiters Python").send_keys(keys.RETURN)
time.sleep(101)
#navegador.send_keys(keys.RETURN)

