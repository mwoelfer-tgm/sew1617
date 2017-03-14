import socket
from enum import Enum
import time
import random

xAxsis = []
yAxsis = []
map = []
posX = 0
posY = 0
lastMove = "up"


def getPosY(chY):
    """

    :param chY: the direction, -1 or 1
    :return: the new y coordinate
    """
    newY = posY + chY
    if newY < 0:
        return newY+10
    elif newY > 9:
        return newY-10
    return newY


def getPosX(chX):
    """

    :param chX: the direction, -1 or 1
    :return: the new x coordinate
    """
    newX = posX + chX
    if newX < 0:
        return newX+10
    elif newX > 9:
        return newX-10
    return newX


def rec_fields(clientsocket):
    data = clientsocket.recv(1024).decode()
    print("posX: "+str(posX)+"     posY: "+str(posY))
    if not data:
        print("Connection closed")
        return True
    if len(data) == 50:

        startY = -2
        dX = 0
        dY = 2

        for y in range(5):
            startX = -2
            for x in range(5):
                map[getPosY(startY)][getPosX(startX)] = data[dX:dY]
                startX += 1
                dX += 2
                dY += 2

            startY += 1


        #if map[posY][posX] == "0":
        #    map[posY][posX] = data[24:25]

        #print(data[0:10])
        #print(data[10:20])
        #print(data[20:30])
        #print(data[30:40])
        #print(data[40:50])

    elif len(data) == 18:

        startY = -1
        dX = 0
        dY = 2

        for y in range(3):
            startX = -1
            for x in range(3):
                map[getPosY(startY)][getPosX(startX)] = data[dX:dY]
                startX += 1
                dX += 2
                dY += 2

            startY += 1

        #In die map einfuegen
        #if map[posY][posX] == "0":
        #    map[posY][posX] = data[8:9]

        #print(data[0:6])
        #print(data[6:12])
        #print(data[12:18])
    elif len(data) == 98:

        startY = -3
        dX = 0
        dY = 2

        for y in range(7):
            startX = -3
            for x in range(7):
                map[getPosY(startY)][getPosX(startX)] = data[dX:dY]
                startX += 1
                dX += 2
                dY += 2

            startY += 1

        #if map[posY][posX] == "0":
        #    map[posY][posX] = data[48:49]

        #print(data[0:14])
        #print(data[14:28])
        #print(data[28:42])
        #print(data[42:56])
        #print(data[56:70])
        #print(data[70:84])
        #print(data[84:98])
    else:
        # Lose / Win
        print(data)
        return True
    print("y;x", end='')
    print(xAxsis)
    for i in range(10):
        print(str(i) + ": ", end='')
        print(map[i])
    return False

