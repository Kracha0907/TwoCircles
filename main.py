import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.btnDraw.clicked.connect(self.paint)

    def paintEvent(self, event):
        print(self.do_paint)
        if self.do_paint:
            pixmap = QPixmap(self.label.size())
            pixmap.fill(Qt.transparent)
            qp = QPainter()
            qp.begin(pixmap)
            self.draw_circles(qp)
            qp.end()
            self.label.setPixmap(pixmap)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circles(self, qp):
        r1 = random.randint(1, 125)
        r2 = random.randint(1, 125)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(QPoint(125, 200), r1, r1)
        qp.drawEllipse(QPoint(375, 200), r2, r2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())