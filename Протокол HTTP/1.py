user_query = 'как стать бэкенд-разработчиком'
us = user_query.split(' ')
usj = '%20'.join(us)

url = 'https://yandex.ru/search/?text=' + usj

print(url)
