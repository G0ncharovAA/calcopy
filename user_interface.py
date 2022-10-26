from telegram import Update
from telegram.ext import CallbackContext


def tele_print(update: Update, context: CallbackContext, output):
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)


def show_greetings():
    welcome = "Добро пожаловать в CalcoPy!"
    return welcome


def king_menu():
    return "1 - divide (Деление)\n2 - int divide (Целочисленное деление)\n3 - reminder (Остаток от деления)\n4 - mult (Умножение)\n5 - pow (Возведение в степень)\n6 - sqrt (Квадратный корень)\n7 - subtraction (Вычетание)\n8 - sum (Сложение)\n0 - выход\nКакую операцию Вам необходимо произвести?: "


def enter_real_argument():
    return "Введите вещественный аргумент: "


def enter_complex_argument():
    return "Введите комлексный аргумент, <вещественная часть> <комплексная чать> разделены пробелом: "


def show_result(result):
    result_show = f"Результат выполнения операции: {result}"
    return result_show


def ask_for_complex():
    return "Использовать ли комплесные аргументы? [Да/Нет]"


def show_error(error):
    error_show = f"Произошла ошибка: {error}"
    return error_show


def show_goodbye():
    bye = "Вы вышли из программы"
    return bye
