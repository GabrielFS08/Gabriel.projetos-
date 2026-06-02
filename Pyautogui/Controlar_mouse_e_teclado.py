import pyautogui
import time
import pandas as pd

#importar a base de dados
tabela = pd.read_csv("produtos.csv")
#tempo de espera entre os comandos
pyautogui.PAUSE = 0.5

#abrir o sistema opera ou um outro navegador escolhido
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")#abrir uma nova aba
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#esperar carregar o site6.5 
time.sleep(2)

#fazendo login
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=996, y=550)

#para registrar os produtos primeiro vamos percorrer cada linha da tabela
for linha in tabela.index: #tabela.index vai percorrer somentes as linhas
    pyautogui.click(x=836, y=283)#clica na primeira linha do formulário
    pyautogui.write(str(tabela.loc[linha, "codigo"]))#loc é usado pra buscar informação da coluna código, e na sua linha correspondente
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha, "obs"]):#se a linha da coluna obs for nan, ele nao digitara no campo de obs
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    
    pyautogui.click(x=908, y=932)
    pyautogui.scroll(200)#volta pro início da tela com o scroll pra cima
    



