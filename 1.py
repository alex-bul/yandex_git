import sys
import math

from form1 import Ui_Form
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor, QPolygonF


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None
        self.pushButton.clicked.connect(self.draw_circle)

    def draw_flag(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def createPoly(self, n, r, s):
        polygon = QPolygonF()
        w = 360 / n  # angle per step
        for i in range(n):  # add the points of polygon
            t = w * i + s
            x = r * math.cos(math.radians(t))
            y = r * math.sin(math.radians(t))
            polygon.append(QPointF(self.width() / 2 + x, self.height() / 2 + y))

        return polygon

    def draw(self, status):
        self.qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255), ))
        if status == 1:
            r = randint(10, 100)
            self.qp.drawEllipse(*[i - r * 0.5 for i in self.coords_], r, r)
        elif status == 2:
            size = randint(10, 100)
            self.qp.drawRect(*[i - size * 0.5 for i in self.coords_], size, size)
        elif status == 3:
            x, y = self.coords_
            y += 25
            rand_num = randint(0, 100)
            R = 15 - rand_num
            a = 13 + rand_num
            coords = ((x, y - 50), (x + a, y - R), (x - a, y - R))
            a = QPolygonF()
            for i in coords:
                a.append(QPointF(*i))
            self.qp.drawPolygon(a)

    def draw_circle(self, event):
        self.coords_ = [randint(0, self.width()), randint(0, self.height())]
        self.status = 1
        self.draw_flag()




app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
