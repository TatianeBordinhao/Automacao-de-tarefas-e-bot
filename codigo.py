# Projeto usando automação de tarefas e bot para cadastro de clientes

# Passo 1: Entrar no site da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

#pip install pyautogui
#pyautogui é uma biblioteca = pacotes de código
#pyautogui.click (para clicar)
#pyautogui.write (para escrever texto)
#pyautogui.press (aperta uma única tecla)
#pyautogui.hotkey (aperta um atalho)

import pyautogui # biblioteca do python
import time # permite fazer o controle de tempo
pyautogui.PAUSE = 0.5 # pausa entre a execução dos comandos
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #variável

# Passo 1: Entrar no site da empresa
# abrir o navegador
pyautogui.press ("Win") 
pyautogui.write ("chrome")
pyautogui.press ("enter")
pyautogui.write (link)
pyautogui.press ("enter")
# fazer uma pausa maior para o site carregar
time.sleep(4) # computador espera

# Passo 2: Fazer login
# clicar no campo de email
pyautogui.click(x=1373, y=461)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passa para o próximo campo
pyautogui.write("1234") # senha
pyautogui.press("tab") # passa para o botão
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(4) # computador espera

# Passo 3: Abrir a base de dados (importar o arquivo para dentro do python)
# pandas #ferramenta em python que trabalha com base de dados
# openpyxl #trabalha com base de dados excel
#pip install pandas openpyxl
import pandas

#csv - formato do arquivo
tabela = pandas.read_csv("produtos.csv")
print (tabela)

#index - índice (n. linhas da tabela)
for linha in tabela.index:
    # Passo 4: Cadastrar um produto
    pyautogui.click(x=1316, y=375) #clicar no campo do código
    
    #código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "Nan":
        pyautogui.write(obs)
    pyautogui.press("tab")    
        
    pyautogui.press("enter") # clicou no botão enviar
    
    # voltar para o início da tela - dar Scroll (rolar) na tela
    # scroll positivo sobre a tela e scroll negativo desce a tela
    pyautogui.scroll(5000)
    
    #para localizar uma linha na tabela no python uso [] - ex: codigo = tabela.loc[linha, "coluna codigo"], o str torna todos os dados formatos como texto, para evitar erros!
    #Nan = valor vazio
    #!= diferente
    

# Passo 5: Repetir o passo 4 até acabar a lista de produtos



