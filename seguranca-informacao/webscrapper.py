from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    site = requests.get("https://www.climatempo.com.br/").content
    
    soup = BeautifulSoup(site, 'html.parser') #Baixar o html
    #print(soup.prettify()) #Exibir o html identado
    
    temperatura = soup.find('span', class_='_block _margin-b-5 -gray')
    print(soup.a)
    print(soup.p)
    print(soup.find('admin'))