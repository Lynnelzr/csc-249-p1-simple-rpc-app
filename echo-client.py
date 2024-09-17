#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
# MSG = "Hello, world"

def run_client():
    print("Client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            if not talk_to_server(s):
                break
    print("Client is disconnecting...")

def talk_to_server(sock):
    operation = input("Enter the operation (converting to usd / converting from usd): ")
    num1 = input("Enter the exchange rate (other currency/usd): ")
    num2 = input("Enter the amount of money: ")
    message = f"{operation}:{num1}:{num2}"
    print(f"connection established, sending request '{message}'")
    sock.sendall(message.encode('utf-8'))
    print("Message sent, waiting for reply")
    reply = sock.recv(1024)
    
    if not reply:
        print("No reply from server.")
        return False
    else:
        print(f"Received reply: {reply.decode('utf-8')}")
        return True

if __name__ == "__main__":
    run_client()
    print("Client has exited.")
