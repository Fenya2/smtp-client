import socket
import ssl
import base64
import random


host_addr = 'smtp.yandex.ru.'
port = 465
user_name = 'dim.di44ich'
application_password = 'ompssnaaulfcayzq'


def generate_random_str():
    return "boundary_askljhvaxmsvhdkl"


def request(socket, request):
    socket.send(request + b'\n')
    recv_data = socket.recv(65535).decode()
    return recv_data


def create_letter():
    with open('headers.txt', 'r') as file:
        letter = file.read() + '\n'        
    boundary = generate_random_str()

    letter += f"""Content-Type: multipart/mixed;
    boundary=\"{boundary}\""""
    letter += '\n\n'
    letter += f'--{boundary}'
    # TODO заголовки для текста (Content-Type, \n)
    with open('body.txt', 'r') as file:
        letter += file.read() + '\n'
    letter += f'--{boundary}' + '\n'
    # TODO заголовки для картинки (Content-Type, \n)
    with open('cat.jpg', 'rb') as file:
        letter += base64.b64encode(file.read()).decode()
    letter += '\n'
    letter += f'--{boundary}--' + '\n.\n'
    return letter


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host_addr, port))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    client = context.wrap_socket(client)
    print(client.recv(1024))
    print(request(client, bytes(f"EHLO {user_name}", 'utf-8')))
    # base64login = base64.b64encode(user_name.encode())
    # base64password = base64.b64encode(application_password.encode())
    # print(request(client, b'AUTH LOGIN'))
    # print(request(client, base64login))
    # print(request(client, base64password))
    # print(request(client, b'MAIL FROM:dim.di44ich@yandex.ru'))
    # print(request(client, b'RCPT TO:dim74.09@mail.ru'))
    
    # print(request(client, b'DATA'))
    
    # create_letter(headers)

    # print(request(client, bytes(letter, 'utf-8')))
    # print(request(client, b'QUIT'))