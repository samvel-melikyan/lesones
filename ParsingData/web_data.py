import requests
from local_data import *
from bs4 import BeautifulSoup

# r = requests.get(url)
# with open('letterbox.html', 'w', encoding='utf-8') as output_file:
#    output_file.write(r.text)

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

# Находим все элементы <tr> с классом diary-entry-row viewing-poster-container
entries = soup.find_all('tr', class_='diary-entry-row viewing-poster-container')

data = []
for entry in entries:
   td_film_details = entry.find('td', class_='td-film-details')
   film_name = td_film_details.find('a').text

   release_date = entry.find('td', class_='td-released center').text

   td_rating_rating_green = entry.find('td', class_='td-rating rating-green')
   rating_span = td_rating_rating_green.find('span', class_='rating')
   classes = rating_span.get('class', [])

   rating = classes[1].split('-')[1]

   # Добавляем новую пару ключ-значение
   data.append({'film_name': film_name, 'release_date': release_date, 'rating': rating})

print(data[:5])

page_num = 16

url = f'https://letterboxd.com/{user_login}/films/diary/page/{page_num}/'

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

entries = soup.find_all('tr', class_='diary-entry-row viewing-poster-container')

print(len(entries))

