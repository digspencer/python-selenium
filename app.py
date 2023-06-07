from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui


options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=options)

#Entrando no navegador
navegador.get(f'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in')
time.sleep(2)

# Digitando o email
navegador.find_element('xpath', '//*[@id="username"]').send_keys("maria@gmail.com")
# Maximizando a Janela
navegador.maximize_window()
# Digitando a senha
navegador.find_element('xpath', '//*[@id="password"]').send_keys("maria!")
# Clicando no botão de Login
navegador.find_element('xpath', '//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(5)
# Colocando 'Tech Recruiters Python' na barra de pesquisa 
navegador.find_element('xpath', '//*[@id="global-nav-typeahead"]/input').send_keys("Tech Recruiter")
#Aguarde 2 Secs
time.sleep(4)
navegador.find_element('xpath', '//*[@id="global-nav-typeahead"]/input').send_keys(Keys.RETURN)
time.sleep(4)
navegador.find_element('xpath', '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button').click()

time.sleep(5)
while True:
    try:
        time.sleep(2)
        navegador.find_element_by_id('xpath', '//*[@id="ember438"]').click()
        time.sleep(1)
        navegador.find_element('xpath', '/html/body/div[3]/div/div/div[3]/button[2]/span').click()
        time.sleep(1)
        navegador.find_element('xpath', '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[5]/div/div/button[2]/span').click()
    except Exception:
        pyautogui.scroll(-20)