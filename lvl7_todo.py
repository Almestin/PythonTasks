list_tasks = [{"title": "Buy bread", "done": "False"}, {"title": "Buy beer", "done": "True"},
              {"title": "Buy cat", "done": "False"}, {"title": "Buy car", "done": "True"}]


def show_menu(board):
    print(board * 30)
    print("1. Додати завдання")
    print("2. Показати завдання")
    print("3. Позначити виконаним")
    print("4. Видалити завдання")
    print("5. Вийти")
    print(board * 30)


def get_number(item):
    number_of_task = None
    while True:
        try:
            number_of_task = int(input(f"Вкажить номер {item}: "))
        except Exception:
            print("Некорретний ввод!")
            continue
        if number_of_task and item == "завдання" and 0 < number_of_task <= len(list_tasks) \
                or number_of_task and item == "меню" and 0 < number_of_task < 6:
            return number_of_task
        else:
            print("Некорретний ввод!")
            continue


def add_task(tasks):
    task_name = ""
    while True:
        task_name = input("Вкажить назву завдання: ")
        if task_name == "":
            print("Треба вказати назву завдання!")
            continue
        else:
            break
    tasks.append({"title": task_name, "done": "False"})
    print(f"Завданя - {task_name} додано!")


def show_task(tasks):
    print("Список завдань:")
    if len(tasks) == 0:
        print("Список завдань порожній")
    else:
        for index, task in enumerate(tasks):
            print(f"Завданя {index + 1} - {task["title"]} === Зроблено? - {task["done"]}")


def complete_task(tasks):
    choice_to_complete = get_number("завдання")
    if tasks[choice_to_complete - 1]["done"] == "False":
        tasks[choice_to_complete - 1]["done"] = "True"
        print(f"Завданя - {tasks[choice_to_complete - 1]["title"]} виконано!")
    else:
        print(f"Завданя - {tasks[choice_to_complete - 1]["title"]} вже виконано!")


def delete_task(tasks):
    removed_task = tasks.pop(get_number("завдання") - 1)
    print(f"Завданя - {removed_task["title"]} === Зроблено? - {removed_task["done"]} видалено")


while True:
    show_menu("*")
    choice = get_number("меню")
    if choice == 1:
        add_task(list_tasks)
        continue
    elif choice == 2:
        show_task(list_tasks)
        continue
    elif choice == 3:
        complete_task(list_tasks)
        continue
    elif choice == 4:
        delete_task(list_tasks)
        continue
    elif choice == 5:
        print("До наступної зустрічі!")
    break
