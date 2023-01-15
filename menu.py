from telebot import types


# Main menu
main_menu = types.InlineKeyboardMarkup(row_width=3)
main_menu.add(
    types.InlineKeyboardButton(text='🛍️ Каталог', callback_data='catalog')
)

main_menu.add(
    types.InlineKeyboardButton(text='👤 Профиль', callback_data='profile'),
    types.InlineKeyboardButton(text='👥 Реферальная сеть', callback_data='referral_link')
)

main_menu.add(
    types.InlineKeyboardButton(text='ℹ️ Информация', callback_data='info'),
    types.InlineKeyboardButton(text='🛒 Мои покупки', callback_data='all_purchases'),
    types.InlineKeyboardButton(text='🆘 Помощь', callback_data='need_help')
)

main_menu.add(
    types.InlineKeyboardButton(text='💸 Пополнить баланс', callback_data='balance_repenish'),
)

# Admin menu
admin_menu = types.InlineKeyboardMarkup(row_width=2)
admin_menu.add(types.InlineKeyboardButton(text='🛍️ Управление каталогом', callback_data='catalog_control'), types.InlineKeyboardButton(text='📦 Управление товаром', callback_data='control_of_sections'))
admin_menu.add(types.InlineKeyboardButton(text='💸 Настройка платёжек', callback_data='edit_pay'), types.InlineKeyboardButton(text='💵 Изменить баланс', callback_data='give_money'))
admin_menu.add(types.InlineKeyboardButton(text='📢 Рассылка', callback_data='send_message_admin'), types.InlineKeyboardButton(text='💳 Топ рефералов(доходы)', callback_data='admin_top_referral'))
admin_menu.add(types.InlineKeyboardButton(text='📊 Информация', callback_data='admin_info'))

admin_menu.add(types.InlineKeyboardButton(text='❌ Выйти', callback_data='exit_admin'))


# Qiwi Balance
pay_menu_control_catalog = types.InlineKeyboardMarkup(row_width=2)
pay_menu_control_catalog.add(types.InlineKeyboardButton(text='🌐 Баланс', callback_data='qiwi_check_pay'))
pay_menu_control_catalog.add(
    types.InlineKeyboardButton(text='💳 Получить QIWI', callback_data='qiwi_request'),
    types.InlineKeyboardButton(text='📤 Отправить QIWI', callback_data='qiwi_send')
)
pay_menu_control_catalog.add(types.InlineKeyboardButton(text='❌ Выйти', callback_data='back_admin_menu'))

# Admin control
admin_menu_control_catalog = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_catalog.add(
    types.InlineKeyboardButton(text='Добавить раздел в каталог', callback_data='add_section_catalog'),
    types.InlineKeyboardButton(text='Удалить раздел в каталог', callback_data='delete_section_catalog'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_admin_menu')
)

# Admin control section
admin_menu_control_section = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_section.add(
    types.InlineKeyboardButton(text='Добавить товар в раздел', callback_data='add_product_section'),
    types.InlineKeyboardButton(text='Удалить товар из раздела', callback_data='delete_product_section'),
    types.InlineKeyboardButton(text='Загрузить товар', callback_data='product_download'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_admin_menu')
)

# Back to admin menu
back_admin_menu = types.InlineKeyboardMarkup(row_width=1)
back_admin_menu.add(
    types.InlineKeyboardButton(text='Вернуться в админ меню', callback_data='back_admin_menu')
)

btn_purchase = types.InlineKeyboardMarkup(row_width=2)
btn_purchase.add(
    types.InlineKeyboardButton(text='Купить', callback_data='buy'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_menu')
)

btn_ok = types.InlineKeyboardMarkup(row_width=3)
btn_ok.add(
    types.InlineKeyboardButton(text='Понял', callback_data='btn_ok')
)

to_close = types.InlineKeyboardMarkup(row_width=3)
to_close.add(
    types.InlineKeyboardButton(text='❌', callback_data='to_close')
)

balance_repenish = types.InlineKeyboardMarkup(row_width=3)
balance_repenish.add(
          types.InlineKeyboardButton(text='🥝 Qiwi', callback_data='balance_replenish'),
          types.InlineKeyboardButton(text='📤 BTC', callback_data='balance_renish'),
          types.InlineKeyboardButton(text='❌ Выйти', callback_data='to_close')
)





