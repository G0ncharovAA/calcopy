def show_greetings():
    print("Добро пожаловать в CalcoPy!")


def king_menu():
    answer = input(
        "1 - divide (Деление)\n2 - int divide (Целочисленное деление)\n3 - reminder (Остаток от деления)\n4 - mult (Умножение)\n5 - pow (Возведенее в степень)\n6 - sqrt (Квадратный корень)\n7 - subtraction (Вычетание)\n8 - sum (Сложение)\n0 - выход\nКакую операцию Вам необходимо произвести?: ")
    return answer


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
