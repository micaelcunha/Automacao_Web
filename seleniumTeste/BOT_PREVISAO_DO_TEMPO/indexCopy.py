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
        driver.get('https://weather.com/weather/today/l/-12.25,-38.96?par=google')   

        # Escreve cidade específica
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'LocationSearch_input'))).click()
        time.sleep(3)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'LocationSearch_input'))).send_keys('Feira de Santana, Bahia, Brazil')
        time.sleep(3)
        action.key_down(Keys.ENTER).perform()
        time.sleep(3)
        
        # Aguardando a presença do elemento (aguardando a presença do elemento nos proximos 10 segundos)
        temperatura = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'CurrentConditions--tempValue--MHmYY'))).text

        print(f'\n\n--------------------------------------\n\nTemperatura atual na regional BA: {temperatura}F \n\n--------------------------------------')

        #Transforma F em C      
        temp = str(temperatura).replace('°','') 
        temperatura_c  = int((int(temp) -32)/ 1.8)

        print(f'\n\n--------------------------------------\n\nTemperatura atual na regional BA: {temperatura_c}°C \n\n--------------------------------------')

        return temperatura_c

def atualizarBanco():
    clima = webScraping()
    print("\n  Atualizando banco!")
    try:
        con = mysql.connector.connect (host='localhost', database='senai', user='root', password= '')  
        consulta_sql = rf"UPDATE `clima` SET `temperatura_atual`='{int(clima)}' where id = 1;"
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
