import socket

lang = input("Please enter language: ")

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('localhost', 1337))

while True:
    message = input("Enter you message : ")

    if message == '!q':
        client.close()
        break
    else:
        client.send(f'[{lang}]{message}'.encode())
        

