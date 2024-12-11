# "Рассылка писем"
def send_email(message,recipient,sender = "university.help@gmail.com"):
    if not("@" in recipient and "@" in sender) or not('.com' in recipient or '.ru' in recipient or '.net' in recipient) or not('.com' in sender or '.ru' in sender or '.net' in sender):
        my_str = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    elif recipient.lower() == sender.lower():
        my_str = 'Нельзя отправить письмо самому себе!'
    elif sender.lower() == 'university.help@gmail.com'.lower():
        my_str = f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
    else:
        my_str = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'
    print(my_str)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')