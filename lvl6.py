# Умова
# Користувач вводить один рядок з цінами покупок через пробіл.
# Приклад вводу:
# 120 45 300 89 10
# Потрібно:
# Перетворити введений рядок у список чисел
# Знайти:
# загальну суму покупок
#  середню ціну
#  кількість покупок дорожчих за середню
#   3. Вивести:
# суму
# середнє (округлити до 2 знаків)
# кількість покупок, що більші за середню

count = 0
price_list = []

my_list = input("Введите список цен покупок: ").split(" ")

for item in my_list:
    price_list.append(float(item))

total_amount = sum(price_list)
average_price = total_amount / len(price_list)

for item in price_list:
    if item > average_price:
        count += 1

print(f"Общая сумма покупок: {total_amount}")
print(f"Средняя цена покупок: {round(average_price, 2)}")
print(f"Количество покупок дороже средней цены: {count}")
