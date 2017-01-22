import socket
from enum import Enum
import random
import time

map = [[0 for x in range(10)] for y in range(10)]
player_x = 0
player_y = 0
player_view = 0
first = True
zuege = 0
def rec_fields(data):
    if not data:
        print("Connection closed")
        return True

    if len(data) == 50:
        player_view = 5
    elif len(data) == 18:
        player_view = 3
    elif len(data) == 98:
        player_view = 7
    else:
        # Lose / Win
        print(data)
        return True



    # hilfe von Mladen Vojnovic
    startY = -int(player_view/2)
    dX = 0
    dY = 1
    for y in range(player_view):
        startX = -int(player_view/2)
        for x in range(player_view):
            if map[getPosY(startY)][getPosX(startX)] == 0:
                map[getPosY(startY)][getPosX(startX)] = data[dX*2:dY*2]
            startX += 1
            dX += 1
            dY += 1
        startY += 1
    print_map()
    return False

def getPosY(chY):
    newY = player_y + chY
    if newY < 0:
        return newY+10
    elif newY > 9:
        return newY-10
    return newY


def getPosX(chX):
    newX = player_x + chX
    if newX < 0:
        return newX+10
    elif newX > 9:
        return newX-10
    return newX

def print_map():
    for x in map:
        for y in x:
            if(y==0):
                print("0 ", end='')
            else:
                print(y,end='')
        print()

def getPlayer(data):
    if len(data) == 50:
        return data[24:26]
    elif len(data) == 18:
        return data[8:10]
    elif len(data) == 98:
        return data[48:50]

def getRight(data):
    if len(data) == 50:
        return data[26:28]
    elif len(data) == 18:
        return data[10:12]
    elif len(data) == 98:
        return data[50:52]

def getLeft(data):
    if len(data) == 50:
        return data[22:24]
    elif len(data) == 18:
        return data[6:8]
    elif len(data) == 98:
        return data[46:48]

def getDown(data):
    if len(data) == 50:
        return data[34:36]
    elif len(data) == 18:
        return data[14:16]
    elif len(data) == 98:
        return data[62:64]

def getUp(data):
    if len(data) == 50:
        return data[14:16]
    elif len(data) == 18:
        return data[2:4]
    elif len(data) == 98:
        return data[34:36]

class CommandType(Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"

def getPriority(field, cords):
    if field == "F ":
        return 0
    if field == "G ":
        return 1
    if field == "M ":
        return 2
    if field[1] == "B":
        return 3
    if field == "C " and not cords == [0,0]:
        return 3

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
    try:
        # Verbindung herstellen (Gegenpart: accept() )
        clientsocket.connect(('localhost', 5050))
        clientsocket.send("Player".encode())
        # Antwort empfangen
        data = clientsocket.recv(1024).decode()
        if not data or not data=="OK":
            # Schließen, falls Verbindung geschlossen wurde
            clientsocket.close()
        else:
            while True:
                data = clientsocket.recv(1024).decode()
                if rec_fields(data):
                    break
                while True:
                    #msg = input("UP/RIGHT/DOWN/LEFT?")

                    right_field = getRight(data)
                    if (player_x +1) > 9:
                        cords_right = [player_x-9,player_y]
                    else:
                        cords_right = [player_x+1,player_y]
                    left_field = getLeft(data)
                    if (player_x -1) < 0:
                        cords_left = [player_x+9,player_y]
                    else:
                        cords_left = [player_x-1,player_y]
                    up_field = getUp(data)
                    if (player_y -1) < 0:
                        cords_up = [player_x,player_y+9]
                    else:
                        cords_up = [player_x,player_y-1]
                    down_field = getDown(data)
                    if (player_y +1) > 9:
                        cords_down = [player_x,player_y-9]
                    else:
                        cords_down = [player_x,player_y+1]
                    player_field = getPlayer(data)
                    cords_player = [player_x,player_y]
                    r = random.choice(['up', 'right', 'left', 'down'])

                    # Nachricht schicken
                    try:
                        print("Player: ", player_field, cords_player)
                        print("Oben: ",up_field,cords_up)
                        print("Rechts: ",right_field,cords_right)
                        print("Unten: ",down_field,cords_down)
                        print("Links: ", left_field, cords_left)
                    except TypeError:
                        pass



                    print("Anzahl der Züge: " + str(zuege))
                    time.sleep(1)
                    msg = r
                    if msg.lower() == "up":
                        if up_field != "L ":
                            player_y -= 1
                            if player_y < 0:
                                player_y += 10
                            zuege += 1
                            clientsocket.send(CommandType.UP.value.encode())
                            break
                    elif msg.lower() == "down":
                        if down_field != "L ":
                            player_y += 1
                            if player_y > 9:
                                player_y -= 10
                            zuege += 1
                            clientsocket.send(CommandType.DOWN.value.encode())
                            break
                    elif msg.lower() == "left":
                        if left_field != "L ":
                            player_x -= 1
                            if player_x < 0:
                                player_x += 10
                            zuege += 1
                            clientsocket.send(CommandType.LEFT.value.encode())
                            break
                    elif msg.lower() == "right":
                        if right_field != "L ":
                            player_x += 1
                            if player_x > 9:
                                player_x -= 10
                            zuege+=1
                            clientsocket.send(CommandType.RIGHT.value.encode())
                            break
    except socket.error as serr:
        print("Socket error: " + serr.strerror)