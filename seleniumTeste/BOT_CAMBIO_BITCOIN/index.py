from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
# Validar a presença de qualquer elemento
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mysql.connector
from  mysql.connector import Error

def webScraping():

        
        option = webdriver.ChromeOptions() #Cria o obejeto com a diretrizes para o browser que sera aberto
        option.add_argument("--start-maximized") # chrome maximizado DIRETRIZ 1
        option.add_argument("--lang=pt")  # Define o idioma para português DIRETRIZ 2
        # option.add_argument("--headless")   # Chrome em modo headless invisível DIRETRIZ 3
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)# Baixa o browser executável que sera manipulado
        #Cria o obejeto que ira permitir simular sequencias de ações de mouse e teclas do servidor
        action = ActionChains(driver)
        # Acessa site específico
        driver.get('https://www.google.com.br/')   

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'APjFqb'))).click()
        time.sleep(3) 
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'APjFqb'))).send_keys('bitcoin')
        time.sleep(3)
        action.key_down(Keys.ENTER).perform()
        time.sleep(3)
        
        bitcoin = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pclqee'))).text
        print(bitcoin)
        return bitcoin
        
def atualizarBanco():
    bitcoin = webScraping()
    print("\n  Atualizando banco!")
    try:
        con = mysql.connector.connect (host='localhost', database='senai', user='root', password= '')
        consulta_sql = rf"UPDATE `bitcoin` SET `valor_bitcoin`='{str(bitcoin)}' where id = 1;"
        cursor = con.cursor()
        cursor.execute(consulta_sql) 
        con.commit()
    except Error as erro:
        print("Erro ao acessar tabela MysQL", erro)
    finally:
        if(con.is_connected()):
            con.close()
            cursor.close()
            print("  Conexäo ao MysQL encerrada\n\n")

atualizarBanco()
