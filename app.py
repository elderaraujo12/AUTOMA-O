import pyautogui
from time import sleep

#bibliotecas
#pip install pyautogui pillow mouseinfo

#- passo manuais para realizar este processo 
#comando para abrir o calculador de mouse 
#python
#from mouseinfo import mouseInfo
#mouseInfo

#1- clicar e digitar meu usuario 
pyautogui.click(801,447,duration=0.5)
pyautogui.write('maycon') 
#2- clicar e digitar minha senha
pyautogui.click(801,478,duration=0.5)
pyautogui.write('123456')
#3- clicar em entrar
pyautogui.click(630,507,duration=0.5)
#4- extrair cada produtooProduto 134100838.61


with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto=linha.split(',')[0]
        quantidade=linha.split(',')[1]
        preco=linha.split(',')[2]

	#1- clicar e ditar produto
        pyautogui.click(448,436,duration=0.5)
        pyautogui.write(produto)
	#2- clicar e digitar quantidade
        pyautogui.click(454,467,duration=0.5)
        pyautogui.write(quantidade)
	#3- clicar e digitar o preço
        pyautogui.click(456,491,duration=0.5)
        pyautogui.write(preco)

        pyautogui.click(355,644,duration=1)

