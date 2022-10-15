from enum import Enum
from model_divide import division, integer_division, remainder_division
from model_mult import multyply
from model_pow import pow
from model_sqrt import sqrt
from model_subtraction import subtraction
from model_sum import sum


class OperationType(Enum):
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
