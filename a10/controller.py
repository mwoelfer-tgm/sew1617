from PySide.QtGui import *
from PySide.QtCore import *
import view
import model
from multiprocessing import Process,Value
import random
import time
import threading


class Controller(QWidget):
    def __init__(self):
        """
        Initializes object attributes, connects buttons and starts the refreshThread
        """
        QWidget.__init__(self)
        self.view = view.Ui_widget()
        self.view.setupUi(self)
        self.model = model.Model()
        self.view.new_point.clicked.connect(self.add_point)
        self.view.remove_point.clicked.connect(self.remove_point)
        rf = RefreshThread(self)
        rf.start()

    def paintEvent(self,event):
        """
        Gets called with every event that happens on the QWidget

        :param event: The event which occured, for example Mouse was hovered/clicked over button, update() was called

        :return: void
        """
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255,0,0))
        for point in self.model.points:
            qp.drawEllipse(point.x.value,point.y.value,10,10)
        qp.end()

    def add_point(self):
        """
        Gets called when the new_point button is clicked

        Creates a new Point-Process, starts it and adds it to the points list

        :return: void
        """
        p = Point(random.randint(0,500),random.randint(0,450))
        p.start()
        self.model.points.append(p)

    def remove_point(self):
        """
        Gets called when the remove_point button is clicked

        Removes the last point from list from the model
        :return:
        """
        if len(self.model.points) > 0:
            self.model.points.pop(len(self.model.points)-1)

#Thread solely for the purpose of updating the QWidget
#Can't be done with a process for some reason => Throws weird exceptions
class RefreshThread(threading.Thread):
    def __init__(self,c):
        """
        Initializes object attributes and calls super constructor

        :param c: Object of the controller
        """
        threading.Thread.__init__(self)
        self.c = c

    def run(self):
        """
        Updates the QWidget every tenth second
        :return: void
        """
        while True:
            time.sleep(0.01)
            self.c.update()
            QApplication.processEvents()


class Point(Process):
    def __init__(self,x,y):
        """
        Randomizes Direction and sets object attributes

        :param x: Randomized x position

        :param y: Randomizes y position
        """
        Process.__init__(self)
        self.x = Value("i",x)
        self.y = Value("i",y)
        self.dir_x = random.randint(0,1)
        self.dir_y = random.randint(0,1)
        self.speed_x = 1
        self.speed_y = 1
        self.model = model.Model()

    def run(self):
        """
        Adjusts the x and y value in a "infinite loop".
        :return:
        """
        while not self.model.closes:
            #If the x direction is 0, move the Point to the left
            if self.dir_x == 0:
                self.x.value -= self.speed_x
            #If the x direction is 1, move the Point to the right
            else:
                self.x.value += self.speed_x

            #If the y direction is 0, move the Point to the left
            if self.dir_y == 0:
                self.y.value -= self.speed_y
            #If the y direction is 1, move the Point to the right
            else:
                self.y.value += self.speed_y

            #If the Point moves out of the legitimate range, the speed gets reverted
            if self.x.value > 500 or self.x.value < 0:
                self.speed_x *= -1
            if self.y.value > 450 or self.y.value < 0:
                self.speed_y *= -1

            #Adjusts position of point every tenth second
            time.sleep(0.01)