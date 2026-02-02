# def can_cast(mana, cost):
#     if mana > cost:
#         return True
#     else:
#         return False
#
# print(can_cast(100, 30))
# print(can_cast(10, 20))

# ____________________________________________

# def celsius_to_fahrenheit(celsius):
#     return round(celsius * 9 / 5 + 32, 1)
#
# print(celsius_to_fahrenheit(451))

# ____________________________________________

# def is_work_time(time):
#     if time > 23 or time < 0:
#         print("Указано не корректное время")
#         return None
#     elif 9 <= time < 18:
#         return True
#     else:
#         return False
#
# print(is_work_time(38))
# print(is_work_time(8))
# print(is_work_time(14))

# ____________________________________________

# def has_enough_money(balance, price):
#     if balance >= price:
#         return True
#     else:
#         return False
#
#
# def can_buy(balance, price, is_shop_open):
#     if has_enough_money(balance, price) and is_shop_open:
#         return True
#     else:
#         return False
#
#
# print(can_buy(100, 10, True))
# print(can_buy(50, 10, False))
# print(can_buy(8, 10, True))

# ____________________________________________

# def find_user(users, name):
#     for user in users:
#         if user == name:
#             return "Found"
#         else:
#             continue
#     return "Not found"
#
# print(find_user(["as","vas","das"], "kas"))

# ____________________________________________

