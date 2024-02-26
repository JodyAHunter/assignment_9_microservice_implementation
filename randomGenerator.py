import socket
import json
import random
import lorem_ipsum_word_bank


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind(("127.0.0.1", 65432))
    socket.listen()
    conn, addr = socket.accept()
    with conn:
        while True:
            recv_data = conn.recv(4096)
            if not recv_data:
                break
            data = json.loads(recv_data.decode())

            # Code block for testing connection
            if data == "Hi I'm the frontend":
                print("SERVER: receiving message from client...")
                print(f"SERVER: message received - {data!r}")
                data = data.upper()
                print("SERVER: Sending message back to client...")
                conn.sendall(data.encode())

            number_of_words = data[1]

            if data[0] == 1:
                if number_of_words > 2:
                    lorem_ipsum_string = "Lorem ipsum"
                    word_count = number_of_words - 2
                else:
                    lorem_ipsum_string = ""
                    word_count = number_of_words

                number_in_word_bank = len(lorem_ipsum_word_bank.word_bank)

                for word in range(word_count):
                    randomized_index = random.randint(0, number_in_word_bank - 1)
                    random_word = lorem_ipsum_word_bank.word_bank[randomized_index]

                    if not lorem_ipsum_string:
                        lorem_ipsum_string += random_word
                    else:
                        lorem_ipsum_string += " "
                        lorem_ipsum_string += random_word

                conn.sendall(lorem_ipsum_string.encode())
                break
