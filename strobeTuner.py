import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QKeyEvent
import numpy as np
from mainWindowUi import Ui_Form
from temperaments import temperaments, noteNames
from listen import Listen

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.noteComboBox.addItems(noteNames)
        self.ui.noteComboBox.setCurrentIndex(69)
        self.ui.temperamentComboBox.addItems(temperaments.keys())
        self.ui.temperamentComboBox.setCurrentIndex(0)
        self.ui.temperamentComboBox.currentTextChanged.connect(self.setTemp)
        self.ui.noteComboBox.currentIndexChanged.connect(self.setNote)
        self.ui.noteComboBox.installEventFilter(self)
        self.ui.temperamentComboBox.installEventFilter(self)
        self.currentNote=69
        self.thread = Listen()
        self.setPitch(440.0)
        self.show()
        self.thread.sig.connect(self.ui.strobeWidget.refresh)
        self.thread.start()

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Left:
                self.currentNote -= 1
                if self.currentNote < 12:  # not tested for so low frequencies but...
                    self.currentNote = 12

                self.ui.noteComboBox.setCurrentIndex(self.currentNote)
                self.ui.noteComboBox.update()
                self.thread.freq = self.frequencies[self.currentNote]

            if event.key() == QtCore.Qt.Key_Right:
                self.currentNote += 1
                if self.currentNote > 100:  # a quite arbitrary limit
                    self.currentNote = 100

                self.ui.noteComboBox.setCurrentIndex(self.currentNote)
                self.ui.noteComboBox.update()
                self.thread.freq = self.frequencies[self.currentNote]

            if event.key() == QtCore.Qt.Key_Up:
                self.setPitch(self.pitch + 1)

            if event.key() == QtCore.Qt.Key_Down:
                self.setPitch(self.pitch - 1)

            return True
        else:
            return False


    @QtCore.pyqtSlot(str)
    def setTemp(self, temp):
        self.setPitch(self.pitch)

    @QtCore.pyqtSlot(int)
    def setNote(self, note):
        self.currentNote = note
        self.thread.freq = self.frequencies[self.currentNote]
        
    def setPitch(self, pitch):
        if pitch > 530 :
            pitch = 530 # seems high enough to me...
        if pitch < 385:
            pitch = 385
        self.pitch = pitch
        self.ui.label.setText(str(pitch))
        self.ui.label.update()
        temp = self.ui.temperamentComboBox.currentText()
        self.frequencies = np.array(temperaments[temp])*self.pitch / 440.0
        self.thread.freq = self.frequencies[self.currentNote]



app = QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())

