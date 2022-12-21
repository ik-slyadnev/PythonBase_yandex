favorite_songs = {
    'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'],
    'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'],
    'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
}
# Ниже напишите код, который напечатает на экран, сколько у Димы любимых песен
dima = favorite_songs['Дима']
print(len(dima))

# Ниже напишите код, который построчно напечатает

songs = favorite_songs['Соня']
for song in songs:
    print(song)