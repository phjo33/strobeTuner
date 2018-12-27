from PyQt5.QtWidgets import QSpinBox

class pitchSpinBox(QSpinBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.lineEdit.setReadOnly(True)

