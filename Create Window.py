import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QCheckBox, QRadioButton

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        a = 10
        self.setGeometry(400, 400, 300, 180)
        self.setWindowTitle('Window')
        btn = QPushButton("Button", self)
        btn.move(100,130)
        btn.clicked.connect(self.test)

        self.label_1 = QLabel(self)
        self.label_1.setText('Select 1')
        self.label_1.move(20, 5)
        self.cb_1 = QCheckBox("1", self)
        self.cb_1.move(20, 20)
        self.cb_2 = QCheckBox("2", self)
        self.cb_2.move(20, 40)
        self.cb_3 = QCheckBox("3", self)
        self.cb_3.move(20, 60)

        self.label_2 = QLabel(self)
        self.label_2.setText('2+2')
        self.label_2.move(100, 5)
        self.rb_1 = QRadioButton('4', self)
        self.rb_1.move(100, 20)
        self.rb_2 = QRadioButton('2', self)
        self.rb_2.move(100, 40)
        self.rb_3 = QRadioButton('5', self)
        self.rb_3.move(100, 60)

        self.label_3 = QLabel(self)
        self.label_4 = QLabel(self)

    def test(self):
        self.checkbox()
        self.radiobox()

    def checkbox(self):
        self.x = 0

        if self.cb_1.isChecked():
            self.x += 1
        if self.cb_2.isChecked():
            self.x += 1
        if self.cb_3.isChecked():
            self.x += 1

        self.label_3.move(25, 80)
        self.label_3.setText(str(self.x))

    def radiobox(self):
        self.label_4.move(100, 80)

        if  self.rb_1.isChecked():
            self.label_4.setText('Yes')
        else:
            self.label_4.setText('No')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Window()
    controller.show()
    sys.exit(app.exec())
