from enum import Enum
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


def ask_for_complexity():
    if ui.ask_for_complex():
        arg1real, arg1complex = ui.enter_complex_argument()
        arg2real, arg2complex = ui.enter_complex_argument()
        arg1 = complex(float(arg1real), float(arg1complex))
        arg2 = complex(float(arg2real), float(arg2complex))
    else:
        arg1 = ui.enter_real_argument()
        arg2 = ui.enter_real_argument()
    return arg1, arg2


def perform_divide():
    try:
        args = ask_for_complexity()
        result = model_divide.division(args[0], args[1])
        ui.show_result(result)
    except Exception as ex:
        ui.show_error(ex)


def perform_multiply():
    try:
        args = ask_for_complexity()
        result = model_mult.multyply(args[0], args[1])
        ui.show_result(result)
    except Exception as ex:
        ui.show_error(ex)


if __name__ == '__main__':
    main()