class CommandType(Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"



def getMove(lm, mode, priority):
    """

    :param lm: last Move
    :param mode: to now if ur searching for the bomb/castle or if you already know
    :param priority: to now if the x or y Axsis is more important
    :return: the command for the server
    """
    #print("getMove")

    #-------------------------------if you are seaarching for the target, moving in a diagonal direcgtion from bottom left to up right
    if mode[0] == "normal":
        #print("mode : normal")
        if lm == "up":
            #print("lm : up")
            if map[posY][getPosX(1)] == "L ":
                if map[getPosY(-1)][posX] == "L ":
                    if map[posY][getPosX(-1)] == "L ":
                        return "down"
                    else:
                        return "left"
                else:
                    return "up"
            else:

                return "right"

        elif lm == "right":
            #print("lm : right")
            if map[getPosY(-1)][posX] == "L ":
                if map[posY][getPosX(1)] == "L ":
                    if map[getPosY(1)][posX] == "L ":
                        return "left"
                    else:
                        return "down"
                else:
                    return "right"
            else:
                return "up"

        elif lm == "down":
            #print("lm : down")
            if map[posY][getPosX(1)] == "L ":
                if map[posY][getPosX(-1)] == "L ":
                    if map[getPosY(-1)][posX] == "L ":
                        return "up"
                    else:
                        return "down"
                else:
                    return "left"
            else:
                return "right"

        elif lm == "left":
            #print("lm : left")
            if map[getPosY(-1)][posX] == "L ":
                if map[getPosY(1)][posX] == "L ":
                    if map[posY][getPosX(-1)] == "L ":
                        return "right"
                    else:
                        return "left"
                else:
                    return "down"
            else:
                return "up"

    #------------------------------if you know the target, bomb/castle
    if mode[0] == "bomb":
        #print("bomb planted")

        #moms spaghetti for directions in x Axsis
        if mode[1] > posX:
            dirX = mode[1] - posX
            dirX2 = "right"
        elif mode[1] < posX:
            dirX = posX - mode[1]
            dirX2 = "left"
        else:
            dirX = 0
            dirX2 = "no"

        #moms spaghetti for dir in y Axsis
        if mode[2] > posY:
            dirY = mode[2] - posY
            dirY2 = "down"
        elif mode[2] < posY:
            dirY = posX - mode[2]
            dirY2 = "up"
        else:
            dirY = 0
            dirY2 = "no"

        if priority == "x":
            if dirX > 5:
                if dirX2 == "right":
                    if map[posY][getPosX(-1)] == "L ":
                        if dirY > 5:
                            if dirY2 == "up":
                                if map[getPosY(1)][posX] == "L ":
                                    return "up"
                                else:
                                    return "down"
                            else:
                                if map[getPosY(-1)][posX] == "L ":
                                    return "down"
                                else:
                                    return "up"
                        else:
                            if dirY2 == "up":
                                if map[getPosY(1)][posX] == "L ":
                                    return "down"
                                else:
                                    return "up"
                            else:
                                if map[getPosY(-1)][posX] == "L ":
                                    return "up"
                                else:
                                    return "down"
                    else:
                        return "left"
                else:
                    if map[posY][getPosX(1)] == "L ":
                        if dirY > 5:
                            if dirY2 == "up":
                                if map[getPosY(1)][posX] == "L ":
                                    return "up"
                                else:
                                    return "down"
                            else:
                                if map[getPosY(-1)][posX] == "L ":
                                    return "down"
                                else:
                                    return "up"
                        else:
                            if dirY2 == "up":
                                if map[getPosY(1)][posX] == "L ":
                                    return "down"
                                else:
                                    return "up"
                            else:
                                if map[getPosY(-1)][posX] == "L ":
                                    return "up"
                                else:
                                    return "down"
                    else:
                        return "right"

            else:
                if dirX2 == "left":
                    if map[posY][getPosX(-1)] == "L ":
                        if dirY > 5:
                            if dirY2 == "up":
                                if map[getPosY(1)][posX] == "L ":
                                    return "up"
                                else:
                                    return "down"
                            else:
                                if map[getPosY(-1)][posX] == "L ":
                                    return "down"
                                else:
                                    return "up"
                        else:
                            if dirY2 == "up":
                                if map[getPosY(1)][posX] == "L ":
                                    return "down"
                                else:
                                    return "up"
                            else:
                                if map[getPosY(-1)][posX] == "L ":
                                    return "up"
                                else:
                                    return "down"
                    else:
                        return "left"
                else:
                    if map[posY][getPosX(1)] == "L ":
                        if dirY > 5:
                            if dirY2 == "up":
                                if map[getPosY(1)][posX] == "L ":
                                    return "up"
                                else:
                                    return "down"
                            else:
                                if map[getPosY(-1)][posX] == "L ":
                                    return "down"
                                else:
                                    return "up"
                        else:
                            if dirY2 == "up":
                                if map[getPosY(1)][posX] == "L ":
                                    return "down"
                                else:
                                    return "up"
                            else:
                                if map[getPosY(-1)][posX] == "L ":
                                    return "up"
                                else:
                                    return "down"
                    else:
                        return "right"

        else:
            if dirY > 5:
                if dirY2 == "up":
                    if map[getPosY(1)][posX] == "L ":

                        ran = random.randint(0,1)
                        if ran == 0:
                            if map[posY][getPosX(1)] == "L ":
                                return "left"
                            else:
                                return "right"
                        else:
                            if map[posY][getPosX(-1)] == "L ":
                                return "right"
                            else:
                                return "left"


                    else:
                        return "down"
                else:
                    if map[getPosY(-1)][posX] == "L ":

                        ran = random.randint(0, 1)
                        if ran == 0:
                            if map[posY][getPosX(1)] == "L ":
                                return "left"
                            else:
                                return "right"
                        else:
                            if map[posY][getPosX(-1)] == "L ":
                                return "right"
                            else:
                                return "left"
                    else:
                        return "up"
            else:
                if dirY2 == "up":
                    if map[getPosY(-1)][posX] == "L ":

                        ran = random.randint(0, 1)
                        if ran == 0:
                            if map[posY][getPosX(1)] == "L ":
                                return "left"
                            else:
                                return "right"
                        else:
                            if map[posY][getPosX(-1)] == "L ":
                                return "right"
                            else:
                                return "left"
                    else:
                        return "up"

                else:
                    if map[getPosY(1)][posX] == "L ":

                        ran = random.randint(0, 1)
                        if ran == 0:
                            if map[posY][getPosX(1)] == "L ":
                                return "left"
                            else:
                                return "right"
                        else:
                            if map[posY][getPosX(-1)] == "L ":
                                return "right"
                            else:
                                return "left"
                    else:
                        return "down"






    #if mode[0] == "castle":
        #print("fire in the hole")



def check():
    """

    :return: search mode, and if it is with a castle, then also coordinates of the castle
    """
    #print("check")
    #if map[posY][posX] == "GB" or map[posY][posX] == "MB" or map[posY][posX] == "FB":
     #   for y in range(10):
     #       for x in range(10):
     #           if y != 0 or x != 0:
      #              if map[y][x] == "C " or map[y][x] == "C " or map[y][x] == "C ":
       #                 return "castle",x,y

    for y in range(10):
        for x in range(10):
            if map[y][x] == "GB" or map[y][x] == "MB" or map[y][x] == "FB":
                return "bomb",x,y

    return "normal",0,0


def checkForCastle():
    """

    :return: search mode, and if it is with a castle, then also coordinates of the castle
    """
    for y in range(10):
        for x in range(10):
            if y != 0 or x != 0:
                if map[y][x] == "C " or map[y][x] == "C " or map[y][x] == "C ":
                    return "bomb", x, y

    return "normal",0,0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
    try:
        # Verbindung herstellen (Gegenpart: accept() )
        port = input("Port eingeben:")
        clientsocket.connect(('localhost', int(port)))
        #init map
        for i in range(10):
            map.append([])
            for j in range(10):
                map[i].append("0 ")
        print(map)
        #init orientation
        xAxsis = ["0:","1:","2:","3:","4:","5:","6:","7:","8:","9:"]

        msg = "mvojnovic_client.py"
        # Nachricht schicken
        clientsocket.send(msg.encode())
        # Antwort empfangen
        data = clientsocket.recv(1024).decode()
        if not data or not data=="OK":
            # Schließen, falls Verbindung geschlossen wurde
            clientsocket.close()
        else:
            lastMove = "up"
            zielX = 10
            zielY = 10
            round = 0
            status = "search bomb"
            priority = "x"
            while True:

                if rec_fields(clientsocket):
                    break
                while True:
                    time.sleep(1)
                    if priority == "y":
                        priority = "x"
                    else:
                        priority = "y"
                    if zielX == posX and zielY == posY:
                        priority = "x"
                        status = "search castle"


                    if status == "search bomb":
                        c = check()
                    else:
                        c = checkForCastle()

                    zielX = c[1]
                    zielY = c[2]

                    if zielX == posX:
                        priority = "y"

                    if zielY == posY:
                        priority = "x"

                    msg = getMove(lastMove, c, priority)
                    lastMove = msg
                    print(round)
                    round += 1
                    #print("bout to send")

                    #pause = input("PAUSE")
                    # Nachricht schicken
                    if msg.lower() == "up":
                        posY -= 1
                        if posY == -1:
                            posY = 9

                        clientsocket.send(CommandType.UP.value.encode())
                        break
                    elif msg.lower() == "down":
                        posY += 1
                        if posY == 10:
                            posY = 0

                        clientsocket.send(CommandType.DOWN.value.encode())
                        break
                    elif msg.lower() == "left":
                        posX -= 1
                        if posX == -1:
                            posX = 9

                        clientsocket.send(CommandType.LEFT.value.encode())
                        break
                    elif msg.lower() == "right":
                        posX += 1
                        if posX == 10:
                            posX = 0

                        clientsocket.send(CommandType.RIGHT.value.encode())
                        break
    except socket.error as serr:
        print("Socket error: " + serr.strerror)

