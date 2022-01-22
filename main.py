from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.dn.se/sok/?q=Sverigedemokraterna&page=1&sort=newest&date=').text
soup = BeautifulSoup(html_text, 'lxml')
nyhet = soup.find_all('a', class_='article-results__item th-nyheter')
for nyhet in nyhet:

    nyhet_name = nyhet.find('div', class_='article-results__content').text
    linker = soup.find("a", {"article-results__item th-nyheter"}).attrs['href']

    print(f'''
    Artikel namn: {nyhet_name}
    Länk till artikel: https://www.dn.se{linker}
    ''')

    print('')