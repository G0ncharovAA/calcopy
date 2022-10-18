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
    print("Добро пожаловать в CalcoPy!")


if __name__ == '__main__':
    main()
