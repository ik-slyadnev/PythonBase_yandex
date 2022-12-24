# подключите библиотеку datetime под именем dt
import datetime as dt

start_moment = dt.datetime(2022, 12, 20, 12, 0)  # Напишите код здесь
current_moment = dt.datetime(2022, 12, 24, 18, 25)  # и здесь

total_time = (current_moment - start_moment)  # и здесь

print(total_time)