from server_client_1 import Start
from chat_server import Start_server
import time
import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

Start_server()
print("Loading...")
time.sleep(3)
Start()