class SMTP_sender:
    """
    Отправляет письма указанным получателям
    """
    def __init__(self, server=None, login=None, password=None):
        """
        :param server: доменное имя smtp-сервера
        :param login: логин отправителя
        :param password: пароль отправителя
        :param token: токен (другой способ авторизации)
        """
        self._smtp_server = server
        self._login = login
        self._password = password
    
    def send(letter: str):
