from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

import GameData


class mainMenu(QMainWindow):

    def __init__(self, logic):
        super().__init__()

        self.setWindowTitle('Main Menu')

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMinimumSize(400, 300)
        self.centralwidget.setObjectName("centralwidget")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())

        self.centralwidget.setSizePolicy(sizePolicy)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.centralwidget.setLayout(self.verticalLayout)

        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setText('START')
        self.start_button.setEnabled(True)
        self.start_button.setObjectName("start_button")
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.clicked.connect(lambda: self.init_game_field(logic))

        self.verticalLayout.addWidget(self.start_button)

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setText('EXIT')
        self.exit_button.setEnabled(True)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.clicked.connect(logic.kill_app)

        self.setCentralWidget(self.centralwidget)

    def init_endgame_widow(self, logic):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setFixedSize(300, 150)
        self.centralwidget.adjustSize()
        self.centralwidget.setObjectName("centralwidget")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())

        self.centralwidget.setSizePolicy(sizePolicy)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.centralwidget.setLayout(self.verticalLayout)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText(f'GAME OVER \nYour points: {logic.points}')
        self.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setText('EXIT')
        self.exit_button.setEnabled(True)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.clicked.connect(logic.kill_app)

        self.setCentralWidget(self.centralwidget)

    def init_game_field(self, logic):

        self.setWindowTitle('GameField')
        self.setFixedSize(1000, 1000)

        self.field = QtWidgets.QWidget(self)
        self.field.setObjectName("field")

        self.gridLayout = QtWidgets.QGridLayout(self.field)
        self.gridLayout.setObjectName("gridLayout")
        # print(GameData.FIELD.rand_color)
        # print(GameData.FIELD.will_be_colored)
        for i in range(10):
            for j in range(10):
                button = QPushButton(self.field)

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(1)
                sizePolicy.setVerticalStretch(1)
                sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())

                button.setSizePolicy(sizePolicy)
                button.setBaseSize(QtCore.QSize(3, 3))
                button.setObjectName(f"{i, j}")

                index = logic.contain_coord(i, j)
                if index != -1:
                    color = GameData.FIELD.rand_color.pop(index)
                    button.setIcon(QIcon(QPixmap(logic.define_color(color))))
                    GameData.FIELD.rand_color.insert(index, color)
                    button.setIconSize(QSize(50, 50))
                elif GameData.FIELD.field[i][j] == 0:
                    button.setIcon(QIcon(QPixmap(logic.define_color(0))))
                    button.setIconSize(QSize(400, 400))
                else:
                    icon = QIcon(QPixmap(logic.choose_color(i, j)))
                    button.setIcon(icon)
                    button.setIconSize(QSize(100, 100))

                button.clicked.connect(lambda: self.clicked(logic))

                self.gridLayout.addWidget(button, i, j, 1, 1)

        self.setCentralWidget(self.field)

    def clicked(self, logic):
        button = self.sender()
        if type(button) is not None:
            x = int(button.objectName()[1])
            y = int(button.objectName()[4])
            if logic.click_detected(x, y) > 0:
                print(1)
                self.update_field(logic)
            else:
                print(-1)
                self.init_endgame_widow(logic)

    def update_field(self, logic):
        buttons = self.field.children()
        buttons.pop(0)
        for el in buttons:
            index = logic.contain_coord(int(el.objectName()[1]), int(el.objectName()[4]))
            if index != -1:
                color = GameData.FIELD.rand_color.pop(index)
                el.setIcon(QIcon(QPixmap(logic.define_color(color))))
                GameData.FIELD.rand_color.insert(index, color)
                el.setIconSize(QSize(50, 50))
            elif GameData.FIELD.field[int(el.objectName()[1])][int(el.objectName()[4])] == 0:
                el.setIcon(QIcon(QPixmap(logic.define_color(0))))
                el.setIconSize(QSize(400, 400))
            else:
                icon = QIcon(QPixmap(logic.choose_color(int(el.objectName()[1]), int(el.objectName()[4]))))
                el.setIcon(icon)
                el.setIconSize(QSize(100, 100))
