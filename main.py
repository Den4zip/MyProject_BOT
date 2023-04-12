def print_hi():
    print("Как тебя зовут?")
    name = input()
    print("Сколько тебе лет?")
    age = int(input())
    print(f"Привет, {name},")
    if 6 < age < 18:
        print("Ну ты и школьник")
    if 18 < age < 25:
        print("Ну ты студент")
    print("Арбуз будешь?")


if __name__ == '__main__':
    print_hi()
