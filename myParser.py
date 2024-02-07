import requests 
from bs4 import BeautifulSoup 


URL = 'https://www.cybersport.ru/tags/anime/tetrad-smerti-stala-luchshim-anime-serialom-chelovek-benzopila-tolko-piatyi-itogi-golosovaniia-na-cybersport-ru'
page = requests.get(URL)


series = []
allData = []

soup = BeautifulSoup(page.content, 'html.parser')
allData = soup.find_all('ol')



for item in allData:

    series.append(item.get_text())
    print(item.get_text())  
 
    


    


 
 