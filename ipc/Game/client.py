import socket
from enum import Enum
import random
import math
import time
from collections import defaultdict,  deque
import argparse


# commandtype Enum for decididing direction
class CommandType(Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"


class Graph:
    """
    Graph class with represent a graph object. A graph is needed in order for the dijkstra algorithm to work correctly
    In a graph, a node is a field, which is connected to other fields. Those connections are colled edges.
    In this case, each field is a tile and is connected to the other sourrounding fields via 4 edges.
    Adding to that, each edge has its own distance, this can be imagined as the 'cost' which is needed to travel along that edge.
    For example, a mountain is more expensive to travel to than a forest field

    Src code from: https://gist.github.com/mdsrosa/c71339cb23bc51e711d8
    """
    def __init__(self):
        """
        Initialize the Graph object
        """
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        """
        Add a node to the graph object

        :param value: the node to be added

        :return: None
        """
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        """
        Add an edge to the graph object - A 'connection'

        :param from_node: The node from which the edge sources from

        :param to_node: The node which is targetet by the source

        :param distance: How far apart those nodes are - The 'price' - How expensive it is

        :return: None
        """
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph, initial):
    """
    The infamous Dijsktra algorithm

    :param graph: graph object which represents the map in such a form that the dijkstra algorithm can process it

    :param initial: The initial node from which every edge gets returned

    :return: The path which was already visited and the actual path

    Src code from https://gist.github.com/mdsrosa/c71339cb23bc51e711d8
    """
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def shortest_path(graph, origin, destination):
    """
    'Uses' the output of the dijstkra function to get the shortets path of two points

    :param graph: Graph object which represents the map

    :param origin: From where the path sources from

    :param destination: Destination of the path

    :return: A List of how many were already visited and the actual path

    Src code from https://gist.github.com/mdsrosa/c71339cb23bc51e711d8
    """
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

