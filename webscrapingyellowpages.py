
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#função que realisa a busca dos resultados
def busca(name, city, address, number):
    lista = []
    name = navegador.find_element(By.XPATH, name).text
    city = navegador.find_element(By.XPATH, city).text
    address = navegador.find_element(By.XPATH, address).text
    number = navegador.find_element(By.XPATH, number).text
    lista.extend((name, city, address, number))
    return (lista)

#iniciando o navegador
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
navegador = webdriver.Chrome()

navegador.get("https://www.yellowpages.com/")

#realizando a pesquisa
navegador.find_element(By.XPATH, '//*[@id="query"]').send_keys('Barbecue Restaurants')

#chamando a função
navegador.find_element(By.XPATH, '//*[@id="query"]').send_keys(Keys.ENTER)

busca1 = busca('//*[@id="lid-10310643"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-10310643"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-10310643"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-10310643"]/div/div/div[2]/div[2]/div[1]')
busca2 = busca('//*[@id="lid-10277926"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-10277926"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-10277926"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-10277926"]/div/div/div[2]/div[2]/div[1]')
busca3 = busca('//*[@id="lid-475024885"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-475024885"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-475024885"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-475024885"]/div/div/div[2]/div[2]/div[1]')
busca4 = busca('//*[@id="lid-11662159"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-11662159"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-11662159"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-11662159"]/div/div/div[2]/div[2]/div[1]')
busca5 = busca('//*[@id="lid-22249563"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-22249563"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-22249563"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-22249563"]/div/div/div[2]/div[2]/div[1]')
busca6 = busca('//*[@id="lid-1499153"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-1499153"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-1499153"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-1499153"]/div/div/div[2]/div[2]/div[1]')
busca7 = busca('//*[@id="lid-2876051"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-2876051"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-2876051"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-2876051"]/div/div/div[2]/div[2]/div[1]')
busca8 = busca('//*[@id="lid-468310626"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-468310626"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-468310626"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-468310626"]/div/div/div[2]/div[2]/div[1]')
busca9 = busca('//*[@id="lid-22286026"]/div/div/div[2]/div[1]/h2/a/span',
               '//*[@id="lid-22286026"]/div/div/div[2]/div[2]/div[2]/div[2]',
               '//*[@id="lid-22286026"]/div/div/div[2]/div[2]/div[2]/div[1]',
               '//*[@id="lid-22286026"]/div/div/div[2]/div[2]/div[1]')
busca10 = busca('//*[@id="lid-469380780"]/div/div/div[2]/div[1]/h2/a/span',
                '//*[@id="lid-469380780"]/div/div/div[2]/div[2]/div[2]/div[2]',
                '//*[@id="lid-469380780"]/div/div/div[2]/div[2]/div[2]/div[1]',
                '//*[@id="lid-469380780"]/div/div/div[2]/div[2]/div[1]')

#atribuindo os resultados à uma lista
lista = [busca1, busca2, busca3, busca4, busca5, busca6, busca7, busca8, busca9, busca10]

#gerando o .txt
with open('resultado.txt', 'w', encoding='utf-8') as arquivo:
    for valor in lista:
        arquivo.write(str(valor) + '\n')

#fechando o navegador
navegador.quit()