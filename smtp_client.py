import re
import smtplib
import config
import os
import base64

from email.message import EmailMessage


def send(sender, recipients, email):
    """
    Отправляет письмо
    :param sender: почтовый ящик отправителя
    :param recipients: итерируемый объект по почтовым ящикам получателей
    :param email: письмо для отправки
    """
    server = smtplib.SMTP(f'{config.SERVER}:{config.PORT}')
    server.starttls()
    server.login(config.LOGIN, config.PASSWORD)
    server.sendmail(sender, recipients, email)
    server.quit()


def attach_pictures(mail, pictures_dir):
    """
    Прикрепляет картинки из указанной директории к письму
    :param mail: письмо
    :param pictures_dir: директория с картинками
    """
    for pic in os.listdir(pictures_dir):
        with open(pictures_dir + pic, 'rb') as f:
            data = f.read()
        mail.add_attachment(
            data,
            maintype='image',
            subtype='png',
            filename=pic
        )


def get_message_text(file) -> str:
    """
    Возвращает текст письма из файла для отправки
    :param file: файл с письмом
    :returns: текст письма
    """
    with open(file, 'r') as f:
        data = f.read()
    return data


def get_recipients(file):
    """
    Возвращает список получателей, записанных в файл
    :param file: файл с почтами получателей
    :returns: список адресов получателей
    """
    with open(file, 'r') as f:
        data = f.read()
    return re.findall(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+', data)


def generate_subject(subject):
    """
    Кодирует строку в utf-8, полученный байты преобразует
    в base64, и формирует строку для не ascii заголовка
    :param subject: строка - тема письма
    """
    subject = base64.b64encode(subject.encode('utf-8')).decode('ascii')
    return f'=?UTF-8?B?{subject}?='


def create_message():
    """ 
    Формирует сообщения для отправки по конфигу
    """
    msg = EmailMessage()
    msg['From'] = config.SENDER
    msg['TO'] = ', '.join(get_recipients(config.RECIPIENTS))
    msg['Subject'] = generate_subject(config.SUBJECT)
    msg.set_content(get_message_text(config.TEXT))
    attach_pictures(msg, config.PICTURES)
    return msg


def main():
    msg = create_message()
    send(config.SENDER, re.split(r', ', msg['To']), str(msg))


if __name__ == '__main__':
    main()