# client which connects to servera nd sends and receives data
class Client:
    def __init__(self, ip_address, port, map_size, time):
        """
        initialize member variables

        :param ip_address: ip-address which the client connects to (default='localhost')

        :param port: port which the client connects to (default=5050)

        :param map_size: size of the map, always square! (default=10)

        :param time: time the client takes in between each turn, in seconds (default=1)
        """
        self.ip_address = ip_address
        self.port = port
        self.map_size = map_size
        self.time = time
        self.cords_player = [0,0]
        self.turns = 0
        self.has_bomb = False
        self.map = [[0 for x in range(self.map_size)] for y in range(self.map_size)]
        self.curr_path = []
        self.mode = 0
        self.i = 0
        self.j = 0
        self.target = []
        self.visited = []

    def update_map(self, data):
        """
        update the intern map with the data received from the server

        :param data: data which was sent from the server, 'what the client sees'
        """

        # because you see different depending on the field you're standing, the amount of rows have to be calculated
        # i.e. when you're standing on a forest, you'll have 3 rows, on gras you'll have 5 rows and on mountains you'll see 7 rows
        rows = int(math.sqrt((len(data)/2)))

        # this algorithm updates the map, help from Mladen Vojnovic

        # define start cords
        cords_start = [0,0]
        # set x-coord of start-coords
        cords_start[1] = -int(rows / 2)
        # because data always saves each field with 2 characters, we need 2 variables to correctly iterate through whole data
        i = 0
        j = 1
        for y in range(rows):
            # set y-coord of start-coords
            cords_start[0] = -int(rows / 2)
            for x in range(rows):
                # check if the map wasn't already updated on said position
                if self.map[self.get_pos_y(cords_start[1])][self.get_pos_x(cords_start[0])] == 0:
                    # set position of map to position of data
                    self.map[self.get_pos_y(cords_start[1])][self.get_pos_x(cords_start[0])] = data[i * 2:j * 2]
                # increment x-coord of start-coords
                cords_start[0] += 1
                # increment iterate variables
                i += 1
                j += 1
            # increment y-coord of start-coords
            cords_start[1] += 1

    def get_graph(self):
        """
        With the information of the intern map create a Graph object and fill it with the information
        :return: a graph object filled with the nodes and edges of the intern map
        """
        # create a new graph object to represent the map in a way so that the dijsktra alogirithm can be applied
        g = Graph()
        # iterate trough the map
        for y in range(self.map_size):
            for x in range(self.map_size):
                # only put fields in the graph that were already seen
                if self.map[y][x] != 0:
                    # add the field to the graph as a node => 'Knotenpunkt' => basically just a field in the graph
                    g.add_node(str([y,x]))
                    # iterate through neighbours
                    for neighbour in self.around_pos([y,x]):
                        # only go through neighbours whose field is known
                        if self.field_at(neighbour) != 0:
                            # the distance is how much it 'costs' to go to a certain field
                            # for example, it is more 'expensive' to go on a mountain than it'd be to go on a grass field
                            distance = 1
                            if self.field_at(neighbour) == 'L ':
                                distance = 10000
                            if self.field_at(neighbour) == 'M ':
                                distance = 2
                            # add the edge => 'Verbindung' => basically how 2 nodes are connected together, and how expensive it is to go there
                            g.add_edge(str([y,x]), str(neighbour), distance)
        return g

    def get_pos_y(self,ch_y):
        """
        :param ch_y: y coordinate to be checked

        :return: y coordinate of player added with y coordinate of parameter guaranteed in interval [0 - map_size]
        """
        newY = self.cords_player[0] + ch_y
        if newY < 0:
            return newY + self.map_size
        elif newY > (self.map_size - 1):
            return newY - self.map_size
        return newY

    def get_pos_x(self,ch_y):
        """
        :param ch_x: x coordinate to be checked

        :return: x coordinate of player added with x coordinate of parameter guaranteed in interval [0 - map_size]
        """
        newX = self.cords_player[1] + ch_y
        if newX < 0:
            return newX + self.map_size
        elif newX > (self.map_size - 1):
            return newX - self.map_size
        return newX

    def print_map(self):
        """
        represents the internal map with borders and coordinate system
        """
        y_number = 0

        # print upper numbers
        print("    ", end='')
        for i in range(self.map_size):
            if i < 10:
                print(str(i) + "  ", end='')
            else:
                print(str(i) + " ", end='')
        print()
        # print upper border
        print("   ", end='')
        for i in range(self.map_size):
            print("---", end='')
        print()
        for y in self.map:
            # print left border and number
            if y_number < 10:
                print(str(y_number) + " | ", end='')
            else:
                print(str(y_number) + "| ", end='')
            # print actual map
            for x in y:
                if x == 0:
                    print("0  ", end='')
                else:
                    print(str(x) + " ", end='')
            print()
            y_number += 1

    def get_priority(self, field, cords):
        """
        gets the priority of a certain field on a certain cord

        :param field: string representation of a field

        :param cords: the cords the field is on

        :return: priority of the field
        """
        # if forest => low priority
        if field == "F ":
            return 1
        # if gras => medium priority
        elif field == "G ":
            return 2
        # if mountain => higher porioty
        elif field == "M " and cords not in self.visited:
            return 3
        # if bomb and bomb wasn't already picked up => highest priority
        elif field[1] == "B" and not self.has_bomb:
            return 4
        # if bomb and bomb was already picked up => lowest priority
        elif field[1] == "B" and self.has_bomb:
            return 0
        # if castle and not own castle (own castle is always on [0,0]) and bomb was already picked up => highest priority
        elif field == "C " and not cords == [0, 0] and self.has_bomb == True:
            return 4
        # if castle and not own castle but bomb not picked up => lowest priority
        elif field == "C " and cords == [0, 0]:
            return 0
        # any other cases => lowest priority
        else:
            return 0

    def field_at(self, pos):
        """
        :param pos: position in [y,x] list

        :return: string representation of field on the intern map
        """
        y = pos[0]
        x = pos[1]
        return self.map[y][x]

    def around_pos(self, pos):
        """
        gets the positions around a certain field guaranteed in a [0 - map_size] interval

        :param pos: position of field to be searched in [y,x] list

        :return: list of fields around pos
        """
        if (pos[0] + 1) > (self.map_size - 1):
            down = [pos[0] - (self.map_size - 1), pos[1]]
        else:
            down = [pos[0] + 1, pos[1]]

        if (pos[0] - 1) < 0:
            up = [pos[0] + (self.map_size - 1), pos[1]]
        else:
            up = [pos[0] - 1, pos[1]]

        if (pos[1] - 1) < 0:
            left = [pos[0], pos[1] + (self.map_size - 1)]
        else:
            left = [pos[0], pos[1] - 1]

        if (pos[1] + 1) > (self.map_size - 1):
            right = [pos[0], pos[1] - (self.map_size - 1)]
        else:
            right = [pos[0], pos[1] + 1]
        return [up, right, down, left]


    def get_directions(self,path):
        """
        :param path: A path of fields which are to be visited

        :return: A list of directions instead of the direct fields, helps enormously when developing the logic
        """
        # the direciton list which is to be filled
        dirs = []

        # iterate through the path
        for i in range(1,len(path)):
            # get the direction between the src and target field
            src = [int(path[i-1][1]),int(path[i-1][4])]
            targ = [int(path[i][1]),int(path[i][4])]

            # this works because in the path each distance is always either 1, -1 in x or 1,-1 in y... edge cases are when it goes 'above' the map_size, which also gets checked
            if ((targ[1]-src[1]) == 1) or ((targ[1]-src[1]) == -(self.map_size-1)):
                dirs.append('right')
            elif ((targ[1]-src[1]) == -1) or ((targ[1]-src[1]) == self.map_size-1):
                dirs.append('left')
            elif ((targ[0]-src[0]) == 1) or ((targ[0]-src[0]) == -(self.map_size-1)):
                dirs.append('down')
            elif ((targ[0]-src[0]) == -1) or ((targ[0]-src[0]) == self.map_size-1):
                dirs.append('up')
        return dirs


    def start(self):
        """
        main method of the client

        connects to the server, and automatically creates data to be sent to server

        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            try:
                # Verbindung herstellen (Gegenpart: accept() )
                clientsocket.connect((self.ip_address, self.port))
                clientsocket.send("mwoelfer01".encode())
                # Antwort empfangen
                data = clientsocket.recv(1024).decode()
                if not data or not data == "OK":
                    # Schließen, falls Verbindung geschlossen wurde
                    clientsocket.close()
                else:
                    while True:
                        # receive the data
                        data = clientsocket.recv(1024).decode()

                        # if there is some kind of error, close the connection
                        if not data:
                            print("Connection closed")
                            break

                        # if the reply wasn't info on how much the player sees, it has to be losing/winning message
                        if len(data) != 18 and len(data) != 50 and len(data) != 98:
                            print(data)
                            return True

                        # take current view and update intern map with it
                        self.update_map(data)
                        # print the intern map
                        self.print_map()
                        while True:
                            # get the string representation of the field the player stands on
                            player_field = self.field_at(self.cords_player)

                            # get cords and field type of each field that the player is being surrounded by
                            cords_up = self.around_pos(self.cords_player)[0]
                            up_field = self.field_at(cords_up)

                            cords_right = self.around_pos(self.cords_player)[1]
                            right_field = self.field_at(cords_right)

                            cords_down = self.around_pos(self.cords_player)[2]
                            down_field = self.field_at(cords_down)

                            cords_left = self.around_pos(self.cords_player)[3]
                            left_field = self.field_at(cords_left)

                            # print out basic information for debugging
                            print("Player: " + str(self.cords_player))
                            print("Hat Bombe: " + str(self.has_bomb))

                            # if the player stands on the bomb, set the class attribute to True
                            if player_field[1] == "B":
                                self.has_bomb = True

                            # the msg which is then to be sent to the server
                            msg = ""
                            if self.mode == 0:
                                # mode 0 means that nothing important was found yet and mountains / bombs / castles are being searched
                                for y in range(len(self.map)):
                                    for x in range(len(self.map)):
                                        if self.map[y][x] != 0:
                                            if self.get_priority(self.map[y][x], [y, x]) == 4:
                                                self.mode = 1
                                                self.curr_path = self.get_directions(shortest_path(self.get_graph(),str(self.cords_player),str([y,x]))[1])
                                                self.target = [y,x]
                                            elif self.get_priority(self.map[y][x],[y,x]) == 3:
                                                self.mode = 2
                                                if self.cords_player != [y,x]:
                                                    self.curr_path = self.get_directions(shortest_path(self.get_graph(), str(self.cords_player),str([y, x]))[1])
                                                    self.target = [y,x]
                                            else:
                                                if self.i % 2 == 0:
                                                    msg = 'right'
                                                else:
                                                    msg = 'down'

                            if self.mode == 2:
                                # mode 2 means that a mountain was found, but if a priority 4 thing (bomb/castle) gets seen the target is immediately switched
                                for y in range(len(self.map)):
                                    for x in range(len(self.map)):
                                        if self.map[y][x] != 0:
                                            if self.get_priority(self.map[y][x], [y, x]) == 4:
                                                self.mode = 1
                                                self.j = 0
                                                self.curr_path = self.get_directions(shortest_path(self.get_graph(),str(self.cords_player),str([y,x]))[1])
                                if self.mode != 1:
                                    if self.j == len(self.curr_path):
                                        self.visited.append(self.target)
                                        self.mode = 0
                                        self.j = 0
                                    else:
                                        msg = self.curr_path[self.j]
                                        self.j += 1
                            if self.mode == 1:
                                # if mode 1 is entered, it means that something important was found with a set path
                                if self.j == len(self.curr_path):
                                    self.mode = 0
                                    self.j = 0
                                else:
                                    print("Remaining Path: " + str(self.curr_path[self.j:]))
                                    msg = self.curr_path[self.j]
                                    self.j += 1

                            self.i+=1
                            #msg = random.choice(['right','left','up','down'])

                            # print out the amount turns that were taken that game
                            print("Anzahl der Züge: " + str(self.turns))
                            # sleep the amount that specified when starting the client
                            time.sleep(self.time)
                            # if the choice was up
                            if msg.lower() == "up":
                                # if the desired field was a lake, chose another field
                                if up_field != "L ":
                                    # make sure player cords only go from [0 - map_size]
                                    self.cords_player[0] -= 1
                                    if self.cords_player[0] < 0:
                                        self.cords_player[0] += self.map_size
                                        self.turns += 1
                                    clientsocket.send(CommandType.UP.value.encode())
                                    break
                            # if the choice was down
                            elif msg.lower() == "down":
                                if down_field != "L ":
                                    # make sure player cords only go from [0 - map_size]
                                    self.cords_player[0] += 1
                                    if self.cords_player[0] > (self.map_size - 1):
                                        self.cords_player[0] -= self.map_size
                                    self.turns += 1
                                    clientsocket.send(CommandType.DOWN.value.encode())
                                    break
                            # if the choice was left
                            elif msg.lower() == "left":
                                if left_field != "L ":
                                    self.cords_player[1] -= 1
                                    if self.cords_player[1] < 0:
                                        self.cords_player[1] += self.map_size
                                    self.turns += 1
                                    clientsocket.send(CommandType.LEFT.value.encode())
                                    break
                            # if the choice was right
                            elif msg.lower() == "right":
                                if right_field != "L ":
                                    self.cords_player[1] += 1
                                    if self.cords_player[1] > (self.map_size - 1):
                                        self.cords_player[1] -= self.map_size
                                    self.turns += 1
                                    clientsocket.send(CommandType.RIGHT.value.encode())
                                    break
            except socket.error as serr:
                print("Socket error: " + serr.strerror)

if __name__ == '__main__':
    # initialize Argumentparser with fitting description
    parser = argparse.ArgumentParser(description='Client solves the puzzle game on its own')
    # add arguments
    parser.add_argument("-i","--ip-address",help="Address of the server (default='localhost')",default="localhost")
    parser.add_argument("-p","--port",help="Port of the server (default='5050')",default=5050,type=int)
    parser.add_argument("-r","--rows",help="rows of the server map(square) (default='10')",default=10,type=int)
    parser.add_argument("-t","--time",help="time between each turn (default=0.01",default=0.01,type=float)
    # parse arguments
    args = parser.parse_args()
    # initialize client with parameters
    c = Client(args.ip_address, args.port, args.rows, args.time)
    # start the client
    c.start()