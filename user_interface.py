import compl
def show_greetings():
    print("Добро пожаловать в CalcoPy!")


def king_menu():
    answer = input(
        "1 - divide (Деление)\n2 - int divide (Целочисленное деление)\n3 - reminder (Остаток от деления)\n4 - mult (Умножение)\n5 - pow (Возведенее в степень)\n6 - sqrt (Квадратный корень)\n7 - subtraction (Вычетание)\n8 - sum (Сложение)\n0 - выход\nКакую операцию Вам необходимо произвести?: ")
    if int(answer) > 8 or int(answer) < 0:
        print("Не верное значение...")
        return king_menu()
    return int(answer)

def ask_for_complexity():
    if ask_for_complex() == "Да":
        arg1real, arg1complex = enter_complex_argument()
        arg2real, arg2complex = enter_complex_argument()
        arg1 = compl.get_compl(float(arg1real), float(arg1complex))
        arg2 = compl.get_compl(float(arg2real), float(arg2complex))
    else:
        arg1 = float(enter_real_argument())
        arg2 = float(enter_real_argument())
    return arg1, arg2
def enter_real_argument():
    return input("Введите вещественный аргумент: ")


def enter_complex_argument():
    real_part = input("Введите вещественную часть: ")
    complex_part = input("Введите комплексную часть: ")
    return real_part, complex_part


def show_result(result):
    print(f"Результат выполнеия операции: {result}")


def ask_for_complex():
    return input("Использовать ли комплесные аргументы? [Да/Нет]")


def show_error(error):
    print(f"Произошла ошибка: {error}")


def show_goodbye():
    print("Вы вышли из программы")
