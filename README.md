# Jody and Michael's Communication Contract for Random Generator Microservice
## How to programmatically request data from the microservice
The user of the client will request data from the microservice via python socket programming (host = "127.0.0.1", port = 65432). The microservice expects user input in the form of a list with two integer values.
For this implementation, the first value is assumed to be 1, which represents the user choosing the Lorem Ipsum Generator service. The second integer value will be the number of words that the user wants in the Lorem Ipsum string.
The user input will be changed from a list type to a json formatted string using the json module dumps method. Then, the user input is sent through the socket to the microservice encoded into byte form. 

Below is an example of the client receiving input from the user, establishing a socket connection with the microservice, and sending the user input to the microservice via json module.

  ```
  import socket
  import json

  choose_generator = int(input("Please enter 1 if you would like to use the Lorem Ipsum Generator: "))
  how_many = int(input("Please enter how many words you would like to generate (maximum of 1000): "))

  user_input = [choose_generator, how_many]

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect(("127.0.0.1", 65432))
    send_data = json.dumps(user_input)
    socket.sendall(send_data.encode())
  ```

## How to programmatically receive data from the microservice
The user of the client will receive data back from the microservice via the previously established socket connection. The recv method from the socket module is used within an infinite while loop, breaking once no more data is being received from the microservice.
Once all data is received back from the microservice (in this case, data should be a complete Lorem Ipsum string consisting of the number of words requested), the data is decoded from byte form and displayed to the user.

  ```
    data = b""
    while True:
        recv_data = socket.recv(4096)
        if not recv_data:
            break
        data += recv_data
    print(f"{data.decode()}")
  ```


## UML Sequence Diagram
![UML](https://github.com/JodyAHunter/assignment_9_microservice_implementation/assets/114111842/cb551200-67ea-4ce2-9e79-b0aa42fb8015)

