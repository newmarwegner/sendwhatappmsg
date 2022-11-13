import time
import urllib.parse
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config

## Dados base
data_curso = '19/11'
file_path = os.path.abspath('./preliminar_presencial.pdf')
msg = config('msg_preliminar')
mensagem = msg.replace('dd/mm', data_curso).replace('%', ' ')
texto = urllib.parse.quote(mensagem)
contatos = config('contatos').split(',')

## Execução webdriver
wapp = webdriver.Chrome('./chromedriver')
wapp.get(config('whatsapp'))

while not wapp.find_elements(By.ID, "side"):
    time.sleep(1)

for numero in contatos:
    wapp.get(f"https://web.whatsapp.com/send?phone={numero}&text={texto}")

    while not wapp.find_elements(By.ID, "side"):
        time.sleep(1)
    time.sleep(4)

    wapp.find_element(By.XPATH, config('send_msg')).click()
    wapp.find_element(By.XPATH, config('anexo')).click()
    wapp.find_element(By.XPATH, config('input')).send_keys(file_path)
    time.sleep(4)
    wapp.find_element(By.XPATH, config('final_send')).click()
    time.sleep(5)
