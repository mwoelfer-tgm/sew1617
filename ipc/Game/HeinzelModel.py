from math import sqrt
from random import randint


class HeinzelClient:
    """
    Client for solving the IPC-Game
    as fast as possible (at least
    solve it successfully)


    :var posX: Position of the client on X-coordinates | horizontal
    :type int

    :var posY: Position of the client on Y-coordinates | vertical
    :type int

    :var field_length: length of the field
    :type int

    :var has_bomb: test, if the player stood on the bomb
    :type bool

    :var movement: direction, which the client will move at the end
    :type str

    :var battlefield: where the whole field will be safed
    :type list

    :var test_field: where the Lakes are marked
    :type list

    :var view_field: sight of the client in the moment
    :type list

    :var round_counter: counts the rounds
    :type int
    """

    posX = 0
    posY = 0
    has_bomb = False
    movement = "empty"
    round_counter = 0
    client_name = "PHeinzel_Client"
    view_field = []
    lake_counter = 0

    def __init__(self, field_length):
        """
        Constructor

        :param field_length: Length of the field
        :type field_length: int
        """

        self.field_length = field_length

        self.battlefield = self.create_map("U ", self.field_length)
        self.test_field = self.create_map("empty", self.field_length)

    def fill_field(self, data):
        """
        fills view_field (and recreate it)
        and battlefield with the data given

        :param data: the String of the seen field from the Server
        :type data: str
        """

        # ---- general ---- #
        length_v = int(sqrt(len(data) / 2))  # length of the sight
        self.view_field = self.create_map("U ", length_v)  # how far the client sees
        counter = 0  # data counter
        # ---- ------- ---- #

        # ---- battlefield ---- #
        fill_posY = int(length_v / 2)
        # ---- ----------- ---- #

        for i in range(0, length_v):

            # ---- battlefield ---- #
            y_print = self.corr_value(self.posY - fill_posY)
            fill_posY -= 1
            fill_posX = int(length_v / 2)
            # ---- ----------- ---- #

            for j in range(0, length_v):
                # ---- battlefield ---- #
                x_print = self.corr_value(self.posX - fill_posX)
                fill_posX -= 1
                # ---- ----------- ---- #

                # ---- prints ---- #
                self.battlefield[y_print][x_print] = data[counter:counter + 2]
                self.view_field[i][j] = data[counter:counter + 2]
                counter += 2
                # ---- ------ ---- #

    def corr_value(self, number):
        """
        Testing for the number given is not less then
        zero and not higher then the field_length
        otherwise it will be corrected as long as the number is out of range

        :param number: number to test
        :type number: int
        :return: number
        :rtype: int
        """

        if number < 0:
            number += self.field_length
        elif 0 <= number <= self.field_length - 1:
            number = number
        elif number > self.field_length - 1:
            number -= 10
        else:
            print("corr_value - Error - number: " + str(number))
        return number

    def make_movement(self):
        """
        the brain of the client

        :return: str based on the secure_lake function
        """
        y_in_list = 0
        x_in_list = 1
        y_x = []
        self.check_position()

        if self.see_enemy_castle():
            print("make_movement - see_enemy_castle")
            for coords in self.find_field_tile("C"):
                if coords[y_in_list] == 0 and coords[x_in_list] == 0:
                    pass
                else:
                    y_x = self.get_distance(coords[y_in_list], coords[x_in_list])
        elif self.see_bomb():
            print("make_movement - see_bomb")
            for coords in self.find_field_tile("B"):
                y_x = self.get_distance(coords[y_in_list], coords[x_in_list])
        elif self.see_mountain():
            print("make_movement - see_mountain")
            for coords in self.find_field_tile("M"):
                y_x = self.get_distance(coords[y_in_list], coords[x_in_list])
        else:
            print("make_movement - nothing True")
            for coords in self.find_field_tile("U"):
                y_x = self.get_distance(coords[y_in_list], coords[x_in_list])

        return self.secure_lake(y_x[y_in_list],y_x[x_in_list])

    def secure_lake(self, y, x):
        """
        tests if a lake is in the way

        :param y: distance between posY and the tile the client want to move to
        :type: int
        :param x: distance between posX and the tile the client want to move to
        :type: int
        :return: direction
        :rtype: str
        """
        #y_ram_important = 0
        #x_ram_important = 0
        #if y < 0:
        #    y_ram = (-y)
        #else:
        #    y_ram = y
        #if x < 0:
        #    x_ram = (-x)
        #else:
        #    x_ram = x
        #for var_y in range(0,y_ram):
        #    if self.battlefield[self.posY+y_ram_important][self.posX+x_ram_important][0] == "L":
        #        if x > 0:
        #            return "left"
        #        if x < 0:
        #            return "right"
        #    if y_ram_important > 0:
        #        y_ram_important -= 1
        #    else:
        #        y_ram_important += 1
        if self.lake_counter != 0:
            if self.lake_counter == 4:
                self.lake_counter -= 1
                if 0 > x < 0:
                    return "up"
                if 0 > y < 0:
                    return "left"
            elif self.lake_counter == 3 or self.lake_counter == 2:
                self.lake_counter -= 1
                if x < 0:
                    return "right"
                if x > 0:
                    return "left"
                if y < 0:
                    return "down"
                if y > 0:
                    return "up"
            elif self.lake_counter == 1:
                self.lake_counter -= 1
                if 0 > x < 0:
                    return "down"
                if 0 > y < 0:
                    return "right"

        if y < 0:
            if self.battlefield[self.corr_value(self.posY+1)][self.posX][0] == "L":
                if x < 0:
                    return "right"
                elif x > 0:
                    return "left"
                else:
                    print("overextend - gonna die")
                    self.lake_counter = 4
                    return self.secure_lake(y, x)
            return "down"
        elif y > 0:
            if self.battlefield[self.corr_value(self.posY-1)][self.posX][0] == "L":
                if x < 0:
                    return "right"
                elif x > 0:
                    return "left"
                else:
                    print("overextend - gonna die")
                    self.lake_counter = 4
                    return self.secure_lake(y, x)
            return "up"
        if x < 0:
            if self.battlefield[self.corr_value(self.posY)][self.posX+1][0] == "L":
                if y < 0:
                    return "down"
                elif y > 0:
                    return "up"
                else:
                    print("overextend - gonna die")
                    self.lake_counter = 4
                    return self.secure_lake(y, x)
            return "right"
        elif x > 0:
            if self.battlefield[self.corr_value(self.posY)][self.posX-1][0] == "L":
                if y < 0:
                    return "down"
                elif y > 0:
                    return "up"
                else:
                    print("overextend - gonna die")
                    self.lake_counter = 4
                    return self.secure_lake(y, x)
            return "left"
        print("secure_lake - error - KEINE AHNUNG!")
        return "right"

    def get_distance(self, y, x):
        """
        returns the distance of the tile

        :param y: the y coordinate of the tile
        :param x: the x coordinate of the tile
        :return: y and x distance
        :rtype: list
        """
        y_move = self.posY - y
        x_move = self.posX - x
        return [y_move, x_move]

    def get_neighbor(self):
        """
        creates a field, where the client is in the middle of it

        :return: the field
        :rtype: list
        """
        neighbor_field = self.create_map("U ", self.field_length)
        y_move = 4 - self.posY
        x_move = 4 - self.posX
        for y in range(0, self.field_length):
            for x in range(0, self.field_length):
                neighbor_field[y][x] = self.battlefield[self.corr_value(y + y_move)][self.corr_value(x + x_move)]
        return neighbor_field

    def find_field_tile(self, what_u_search_for):
        """
        returns all coordinates found
        of the specific tile

        :param what_u_search_for: the tile in the battlefield
        :type: str
        :return: all found coordinates
        :rtype: list
        """

        list_of_coordinates = []
        if what_u_search_for == "B":
            for y in range(0, self.field_length):
                for x in range(0, self.field_length):
                    if self.battlefield[y][x][1] == what_u_search_for:
                        list_of_coordinates.append([y, x])
        elif what_u_search_for == "M" \
                or what_u_search_for == "G" \
                or what_u_search_for == "F" \
                or what_u_search_for == "L" \
                or what_u_search_for == "C" \
                or what_u_search_for == "U":
            for y in range(0, self.field_length):
                for x in range(0, self.field_length):
                    if self.battlefield[y][x][0] == what_u_search_for:
                        list_of_coordinates.append([y, x])
        else:
            print("find_field_title() - Error - param: ", what_u_search_for)
        return list_of_coordinates

    def check_position(self):
        """
        checks the current position at following
        parameters:
            checks if the client stands on a mountain,
            if so the test_field on the position will
            be overwritten to "ascended"
            checks if the client stands on the bomb,
            if so the variable has_bomb will be
            changed to True
        """
        check_var = self.battlefield[self.posY][self.posX]
        if check_var[0] == "M":
            self.test_field[self.posY][self.posX] = "ascended"
        if check_var[1] == "B":
            self.has_bomb = True

    def see_enemy_castle(self):
        """
        tests if the enemy castle is seen
        and it's not his castle and has the bomb

        :return: True when castle is seen
        :rtype: bool
        """
        for y in range(0, self.field_length):
            for x in range(0, self.field_length):
                if self.battlefield[y][x] == "C " and y != 0 and x != 0 and self.has_bomb is True:
                    return True
        return False

    def see_bomb(self):
        """
        simple test if the bomb is spotted
        in the battlefield and not already
        collected then it will return true

        :return: True when Bomb is in battlefield
        :rtype: bool
        """
        for y in range(0, self.field_length):
            for x in range(0, self.field_length):
                if self.battlefield[y][x][1] == "B" and self.has_bomb is False:
                    return True
        return False

    def see_mountain(self):
        """
        simple test if a mountain is spotted
        in the battlefield and not already
        ascended, then it will return true

        :return: True when mountain is in battlefield
        :rtype: bool
        """
        for y in range(0, self.field_length):
            for x in range(0, self.field_length):
                if self.battlefield[y][x][0] == "M" and self.test_field[y][x] == "empty":
                    return True
        return False

    def move_up(self):
        """
        moves the posY upwards
        posY -= 1

        :return: direction
        :rtype: str
        """
        self.posY = self.corr_value(self.posY - 1)
        return "up"

    def move_down(self):
        """
        moves the posY downwards
        posY += 1

        :return: direction
        :rtype: str
        """
        self.posY = self.corr_value(self.posY + 1)
        return "down"

    def move_left(self):
        """
        moves the posX leftwards
        posX -= 1

        :return: direction
        :rtype: str
        """
        self.posX = self.corr_value(self.posX - 1)
        return "left"

    def move_right(self):
        """
        moves the posX rightwards
        posX += 1

        :return: direction
        :rtype: str
        """
        self.posX = self.corr_value(self.posX + 1)
        return "right"

    def log(self):
        """
        prints anything relevant in the console.
        """
        print("====================================================")
        print("Position: ", end="")
        print(self.posY, self.posX)
        print(" ")

        print("Battlefield: ")
        for i in range(0, self.field_length):
            print(self.battlefield[i])
        print(" ")

        print("Field of View: ")
        for j in range(0, len(self.view_field)):
            print(self.view_field[j])
        print(" ")

        print("has_bomb: ", self.has_bomb)
        print(" ")

        print("Round: ", self.round_counter)
        self.round_counter += 1
        print(" ")

    @staticmethod
    def create_map(input_map, width):
        """
        Creates a 2D-List filled and big as needed

        :param input_map: with what the "map" will be filled
        :param width: width of the map created

        :return: map
        :rtype: 2D List
        """
        return [[input_map for b in range(width)] for h in range(width)]

        # def get_client_name(self):
        #    """
        #    method to get the name of the client
        #    :return: self.client_name
        #    :rtype: str
        #    """
        #   #<bound method HeinzelClient.get_client_name
        #   #of <ipc.Heinzel_Client.HeinzelClient.HeinzelClient
        #   #object at 0x02DAA270>>
        #    return self.client_name
