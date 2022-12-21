def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    t = 0
    for i in listened:
        t += int (i)
    m = t//60
    return f'Вы прослушали {len(listened)} песен общей продолжительностью {m} минут.'
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))