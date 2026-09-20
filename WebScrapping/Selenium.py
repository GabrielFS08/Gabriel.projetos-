from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.kabum.com.br/?gclsrc=aw.ds&&utm_id=72385815&gad_source=1&gad_campaignid=72385815&gbraid=0AAAAADx-HyH8wgX9wUOPynjxEjm4t-6Yk&gclid=EAIaIQobChMI4tqRhay_lgMVp1dIAB2rHwF3EAAYASAAEgLrwPD_BwE")
sleep(5)

produtos = driver.find_elements(By.XPATH, "//span[@class='text-sm text-left text-gray-800 text-ellipsis line-clamp-2 break-normal h-40']")

preço = driver.find_elements(By.XPATH, "//span[@class='text-base font-semibold text-gray-800']")

for produto, preço in zip(produtos, preço):
    with open('preços.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{produto.text}, {preço.text}{os.linesep}")

input('')