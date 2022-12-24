# Подключите библиотеку random и дайте ей краткое имя
import random as r

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    # Напишите ваш код здесь
    return r.choice(answers)


print(how_are_you())