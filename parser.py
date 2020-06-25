import pandas as pd
import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': '*/*'}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination').find_all('a')[-2].text
    return int(pages)


def write_csv(data):
    df = pd.DataFrame([data])
    df.to_csv('freelancehunt.csv', index=False, header=False, mode='a')


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('table', class_='table table-normal project-list').find_all('td', class_='left')

    for ad in ads:
        title = ad.find('a', class_='bigger visitable').text
        url = ad.find('a', class_='bigger visitable').get('href')

        data = {'title': title,
                'url': url}
        write_csv(data)


def main():
    url = 'https://freelancehunt.com/projects/skill/python/22.html'
    base_url = 'https://freelancehunt.com/projects/skill/python/22.html?page='

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages+1):
        completed_url = base_url + str(i)
        html = get_html(completed_url)
        get_page_data(html)


if __name__ == '__main__':
    main()
