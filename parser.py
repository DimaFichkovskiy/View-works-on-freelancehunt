import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
HEADERS = {'accept': '*/*', 'user-agent': ua.random}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination').find_all('a')[-2].text
    return int(pages)


def write_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('freelancehunt.csv', index=False, header=False, mode='a')


def get_page_data(html_base, base_url):
    now = datetime.datetime.now()

    data = {'date': list(),
            'title': list(),
            'url': list()}

    total_pages = get_total_pages(html_base)

    for i in range(1, total_pages + 1):
        completed_url = base_url + str(i)
        html = get_html(completed_url)

        soup = BeautifulSoup(html, 'lxml')
        ads = soup.find('table', class_='table table-normal project-list').find_all('td', class_='left')

        for ad in ads:
            try:
                title = ad.find('a', class_='bigger visitable').text
            except AttributeError:
                continue
            url = ad.find('a', class_='bigger visitable').get('href')

            #get day
            day = ''
            if now.day in range(1, 10):
                day = '0' + str(now.day)
            else:
                day = str(now.day)

            #get month
            month = ''
            if now.month in range(1, 10):
                month = '0' + str(now.month)
            else:
                month = str(now.month)

            # get year
            year = str(now.year)

            date = f'{day}-{month}-{year}'

            data['date'].append(date)
            data['title'].append(title)
            data['url'].append(url)

    write_csv(data)


def main():
    url = 'https://freelancehunt.com/projects/skill/python/22.html'
    base_url = 'https://freelancehunt.com/projects/skill/python/22.html?page='

    html_base = get_html(url)
    get_page_data(html_base, base_url)


if __name__ == '__main__':
    main()
