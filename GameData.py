# 0 - empty, no color
# 1 - filled, green
# 2 - filled, red
# 3 - filled, blue
# 4 - filled, yellow
class GameField:

    def __init__(self):
        self.__field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.__will_be_colored = list()
        self.__rand_color = list()
        self.__default_colors = [
            './icons/black.png',
            './icons/green.png',
            './icons/red.png',
            './icons/blue.png',
            './icons/yellow.png'
        ]
        self.__default_am_for_points = 5
        self.__default_am_to_color = 3
        self.__default_start = 15


    def change_cell(self, x, y, color):
        if color < len(self.__default_colors) or color > 0:
            if self.__field[x][y] == 0:
                self.__field[x][y] = color
            else:
                return -1
    @property
    def default_start(self):
        return self.__default_start
    @property
    def default_am_to_color(self):
        return self.__default_am_to_color
    @property
    def default_colors(self):
        return self.__default_colors
    @property
    def defaultam_for_points(self):
        return self.__default_am_for_points
    def clear_all(self):
        self.__rand_color.clear()
        self.__will_be_colored.clear()
    @property
    def rand_color(self):
        return self.__rand_color
    @property
    def field(self):
        return self.__field

    @property
    def will_be_colored(self):
        return self.__will_be_colored

    def color_next(self):
        import random
        self.__rand_color.append(random.randint(1, 4))
        rand_ind = (random.randint(0, 9), random.randint(0, 9))
        while self.__field[rand_ind[0]][rand_ind[1]] != 0:
            rand_ind = (random.randint(0, 9), random.randint(0, 9))
        else:
            self.__will_be_colored.append((rand_ind[0], rand_ind[1]))




def copy(gf):
    row = list()
    for i in range(10):
        column = list()
        for j in range(10):
            column.append(FIELD.field[i][j])
        row.append(column)
    return row


def print_matrix(matrix):
    print('-----------------------------------------')
    for i in matrix.field:
        print(i)
    print('-----------------------------------------')


def print_list(matrix):
    print('-----------------------------------------')
    for i in matrix:
        print(i)
    print('-----------------------------------------')


def random_colored(field, start_amount):
    import random
    for cells in range(start_amount):
        rand_color = random.randint(1, 4)
        rand_ind = (random.randint(0, 9), random.randint(0, 9))
        # if field[rand_ind[0]][rand_ind[1]] != 0:
        while field[rand_ind[0]][rand_ind[1]] != 0:
            rand_ind = (random.randint(0, 9), random.randint(0, 9))
        else:
            field[rand_ind[0]][rand_ind[1]] = rand_color


def will_be_colored(field, start_amount):
    import random
    to_color = list()
    for cells in range(start_amount):
        rand_color = random.randint(1, 4)
        rand_ind = (random.randint(0, 9), random.randint(0, 9))
        tmp = (rand_ind[0], rand_ind[1])
        # print('to_color check' + str(to_color.count(tmp)))
        while field[rand_ind[0]][rand_ind[1]] != 0 and to_color.count(tmp) > 0:
            rand_ind = (random.randint(0, 9), random.randint(0, 9))
        else:
            to_color.append((rand_ind, rand_color))
    return to_color

FIELD = GameField()

if __name__ == '__main__':
    FIELD.color_next()
    # print(FIELD.will_be_colored)
    # print(FIELD.will_be_colored[0][0])
    # for item in FIELD.will_be_colored:
    #     print(item)

