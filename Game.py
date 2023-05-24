from UI import menu


class HandlerEvent:

    def __init__(self):
        self.__x = -1
        self.__y = -1
        self.__clicked = False

    # @staticmethod
    # def start_button_controller(central_widget):
    #     central_widget.setCentralWidget = start_ui(central_widget)

    def mouse_clicked(x, y, state):
        OVERLORD.x = x
        OVERLORD.y = y
        OVERLORD.clicked = state

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    @x.setter
    def x(self, x):
        self.__x = x
    @y.setter
    def y(self, y):
        self.__y = y
    @property
    def clicked(self):
        return self.__clicked

    @clicked.setter
    def clicked(self, state):
        self.__clicked = state


    @property
    def is_clicked(self):
        return self.__clicked

    def reset(self):
        self.__x = -1
        self.__y = -1
        self.__clicked = False

    def start_app(self):
        menu.start_app()


if __name__ == '__main__':
    OVERLORD = HandlerEvent()
    OVERLORD.start_app(OVERLORD)
