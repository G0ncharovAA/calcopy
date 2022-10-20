from enum import Enum

import logg
import compl
import model_divide
import model_mult
import model_pow
import model_sqrt
import model_subtraction
import model_sum
import user_interface as ui


class OperationType(Enum):
    EXIT = 0
    DIVIDE = 1
    DIVIDE_INTEGER = 2
    REMINDER = 3
    MULTIPLY = 4
    POWER = 5
    SQRT = 6
    SUBTRACTION = 7
    SUM = 8


def main():
    ui.show_greetings()
    while True:
        operation_type = OperationType(int(ui.king_menu()))
        match operation_type:
            case OperationType.EXIT:
                ui.show_goodbye()
                break
            case OperationType.DIVIDE:
                perform_divide()
            case OperationType.MULTIPLY:
                perform_multiply()
            case OperationType.POWER:
                perform_power()
            case OperationType.SUBTRACTION:
                perform_subtraction()
            case OperationType.SUM:
                perform_sum()
            case OperationType.DIVIDE_INTEGER:
                perform_divide_integer()
            case OperationType.REMINDER:
                perform_reminder()
            case OperationType.SQRT:
                perform_sqrt()


def ask_for_complexity():
    if ui.ask_for_complex() == "Да":
        arg1real, arg1complex = ui.enter_complex_argument()
        arg2real, arg2complex = ui.enter_complex_argument()
        arg1 = compl.get_compl(float(arg1real), float(arg1complex))
        arg2 = compl.get_compl(float(arg2real), float(arg2complex))
    else:
        arg1 = float(ui.enter_real_argument())
        arg2 = float(ui.enter_real_argument())
    return arg1, arg2


def perform_divide():
    try:
        args = ask_for_complexity()
        model_divide.init(args[0], args[1])
        result = model_divide.division()
        ui.show_result(result)
        logg.SaveRecordToLogFile(["выполняется операция деления", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        ui.show_error(ex)
        logg.SaveRecordToLogFile(["возникла ошибка", "в операции деления", f"ошибка {ex}"])


def perform_divide_integer():
    try:
        args = ask_for_complexity()
        model_divide.init(args[0], args[1])
        result = model_divide.integer_division()
        ui.show_result(result)
        logg.SaveRecordToLogFile(
            ["выполняется операция целочисленного деления", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        ui.show_error(ex)
        logg.SaveRecordToLogFile(["возникла ошибка", "в операции целочисленного деления", f"ошибка {ex}"])


def perform_reminder():
    try:
        args = ask_for_complexity()
        model_divide.init(args[0], args[1])
        result = model_divide.remainder_division()
        ui.show_result(result)
        logg.SaveRecordToLogFile(
            ["выполняется операция вычисления остатка от деления", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        ui.show_error(ex)
        logg.SaveRecordToLogFile(["возникла ошибка", "в операции вычисления остатка от деления", f"ошибка {ex}"])


def perform_multiply():
    try:
        args = ask_for_complexity()
        model_mult.init(args[0], args[1])
        result = model_mult.multyply()
        ui.show_result(result)
        logg.SaveRecordToLogFile(["выполняется операция умножения", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        ui.show_error(ex)
        logg.SaveRecordToLogFile(["возникла ошибка", "в операции умножения", f"ошибка {ex}"])


def perform_power():
    try:
        args = ask_for_complexity()
        model_pow.init(args[0], args[1])
        result = model_pow.my_pow()
        ui.show_result(result)
        logg.SaveRecordToLogFile(
            ["выполняется операция возведения в степень", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        ui.show_error(ex)
        logg.SaveRecordToLogFile(["возникла ошибка", "в операции возведения в степень", f"ошибка {ex}"])


def perform_sqrt():
    try:
        if ui.ask_for_complex() == "Да":
            argreal, argcomplex = ui.enter_complex_argument()
            arg = compl.get_compl(float(argreal), float(argcomplex))
        else:
            arg = float(ui.enter_real_argument())
        model_sqrt.init(arg)
        result = model_sqrt.my_sqrt()
        ui.show_result(result)
        logg.SaveRecordToLogFile(
            ["выполняется операция извлечения квадратного корня", f"аргументы: {arg}", f"результат: {result}"])
    except Exception as ex:
        ui.show_error(ex)
        logg.SaveRecordToLogFile(["возникла ошибка", "в операции извлечения квадратного корня", f"ошибка {ex}"])


def perform_subtraction():
    try:
        args = ask_for_complexity()
        model_subtraction.init(args[0], args[1])
        result = model_subtraction.subtraction()
        ui.show_result(result)
        logg.SaveRecordToLogFile(["выполняется операция вычитания", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        ui.show_error(ex)
        logg.SaveRecordToLogFile(["возникла ошибка", "в операции вычитания", f"ошибка {ex}"])


def perform_sum():
    try:
        args = ask_for_complexity()
        model_sum.init(args[0], args[1])
        result = model_sum.my_sum()
        ui.show_result(result)
        logg.SaveRecordToLogFile(["выполняется операция сложения", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        ui.show_error(ex)
        logg.SaveRecordToLogFile(["возникла ошибка", "в операции сложения", f"ошибка {ex}"])


if __name__ == '__main__':
    main()
