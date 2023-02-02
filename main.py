from bs4 import BeautifulSoup
import requests
import time

def hitta_nyheter():
    html_text = requests.get('https://www.elbruk.se/').text
    soup = BeautifulSoup(html_text, 'lxml')
    nyhet = soup.find_all('div', class_='info-box-content')
    for index, nyhet in enumerate(nyhet):

        nyhet_name = nyhet.find('span', class_='info-box-number').text
        with open(f'nyheter/{index}.txt', 'w') as f:
            f.write(f'''
            Pris: {nyhet_name}
            ''')
        print(f'Fil sparad: {index}')

        print('')

if __name__ == '__main__':
    while True:
        hitta_nyheter()
        time_wait = 60
        print(f'Väntar {time_wait} minuter...')
        time.sleep(time_wait * 60)
