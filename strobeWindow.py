from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

class strobeWindow(QWidget):
    """ inherits QWidget, that allows for drawing the strobes. """
    def __init__(self, parent):
        super().__init__(parent)
        self.x1 = 0.0
        self.x2 = 0.0
        self.x3 = 0.0

    def paintEvent(self, event):
        w = self.width()
        h = self.height()
        y1 = int(0.5 * h // 10)
        y2 = int(3.5 * h // 10)
        y3 = int(6.5 * h // 10)
        painter = QPainter(self)
        painter.begin(self)
        # strobe for fundamental
        if self.x1 < 0.5:
            painter.fillRect(int(w*self.x1), y1, w//2, 3*h//10, QColor('blue'))
        else:
            painter.fillRect(0, y1,int((self.x1-0.5)*w), 3*h//10, QColor('blue'))
            painter.fillRect(int(self.x1*w), y1, int((1-self.x1)*w), 3*h//10, QColor('blue'))
        # strobe for second harmonic
        painter.fillRect(int(self.x2*w), y2, w//4, 3*h//10, QColor('blue'))
        if self.x2 < 0.25:
            painter.fillRect(int((self.x2+0.5)*w), y2, w//4, 3*h//10, QColor('blue'))
        else:
            painter.fillRect(0, y2, int((self.x2 - 0.25)*w), 3*h//10, QColor('blue'))
            painter.fillRect(int((self.x2+0.5)*w), y2, int((0.5-self.x2)*w), 3*h//10, QColor('blue'))
        # strobe for third harmonic
        painter.fillRect(int(w*self.x3), y3, w//8, 3*h//10, QColor('blue'))
        painter.fillRect(int(w*(self.x3+0.25)), y3, w//8, 3*h//10, QColor('blue'))
        painter.fillRect(int(w*(self.x3+0.5)), y3, w//8, 3*h//10, QColor('blue'))
        if self.x3 < 0.125:
            painter.fillRect(int((self.x3+0.75)*w), y3, w//8, 3*h//10, QColor('blue'))
        else:
            painter.fillRect(0, y3, int((self.x3 - 0.125)*w), 3*h//10, QColor('blue'))
            painter.fillRect(int((self.x3+0.75)*w), y3, int((0.25-self.x3) * w), 3 * h // 10, QColor('blue'))

        painter.end()

    def refresh(self, y1, y2, y3):
        self.x1 += y1
        self.x1 %= 1.0
        self.x2 += y2
        self.x2 %= 0.5
        self.x3 += y3
        self.x3 %= 0.25
        self.update()
