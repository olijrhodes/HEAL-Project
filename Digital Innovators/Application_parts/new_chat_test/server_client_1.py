import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back


def Start():
    init()

    colours = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
               Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
               Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
               Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
               ]

    client_colour = random.choice(colours)

    SERVER_HOST = "127.0.0.1"  # change to the ip address of the device the server is located on
    SERVER_PORT = 5002
    separator_token = "<SEP>"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")

    s.connect((SERVER_HOST, SERVER_PORT))

    print("[+] Connected.")

    name = input("Enter Your Name: ")

    def listen_for_messages():
        while True:
            message = s.recv(1025).decode('utf-8')
            print("\n" + message)

    t = Thread(target=listen_for_messages)

    t.daemon = True

    t.start()

    while True:
        to_send = input()
        if to_send.lower() == "q":
            break

        date_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        to_send = f"{client_colour}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
        s.send(to_send.encode())

    s.close()
