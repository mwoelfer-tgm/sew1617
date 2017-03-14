import socket
from enum import Enum
from optparse import OptionParser
from Game.HeinzelModel import HeinzelClient
import time

#!/usr/bin/python
# -*- coding: ascii -*-

def rec_fields(clientsocket):
    data = clientsocket.recv(1024).decode()
    if not data:
        print("Connection closed")
        return True
    if data[0] == "Y":
        # Lose / Win
        print(data)
        return True
    else:
        heinzel.fill_field(data)
    return False


class CommandType(Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"

parser = OptionParser("heinzelClient.py [options] Start the Client and beat our opponent!")
parser.add_option("-i", "--ip-address", dest="IP",help="Address of the Server (default='localhost')")
parser.add_option("-p", "--port", dest="PORT", help="Port of the Server (default='5050')")
parser.add_option("-r", "--rows", dest="ROWS", help="rows of the map (default='10')")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
    try:
        option = parser.parse_args()

        """if option.ip_address:
            localhost = str(option.ip_address)
        else:
            localhost = "localhost"

        if option.port:
            port = int(option.port)
        else:
            port = 5050

        if option.rows is not None:
            row = option.rows
        else:
            row = 10"""
        row = 10
        localhost = 'localhost'
        port = 5050

        heinzel = HeinzelClient(row)
        # Verbindung herstellen (Gegenpart: accept() )
        clientsocket.connect((localhost, port))
        msg = heinzel.client_name  # input("Name?")
        # Nachricht schicken
        clientsocket.send(msg.encode())
        # Antwort empfangen
        data = clientsocket.recv(1024).decode()
        if not data or not data == "OK":
            # Schliessen, falls Verbindung geschlossen wurde
            clientsocket.close()
        else:
            while True:
                if rec_fields(clientsocket):
                    break
                while True:
                    heinzel.log()
                    msg = heinzel.make_movement()
                    time.sleep(0.01)
                    # Nachricht schicken
                    if msg.lower() == "up":
                        clientsocket.send(CommandType.UP.value.encode())
                        heinzel.move_up()
                        break
                    elif msg.lower() == "down":
                        clientsocket.send(CommandType.DOWN.value.encode())
                        heinzel.move_down()
                        break
                    elif msg.lower() == "left":
                        clientsocket.send(CommandType.LEFT.value.encode())
                        heinzel.move_left()
                        break
                    elif msg.lower() == "right":
                        clientsocket.send(CommandType.RIGHT.value.encode())
                        heinzel.move_right()
                        break
    except socket.error as serr:
        print("Socket error: " + serr.strerror)
