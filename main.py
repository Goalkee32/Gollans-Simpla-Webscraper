from bs4 import BeautifulSoup
import requests
import time
import json

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

    with open('nyheter/1.txt') as file, open('pris.json', 'w') as json_file:
        items = {}
        for line in file:
            if not line.strip():
                continue
            data = line.split('|')
            for val in data:
                key, sep, value = val.partition(':')
                items[key.strip()] = value.strip()
        json.dump(items, json_file, indent=4)

if __name__ == '__main__':
    while True:
        hitta_nyheter()
        time_wait = 60
        print(f'Väntar {time_wait} minuter...')
        time.sleep(time_wait * 60)
