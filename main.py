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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
