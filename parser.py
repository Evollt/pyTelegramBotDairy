# импорт библиотеки для парсинга и библиотеки для отправки запроса сайту
from bs4 import BeautifulSoup
import requests

# получаем сайт
url = requests.get('https://www.mgkit.ru/studentu/raspisanie-zanatij')
# получаем исходный код сайта
soup = BeautifulSoup(url.text, 'lxml')

# находим все теги a на сайте
page_all_a = soup.find_all('a')