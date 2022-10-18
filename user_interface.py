import model_divide  as div
import model_mult  as mult
import model_pow  as pow
import model_sqrt  as sqrt
import model_subtraction  as sub
import model_sum  as sum


def king_menu():
    print("Добро пожаловать в CalcoPy!")
    answer = int(input("1 - divide (Деление)\n2 - mult (Умножение)\n3 - pow (Возведенее в степень)\n4 - sqrt (Квадратный корень)\n5 - subtraction (Вычетание)\n6 - sum (Слажение)\nКакую операцию Вам необходимо произвести? :"))
    while True:
        match answer:
            case 1:
                print(div.div_menu())
            case 2:
                print(mult.multyply())
            case 3:
                print(pow.my_pow())
            case 4:
                print(sqrt.sqrt())
            case 5:
                print(sub.subtraction())
            case 6:
                print(sum.sum())

print(king_menu())

# print("Добро пожаловать в CalcoPy!")

# answer = int(input("1 - divide (Деление)\n2 - mult (Умножение)\n3 - pow (Возведенее в степень)\n4 - sqrt (Квадратный корень)\n5 - subtraction (Вычетание)\n6 - sum (Слажение)\nКакую операцию Вам необходимо произвести? :"))
# while True:
#     match answer:
#         case 1:
#             print(div.div_menu())
#         case 2:
#             print(mult.multyply())
#         case 3:
#             print(pow.pow())
#         case 4:
#             print(sqrt.sqrt())
#         case 5:
#             print(sub.subtraction())
#         case 6:
#             print(sum.sum())

