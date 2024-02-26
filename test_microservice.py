import socket
import json


test_connection_message = "Hi I'm the frontend"  # test for successful socket connection

user_input = []

choose_generator = int(input("Please enter 1 if you would like to use the Lorem Ipsum Generator: "))
how_many = int(input("Please enter how many words you would like to generate (maximum of 1000): "))

user_input.append(choose_generator)
user_input.append(how_many)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect(("127.0.0.1", 65432))
    send_data = json.dumps(user_input)
    socket.sendall(send_data.encode())

    data = b""  # will hold all data received
    while True:
        recv_data = socket.recv(4096)
        if not recv_data:
            break
        data += recv_data

    print("Calling Random Generator Microservice...")
    print("Receiving randomized Lorem Ipsum text...")
    print(f"{data.decode()}")
