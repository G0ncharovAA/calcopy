import model_divide  as div
import model_mult  as mult
import model_pow  as pow
import model_sqrt  as sqrt
import model_subtraction  as sub
import model_sum  as sum


def show_greetings():
    print("Добро пожаловать в CalcoPy!")


def king_menu():
    answer = int(input("1 - divide (Деление)\n2 - mult (Умножение)\n3 - pow (Возведенее в степень)\n4 - sqrt (Квадратный корень)\n5 - subtraction (Вычетание)\n6 - sum (Слажение)\n0 - выход\nКакую операцию Вам необходимо произвести? :"))
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
    return input("Использовать ли комплесные аргументы? ")


def show_error(error):
    print(f"Произошла ошибка: {error}")