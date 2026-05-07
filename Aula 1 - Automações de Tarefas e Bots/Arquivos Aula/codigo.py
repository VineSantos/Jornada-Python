import pyautogui
import time
import pandas
##import display

pyautogui.PAUSE = 3
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.click(x=807, y=410)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=2129, y=339)
pyautogui.write("vine@g.com")
pyautogui.click(x=2122, y=426)
pyautogui.write("abcde")
pyautogui.press("enter")

time.sleep(5)

tabela = pandas.read_csv("produtos.csv")
print(tabela)
##display(tabela)

for linha in tabela.index:

    pyautogui.click(x=2216, y=216)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("enter")

    pyautogui.scroll(500)



    ## for linha in tabela.index:
        