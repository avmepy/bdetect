import math
import random
import time

class Window:
    """ class implementing the window (emulator) """

    def __init__(self):
        """
        constructor
        :param dot: top left window
        :param h: window height
        :param w: window width
        """

        #r = Region("""get your image here""")
        r = Region(Region(6,33,1264,615))

        self.dot = (r.x, r.y)
        self.h = r.w
        self.w = r.h
        self.center = (self.dot[0] + int(r.w/2), self.dot[1] + int(r.h/2))

        # angle between window diagonal and x axis
        self.angle = math.atan((self.dot[0] + self.w) / (self.dot[1] + self.h))

    def shape(self):
        """
        :return: the four point tuple (defining window)
        """
        return self.dot, (self.dot[0] + self.w, self.dot[1]), (self.dot[0] + self.w, self.dot[1] + self.h),\
               (self.dot[0], self.dot[1] + self.h)


class Runner:
    """ character class """
    def __init__(self, window):
        """
        constructor
        :param window: emulator window
        """
        self.start = (0, 0)
        self.current = (0, 0)
        self.window = window

    def go(self, location, needGo = False):
        """
        character move
        :param location: destination coordinates
        :return: None
        """
        x, y = location  # in absolute display coordinates
        # in emulator window coordinates
        tmp_x = x - self.window.dot[0]
        tmp_y = y - self.window.dot[1]

        # in character coordinates
        new_x = tmp_x - self.window.center[0]
        new_y = tmp_y - self.window.center[1]

        self.current = (new_x, new_y)

        if needGo:
            click(Location(*location))

    def _get_random_angle(self, deviation=5):
        """
        :param deviation: deviation
        :return: random angle
        """
        pass

    def _get_random_length(self):
        """
        :return: random length
        """
        diagonal = math.sqrt((self.window.dot[0] + self.window.w)**2 + (self.window.dot[1] + self.window.h)**2)
        max_len = int(diagonal / 2)
        return rd.randrange(5, max_len - 10)

    def anotherWay(self):
        """
        alternate move
        used when there are no items or character in a dead end
        :return: None
        """
        z = Runner._get_random_length(self)  # diagonal
        len_x = z * math.cos(self.window.angle)
        len_y = z * math.sin(self.window.angle)
        new_x = abs(self.current[0] - len_x)
        new_y = abs(self.current[1] - len_y)

        # in emulator window
        x_for_click = new_x - self.window.center[0]
        y_for_click = new_y - self.window.center[1]

        # in absolute coordinates
        x_for_click -= self.window.dot[0]
        y_for_click -= self.window.dot[1]

        y_for_click = int(y_for_click)+start.getY()
        x_for_click = int(x_for_click)+start.getX()

        print(x_for_click,y_for_click)

        self.go((x_for_click, y_for_click), True)


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


if __name__ == '__main__':
    player = Runner()
    while True:
        btc = findAll("BTC.png")

        dragon = findAll("DRAGON.png")

        btc += dragon

        btc.sort(key=lambda x: distance(*Runner.cur, x.getX(), x.getY())
        if btc:
            player.go((btc[0].getX(), btc[0].getY()), True)
        else:
            player.anotherWay()