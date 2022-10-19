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
    MULTIPLY = 2
    POWER = 3
    SQRT = 4
    SUBTRACTION = 5
    SUM = 6


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


def ask_for_complexity():
    if ui.ask_for_complex():
        arg1real, arg1complex = ui.enter_complex_argument()
        arg2real, arg2complex = ui.enter_complex_argument()
        arg1 = compl.get_compl(arg1real, arg1complex)
        arg2 = compl.get_compl(arg2real, arg2complex)
    else:
        arg1 = ui.enter_real_argument()
        arg2 = ui.enter_real_argument()
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
