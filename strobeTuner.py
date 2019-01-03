import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, pyqtSignal
import numpy as np
from mainWindowUi import Ui_mainWindow
from temperaments import temperaments, noteNames
from listen import Listen


class Window(QWidget):
    # signal to be emitted when changing temperament : note names list and corresponding frequencies list
    sigChangeTemp = pyqtSignal([list, list])
    # signal to be emitted when changing the note to listen to :
    sigChangeNote = pyqtSignal([float])

    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.temperamentComboBox.addItems(sorted(temperaments.keys()))
        self.ui.temperamentComboBox.setCurrentIndex(1)
        self.ui.temperamentComboBox.currentTextChanged.connect(self.setTemp)
        self.ui.temperamentComboBox.installEventFilter(self)
        self.currentNote=69
        self.automatic = False
        self.thread = Listen()
        self.show()
        self.thread.sig.connect(self.refresh)
        self.sigChangeNote.connect(self.thread.setFreq)
        self.sigChangeTemp.connect(self.thread.setAutomatic)
        self.ui.automaticCheckbox.stateChanged.connect(self.setAutomatic)
        self.setPitch(440.0)
        self.thread.start()

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        else:
            return False

    def keyPressEvent(self, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Left:
                self.currentNote -= 1
                if self.currentNote < 12:  # not tested for so low frequencies but...
                    self.currentNote = 12
                self.ui.noteLabel.setText(noteNames[self.currentNote])
                if self.automatic:
                    self.automatic = False
                self.ui.automaticCheckbox.setCheckState(False)
                self.sigChangeNote.emit(self.frequencies[self.currentNote])

            if event.key() == QtCore.Qt.Key_Right:
                self.currentNote += 1
                if self.currentNote > 100:  # a quite arbitrary limit
                    self.currentNote = 100

                self.ui.noteLabel.setText(noteNames[self.currentNote])
                if self.automatic:
                    self.automatic = False
                self.ui.automaticCheckbox.setCheckState(False)
                self.sigChangeNote.emit(self.frequencies[self.currentNote])

            if event.key() == QtCore.Qt.Key_Up:
                self.setPitch(self.pitch + 1)

            if event.key() == QtCore.Qt.Key_Down:
                self.setPitch(self.pitch - 1)

    @QtCore.pyqtSlot(str)
    def setTemp(self, temp):
        self.setPitch(self.pitch)

    @QtCore.pyqtSlot(float, float, float, str)
    def refresh(self, x1, x2, x3, noteName):
        if noteName:
            self.ui.noteLabel.setText(noteName)
        self.ui.strobeWidget.refresh(x1, x2, x3)

    def setAutomatic(self, state):
        self.automatic = state
        self.setPitch(self.pitch)

    def setPitch(self, pitch):
        if pitch > 530 :
            pitch = 530 # seems high enough to me...
        if pitch < 385:
            pitch = 385
        self.pitch = pitch
        self.ui.pitchLabel.setText(str(pitch))
        self.ui.pitchLabel.update()
        temp = self.ui.temperamentComboBox.currentText()
        self.frequencies = np.array(temperaments[temp])*self.pitch / 440.0
        if self.automatic:
            self.sigChangeTemp.emit(noteNames[24:88], list(self.frequencies[24:88]))
        else:
            self.sigChangeNote.emit(self.frequencies[self.currentNote])


app = QApplication(sys.argv)
aWindow = Window()
sys.exit(app.exec_())

