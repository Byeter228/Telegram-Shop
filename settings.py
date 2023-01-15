
# Token telegram bot
bot_token = '' # токен бота
CHANNELID = 1 # id канала куда будет отсылаться информация, ид без -100 в начале (например: 124873248) - указать заместо нуля

# ID admin
admin_id = 1 # id админа - указать заместо нуля

bot_name = 'bot name' # логин бота
referrral_percent = 15 # Процент реферальной системы

QIWI_NUMBER = 'qiwi number'    # номер киви
QIWI_TOKEN = 'qiwi token'            # токен киви

# Текст после покупки
text_purchase = '❕ Вы выбрали: ' \
                '{name}\n\n' \
                '{info}\n\n' \
                '💠 Цена: {price} рублей\n' \
                '💠 Кол-во товара: {amount}' \


# Информация
info = '''🏠 Магазин: Название магазина
⏰ Дата создания: любая
 \n'''

# Помощь
helps = '''🚑 Текст\n'''

# Пополнение баланса
balance_replenish='⚠️ Пополнение баланса\n\n' \
                    '🥝 QIWI-кошелек:\n<pre>{number}</pre>\n\n' \
                    '📝 Комментарий к переводу:\n<pre>{code}</pre>\n➖➖➖➖➖➖➖➖➖➖\n\n' \
                    'Пополните указанный киви кошелёк на любую сумму.\n' \
                    'Перевод должен быть совершён с киви кошелька.\n' \
                    'Обязательно в рублях.\n\n' \
                    'При нажатии на "🌐 Перейти к оплате", Вам останется ввести лишь сумму платежа.'

# Профиль
profile = '🧾 Профиль\n➖➖➖➖➖➖➖➖➖➖\n' \
          '❤️ Ваш логин - {login}\n' \
          '👨‍💻 Ваш id - {id}\n' \
          '💰 Ваш баланс - {balance} рублей\n' \
          '📝 Дата регистрации - {data}\n➖➖➖➖➖➖➖➖➖➖\n'
