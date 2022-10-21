from enum import Enum

import user_interface as ui
import excep


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
        operation_type = OperationType(excep.check_input_main())
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


def perform_divide():
    excep.check_divide()


def perform_divide_integer():
    excep.check_divide_integer()


def perform_reminder():
    excep.check_remainder_division()


def perform_multiply():
    excep.check_mult()


def perform_power():
    excep.check_pow()


def perform_sqrt():
    excep.check_sqrt()


def perform_subtraction():
    excep.check_subtraction()


def perform_sum():
    excep.check_summ()


if __name__ == '__main__':
    main()
