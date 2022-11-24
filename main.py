import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        rad = random.randint(10, 150)
        qp.setPen(QColor(255, 255, 0))
        x = random.randint(10, 500)
        y = random.randint(10, 500)
        qp.drawEllipse(x, y, 2 * rad, 2 * rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
