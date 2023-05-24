# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

import GameData


class Game_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(1000, 1000)
        self.field = QtWidgets.QWidget(self)
        self.field.setObjectName("field")
        self.gridLayout = QtWidgets.QGridLayout(self.field)
        self.gridLayout.setObjectName("gridLayout")
        self.button_list = list
        for i in range(10):
            for j in range(10):
                button = QPushButton(self.field)
                label = QLabel(self.field)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(1)
                sizePolicy.setVerticalStretch(1)
                sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
                button.setSizePolicy(sizePolicy)
                label.setSizePolicy(sizePolicy)
                button.setBaseSize(QtCore.QSize(3, 3))
                label.setBaseSize(QtCore.QSize(3, 3))
                label.setText(str(GameData.FIELD.field[i][j]))
                label.setObjectName(f"{i, j}")
                button.setObjectName(f"{i, j}")
                button.clicked.connect(self.clicked_func)
                button.setText(str(GameData.FIELD.field[i][j]))
                self.gridLayout.addWidget(button, i, j, 1, 1)
        self.setCentralWidget(self.field)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def clicked_func(self):
        button = self.sender()
        if type(button) is not None:
            x = int(button.objectName()[1])
            y = int(button.objectName()[4])
            Game.mouse_clicked(x, y, True)
            button.setText(str(GameData.FIELD.field[x][y]))


def start_ui(current_app):
    # app = QApplication([])

    window = Game_MainWindow()
    current_app.setCentralWidget(window)

    # app.exec()
