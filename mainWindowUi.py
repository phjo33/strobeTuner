# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(631, 373)
        self.gridLayout = QtWidgets.QGridLayout(mainWindow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.temperamentComboBox = QtWidgets.QComboBox(mainWindow)
        self.temperamentComboBox.setObjectName("temperamentComboBox")
        self.gridLayout.addWidget(self.temperamentComboBox, 1, 2, 1, 1)
        self.pitchLabel = QtWidgets.QLabel(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pitchLabel.setFont(font)
        self.pitchLabel.setObjectName("pitchLabel")
        self.gridLayout.addWidget(self.pitchLabel, 1, 6, 1, 1)
        self.automaticCheckbox = QtWidgets.QCheckBox(mainWindow)
        self.automaticCheckbox.setObjectName("automaticCheckbox")
        self.gridLayout.addWidget(self.automaticCheckbox, 1, 0, 1, 1)
        self.noteLabel = QtWidgets.QLabel(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.noteLabel.setFont(font)
        self.noteLabel.setObjectName("noteLabel")
        self.gridLayout.addWidget(self.noteLabel, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.strobeWidget = strobeWindow(mainWindow)
        self.strobeWidget.setObjectName("strobeWidget")
        self.gridLayout.addWidget(self.strobeWidget, 0, 0, 1, 7)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "strobeTuner"))
        self.pitchLabel.setText(_translate("mainWindow", "440"))
        self.automaticCheckbox.setText(_translate("mainWindow", "Auto"))
        self.noteLabel.setText(_translate("mainWindow", "A4"))

from strobeWindow import strobeWindow
