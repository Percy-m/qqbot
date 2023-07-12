# 

from bs4 import BeautifulSoup as BS
import requests

import psycopg2 as pg

from modules.constant.database import DATABASE,USER,PASSWORD,HOST


def get_house_price(url: str):
    response = requests.get(url)
    html = response.text
    print(html)
    bs = BS(html, "html.parser")
    items = bs.find('div', class_='fjlist-box boxstyle2')
    print(items)

if __name__ == '__main__':

    result = []
    a = []
    with pg.connect(database=DATABASE,
                user=USER,
                password=PASSWORD,
                host=HOST) as conn:
        cursor = conn.cursor()
        cursor.execute("select name from city")
        result = cursor.fetchall()
        for item in result:
            a.append(item[0])
    print(a)