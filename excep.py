import compl
import model_sum
import model_pow
import model_mult
import model_sqrt
import model_subtraction

from logg import SaveRecordToLogFile
from model_divide import init, division, integer_division, remainder_division
from user_interface import king_menu, show_result, show_error, enter_complex_argument
from user_interface import ask_for_complex, enter_real_argument, ask_for_complexity



def check_input_main():
    try:
        result = king_menu()
        return result
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в выборе пункта меню", f"ошибка {ex}"])
        return check_input_main()


def check_divide():
    try:
        args = ask_for_complexity()
        init(args[0], args[1])
        result = division()
        show_result(result)
        SaveRecordToLogFile(
            ["выполняется операция деления", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в операции деления", f"ошибка {ex}"])


def check_divide_integer():
    try:
        args = ask_for_complexity()
        init(args[0], args[1])
        result = int(integer_division())
        show_result(result)
        SaveRecordToLogFile(
            ["выполняется операция целочисленного деления", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в операции целочисленного деления", f"ошибка {ex}"])


def check_remainder_division():
    try:
        args = ask_for_complexity()
        init(args[0], args[1])
        result = int(remainder_division())
        show_result(result)
        SaveRecordToLogFile(
            ["выполняется операция вычисления остатка от деления", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в операции вычисления остатка от деления", f"ошибка {ex}"])


def check_mult():
    try:
        args = ask_for_complexity()
        model_mult.init(args[0], args[1])
        result = model_mult.multyply()
        if args[0]%1 == 0 and args[1]%1 == 0 and result%1 == 0:
            result=int(result)
        show_result(result)
        SaveRecordToLogFile(["выполняется операция умножения",
                            f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в операции умножения", f"ошибка {ex}"])


def check_pow():
    try:
        args = ask_for_complexity()
        model_pow.init(args[0], args[1])
        result = model_pow.my_pow()
        show_result(result)
        SaveRecordToLogFile(
            ["выполняется операция возведения в степень", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в операции возведения в степень", f"ошибка {ex}"])


def check_sqrt():
    try:
        if ask_for_complex() == "Да":
            argreal, argcomplex = enter_complex_argument()
            arg = compl.get_compl(float(argreal), float(argcomplex))
        else:
            arg = float(enter_real_argument())
        model_sqrt.init(arg)
        result = model_sqrt.my_sqrt()
        show_result(result)
        SaveRecordToLogFile(
            ["выполняется операция извлечения квадратного корня", f"аргументы: {arg}", f"результат: {result}"])
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в операции извлечения квадратного корня", f"ошибка {ex}"])


def check_subtraction():
    try:
        args = ask_for_complexity()
        model_subtraction.init(args[0], args[1])
        result = model_subtraction.subtraction()        
        if args[0]%1 == 0 and args[1]%1 == 0 and result%1 == 0:
            result=int(result)
        show_result(result)
        SaveRecordToLogFile(
            ["выполняется операция вычитания", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в операции вычитания", f"ошибка {ex}"])


def check_summ():
    try:
        args = ask_for_complexity()
        model_sum.init(args[0], args[1])
        result = model_sum.my_sum()
        if args[0]%1 == 0 and args[1]%1 == 0 and result%1 == 0:
            result=int(result)
        show_result(result)
        SaveRecordToLogFile(
            ["выполняется операция сложения", f"аргументы: {args}", f"результат: {result}"])
    except Exception as ex:
        show_error(ex)
        SaveRecordToLogFile(
            ["возникла ошибка", "в операции сложения", f"ошибка {ex}"])
