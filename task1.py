from random import randint

number_to_guess = randint(1, 100)
number_of_attempts = 1
answer = 0

print(63 * "*")
print("*", "*", sep = 110 * " ")
print("*", "Игра: Угадай число!", "*", sep = 40 * " ")
print("*", "*", sep = 110 * " ")
print("*", "Суть игры - угадать число от 1 до 100 за наименьшее число попыток", "*", sep=4 * " ")
print("*", "*", sep = 110 * " ")
print(63 * "*")


def getting_an_answer():
    global number_of_attempts
    global answer
    while True:
        try:
            answer = int(input("Введите число: "))
        except Exception:
            print("Введеные данные некорректны. Введите число от 1 до 100")
        if answer:
            return answer
            break


while answer != number_to_guess:
    getting_an_answer()
    if number_to_guess > answer:
        print("Загаданное число больше!")
        number_of_attempts += 1
    if number_to_guess < answer:
        print("Загаданное число меньше!")
        number_of_attempts += 1

print(f"Точно! Вы угадали число с {number_of_attempts} попытки!")
