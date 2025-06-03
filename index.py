import pyautogui
import time

pyautogui.PAUSE = 1
#clica na tecla windows

#abre o sistema
import webbrowser
webbrowser.open("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#delay entre os comandos de enter

#digitar email
pyautogui.press("tab")
pyautogui.click(x=569, y=408)
pyautogui.write("andrielealves2005oliveira@gmail.com")
pyautogui.press("tab")
#delay entre comandos

#digitar senha
pyautogui.click(x=655, y=514)
pyautogui.write("andri123")

#Botao logar
pyautogui.press("tab")    
pyautogui.press("enter")

#delay entre comandos
time.sleep(2)

#importar base de dados
import pandas
#variavel "tabela" para remeter a base de dados
pyautogui.click(x=434, y=294)

tabela = pandas.read_csv(r"C:\Users\andri\Downloads\Python Projects\Automação de cadastros em estoque\bolsas_de_luxo.csv", 
                         encoding="windows-1252", sep=";")    
tabela.columns = tabela.columns.str.strip()
    

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=434, y=294)
    
    Codigo = tabela.loc[linha, "Codigo"]
    pyautogui.write(Codigo)
    
    pyautogui.press("tab")
    Marca = tabela.loc[linha, "Marca"]
    pyautogui.write(Marca)
    
    pyautogui.press("tab")
    Tipo  = tabela.loc[linha, "Tipo"]
    pyautogui.write(Tipo)
    
    pyautogui.press("tab")
    Categoria = str(tabela.loc[linha, "Categoria"])
    pyautogui.write(Categoria)
    
    pyautogui.press("tab")
    Preco_unitario = str(tabela.loc[linha, "Preco_unitario"])
    pyautogui.write(Preco_unitario)
    
    pyautogui.press("tab")
    Custo = str(tabela.loc[linha, "Custo"])
    pyautogui.write(Custo)
    
    pyautogui.press("tab")
    Obs = str(tabela.loc[linha, "Obs"])
    
    if Obs != "nan":
        pyautogui.write(Obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)
            