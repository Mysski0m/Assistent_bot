from functions import (start, oge_menu, ege_menu, main_menu, send_test,
                       test_answer, contact, forward_message_to_or_for_teacher,
                       get_stat)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# Основная функция
def main() -> None:
    updater = Updater("XXXXX")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex('^(ОГЭ)$'), oge_menu))
    dp.add_handler(MessageHandler(Filters.regex('^(ЕГЭ)$'), ege_menu))
    dp.add_handler(MessageHandler(Filters.regex('^(Главное меню)$'), main_menu))
    dp.add_handler(MessageHandler(Filters.regex('^(Отправить сочинение)$'), contact))
    dp.add_handler(MessageHandler(Filters.regex('^(Посмотреть статистику)$'), get_stat))

    # Добавляем фильтры для кнопок ОГЭ
    for i in range(1, 13):
        dp.add_handler(MessageHandler(Filters.regex(f'^№{i}$'), send_test))

    # Добавляем фильтры для кнопок ЕГЭ
    for i in range(1, 28):
        dp.add_handler(MessageHandler(Filters.regex(f'^№{i}$'), send_test))

    dp.add_handler(CallbackQueryHandler(test_answer))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message_to_or_for_teacher))
    dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, forward_message_to_or_for_teacher))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
