from enum import Enum
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


args = []


def start(update: Update, context: CallbackContext) -> int:
    ui.tele_print(update = update, context = context, output = ui.show_greetings())
    ui.tele_print(update=update, context=context, output=ui.king_menu())
    return 0


def on_next(update: Update, context: CallbackContext) -> int:
    operation_type = excep.check(OperationType, update.message.text)
    match operation_type:
        case OperationType.EXIT:
            ui.tele_print(update=update, context=context, output=ui.show_goodbye())
            return ConversationHandler.END
        case OperationType.DIVIDE:
            pass
        case OperationType.MULTIPLY:
            pass
        case OperationType.POWER:
            pass
        case OperationType.SUBTRACTION:
            pass
        case OperationType.SUM:
            pass
        case OperationType.DIVIDE_INTEGER:
            pass
        case OperationType.REMINDER:
            pass
        case OperationType.SQRT:
            pass
        case _:
          ui.tele_print(update=update, context=context, output=ui.show_error(operation_type))
    return 0


def cancel(update: Update, context: CallbackContext) -> int:
    ui.tele_print(update=update, context=context, output=ui.show_goodbye())
    return ConversationHandler.END

def __perform_divide():
    pass

def main():
    updater = Updater(KEY)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            0: [MessageHandler(Filters.all, on_next)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
