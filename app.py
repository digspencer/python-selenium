from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


navegador = webdriver.Chrome()

#Entrando no navegador
navegador.get(f'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in')
time.sleep(2)

# Digitando o email
navegador.find_element('xpath', '//*[@id="username"]').send_keys("MARIA@hotmail.com")
# Maximizando a Janela
navegador.maximize_window()
# Digitando a senha
navegador.find_element('xpath', '//*[@id="password"]').send_keys("MARIA123")
# Clicando no botão de Login
navegador.find_element('xpath', '//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(2)
# Colocando 'Tech Recruiters Python' na barra de pesquisa 
navegador.find_element('xpath', '//*[@id="global-nav-typeahead"]/input').send_keys("Tech Recuiters Python")
#Aguarde 2 Secs
time.sleep(2)
navegador.find_element('xpath', '//*[@id="global-nav-typeahead"]/input').send_keys(Keys.RETURN)
time.sleep(101)

