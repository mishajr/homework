import requests 
from bs4 import BeautifulSoup 
import csv 
 
CSV = 'cars.csv' 
 
HOST = 'https://www.olx.ua/' 
 
URL = 'https://www.olx.ua/uk/transport/' 
 
HEADERS = { 
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' 
     
} 
 
def get_html(url, params = ''): 
    request = requests.get(url, headers = HEADERS, params = params) 
    return request 
 
def get_content(html): 
    soup = BeautifulSoup(html, 'html.parser') 
    items = soup.find_all('div', class_ = 'css-1sw7q4x') 
    cars = [] 
 
 
 
    for item in items: 
        title_item = item.find_next('h6', class_ = 'css-16v5mdi er34gjf0') 
        title = title_item.get_text() if title_item else None 
 
        price_item = item.find_next('p', class_ = 'css-10b0gli er34gjf0') 
        price = price_item.get_text() if price_item else None 
 
        gearbox_item = item.find_next('span', class_ = 'css-efx9z5') 
        gearbox = gearbox_item.get_text() if gearbox_item else None 
 
        link_elem = item.find_next('a', class_ = 'css-rc5s2u') 
        link = link_elem.get('href') if link_elem else None 
        link = HOST + str(link) 
 
        cars.append({ 
            'title': title, 
            'price': price, 
            'gearbox': gearbox, 
            'link': link 
        }) 
    return cars 
#     print(cars) 
 
# get_content(get_html(URL).text) 
 
 
def save_to_csv(cars, path): 
    with open(path, 'w', newline = '') as csvfile: 
        writer = csv.writer(csvfile, delimiter = ';') 
        writer.writerow(['Title', 'Price', 'Gearbox', 'Link']) 
        for car in cars: 
            writer.writerow([car['title'], car['price'], car['gearbox'], car['link']]) 
 
def parse(): 
    pagination= int(input('Введіть кількість сторінок для парсингу: ')) 
    html = get_html(URL) 
    if html.status_code == 200: 
        cars = [] 
        for page in range(1, pagination +1): 
            print(f'Парсинг сторінки {page} з {pagination}...') 
            html = get_html(URL, params = {'page=': page}) 
            cars.extend(get_content(html.text)) 
            save_to_csv(cars, CSV) 
            print(f'Отримано {len(cars)} автомобілів') 
        pass 
 
    else: 
        print('Error') 
 
parse()