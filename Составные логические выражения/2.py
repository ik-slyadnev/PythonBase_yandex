# Продуктов маловато:
milk = not True       # Молоко "НЕ есть".
cereals = True        # Хлопья есть.
eggs = False          # Яиц нет.

# Вставьте логический оператор вместо многоточия.
# Решите, нужно ли расставить скобки.

if milk and cereals or eggs:
    if eggs:
        if milk:
            breakfast = "- омлет"
        else:
            breakfast = "- яичница"
    else:
        breakfast = "- хлопья с молоком"
else:
    if milk:
        breakfast = "- стакан молока"
    elif cereals:
        breakfast = "можно погрызть сухих хлопьев"
    else:
        breakfast = "ничего не будет: разгрузочный день"

print("Сегодня на завтрак", breakfast)