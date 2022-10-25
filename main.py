from enum import Enum
import model_mult
import model_divide
import model_sqrt
import model_pow
import model_subtraction
import model_sum
from secret import KEY
import user_interface as ui
import excep
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)


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


current_operation: OperationType = OperationType.EXIT
args = []

# bread crumbs
MENU, COMPLEXITY, REAL_ARGUMENT, COMPLEX_ARGUMENT = range(4)


def check_yes_or_no(arg):
    if arg.lower() == "да" or arg.lower() == "нет":
        return arg.lower()
    else:
        return Exception(f"{arg}")


def execute_operation(args):
    match args[0]:
        case OperationType.DIVIDE:
            model_divide.init(args[1], args[2])
            return model_divide.division()
        case OperationType.DIVIDE_INTEGER:
            model_divide.init(args[1], args[2])
            return model_divide.integer_division()
        case OperationType.REMINDER:
            model_divide.init(args[1], args[2])
            return model_divide.remainder_division()
        case OperationType.MULTIPLY:
            model_mult.init(args[1], args[2])
            return model_mult.multyply()
        case OperationType.POWER:
            model_pow.init(args[1], args[2])
            return model_pow.my_pow()
        case OperationType.SQRT:
            model_sqrt.init(args[1])
            return model_sqrt.my_sqrt()
        case OperationType.SUBTRACTION:
            model_subtraction.init(args[1], args[2])
            return model_subtraction.subtraction()
        case OperationType.SUM:
            model_sum.init(args[1], args[2])
            return model_sum.my_sum()


def start(update: Update, context: CallbackContext) -> int:
    ui.tele_print(update=update, context=context, output=ui.show_greetings())
    ui.tele_print(update=update, context=context, output=ui.king_menu())
    return MENU


def handle_menu(update: Update, context: CallbackContext) -> int:
    global args
    args = []
    global current_operation
    current_operation = excep.check(OperationType, update.message.text)
    if current_operation == OperationType.EXIT:
        ui.tele_print(update=update, context=context, output=ui.show_goodbye())
        return ConversationHandler.END
    elif issubclass(current_operation, OperationType):
        ui.tele_print(update=update, context=context, output=ui.ask_for_complex())
        return COMPLEXITY
    else:
        ui.tele_print(update=update, context=context, output=ui.show_error(current_operation))
    return ConversationHandler.MENU


def handle_сomplexity(update: Update, context: CallbackContext) -> int:
    use_complexity = excep.check(check_yes_or_no, update.message.text)
    if use_complexity == "да":
        ui.tele_print(update=update, context=context, output=ui.enter_complex_argument())
        return COMPLEX_ARGUMENT
    elif use_complexity == "нет":
        ui.tele_print(update=update, context=context, output=ui.enter_real_argument())
        return REAL_ARGUMENT
    else:
        ui.tele_print(update=update, context=context, output=ui.show_error(f"{use_complexity} - не Да/Нет"))
        return COMPLEXITY


def handle_real_argument(update: Update, context: CallbackContext) -> int:
    arg = excep.check(float, update.message.text)
    if isinstance(arg, float):
        args.append(arg)
        if current_operation == OperationType.SQRT:
            operation_args = [current_operation].extend(args)
            result = excep.check(execute_operation, operation_args)
            if issubclass(result, Exception):
                ui.tele_print(update=update, context=context, output=ui.show_error(result))
            else:
                ui.tele_print(update=update, context=context, output=ui.show_result(result))
                ui.tele_print(update=update, context=context, output=ui.king_menu())
                return MENU
        else:
            if len(args) < 2:
                ui.tele_print(update=update, context=context, output=ui.enter_real_argument())
                return REAL_ARGUMENT
            else:
                operation_args = [current_operation].extend(args)
                result = excep.check(execute_operation, operation_args)
                if issubclass(result, Exception):
                    ui.tele_print(update=update, context=context, output=ui.show_error(result))
                else:
                    ui.tele_print(update=update, context=context, output=ui.show_result(result))
                    ui.tele_print(update=update, context=context, output=ui.king_menu())
                    return MENU
    else:
        ui.tele_print(update=update, context=context, output=ui.show_error(f"{arg} - не число"))
        return REAL_ARGUMENT


def handle_complex_argument
    arg = excep.check(float, update.message.text)
    if isinstance(arg, float):
        args.append(arg)
        if current_operation == OperationType.SQRT:
            operation_args = [current_operation].extend(args)
            result = excep.check(execute_operation, operation_args)
            if issubclass(result, Exception):
                ui.tele_print(update=update, context=context, output=ui.show_error(result))
            else:
                ui.tele_print(update=update, context=context, output=ui.show_result(result))
                ui.tele_print(update=update, context=context, output=ui.king_menu())
                return MENU
        else:
            if len(args) < 2:
                ui.tele_print(update=update, context=context, output=ui.enter_real_argument())
                return REAL_ARGUMENT
            else:
                operation_args = [current_operation].extend(args)
                result = excep.check(execute_operation, operation_args)
                if issubclass(result, Exception):
                    ui.tele_print(update=update, context=context, output=ui.show_error(result))
                else:
                    ui.tele_print(update=update, context=context, output=ui.show_result(result))
                    ui.tele_print(update=update, context=context, output=ui.king_menu())
                    return MENU
    else:
        ui.tele_print(update=update, context=context, output=ui.show_error(f"{arg} - не число"))
        return REAL_ARGUMENT

def cancel(update: Update, context: CallbackContext) -> int:
    ui.tele_print(update=update, context=context, output=ui.show_goodbye())
    return ConversationHandler.END


def main():
    updater = Updater(KEY)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [MessageHandler(Filters.all, handle_menu)],
            COMPLEXITY: [MessageHandler(Filters.all, handle_сomplexity)],
            REAL_ARGUMENT: [MessageHandler(Filters.all, on_next)],
            COMPLEX_ARGUMENT: [MessageHandler(Filters.all, on_next)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
