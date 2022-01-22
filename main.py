from bs4 import BeautifulSoup
import requests
import time

def hitta_nyheter():
    html_text = requests.get('https://www.dn.se/sok/?q=Sverigedemokraterna&page=1&sort=newest&date=').text
    soup = BeautifulSoup(html_text, 'lxml')
    nyhet = soup.find_all('a', class_='article-results__item th-nyheter')
    for index, nyhet in enumerate(nyhet):

        nyhet_name = nyhet.find('div', class_='article-results__content').text
        linker = soup.find("a", {"article-results__item th-nyheter"}).attrs['href']
        with open(f'nyheter/{index}.txt', 'w') as f:
            f.write(f'''
            Artikel namn: {nyhet_name}
            Länk till artikel: https://www.dn.se{linker}
            ''')
        print(f'Fil sparad: {index}')

        print('')

if __name__ == '__main__':
    while True:
        hitta_nyheter()
        time_wait = 10
        print(f'Väntar {time_wait} minuter...')
        time.sleep(time_wait * 60)