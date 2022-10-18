from enum import Enum
import model_divide
import model_mult
import model_pow
import model_sqrt
import model_subtraction
import model_sum


class OperationType(Enum):
    EXIT = 0
    DIVIDE = 1
    MULTIPLY = 2
    POWER = 3
    SQRT = 4
    SUBTRACTION = 5
    SUM = 6


def main():
    view.show_greetings()
    while True:
        operation_type = view.get_operation_type()
        # Python настолько крив что не может сравнивать Enum:
        # operation_type is OperationType.ADD
        # поэтому приходится сравнивать их порядковые значения(((
        if operation_type.value == OperationType.ADD.value:
            add_entry()
        elif operation_type.value == OperationType.FIND.value:
            find_entry(view.get_name_for_search())
        elif operation_type.value == OperationType.IMPORT.value:
            import_data()
        elif operation_type.value == OperationType.EXPORT.value:
            export_data()
        elif operation_type.value == OperationType.EXIT.value:
            view.show_goodbye()
            break


if __name__ == '__main__':
    main()
