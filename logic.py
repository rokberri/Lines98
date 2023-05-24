import copy

from PyQt6.QtWidgets import QApplication

import GameData
from main import mainMenu


class Logic:

    def __init__(self):
        self.__x = -1
        self.__y = -1
        self.__clicked = False
        self.__points = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def points(self):
        return self.__points
    def reset(self):
        self.__x = -1
        self.__y = -1
        self.__clicked = False

    def click_detected(self, x, y):
        # print(x, y)
        field = GameData.FIELD.field
        current_pos = (x, y)
        if (self.__x != -1) and (self.__y != -1) and (field[self.__x][self.__y] != 0):
            if self.can_attend((self.__x, self.__y), current_pos) and (self.__x, self.__y) != current_pos:
                if GameData.FIELD.change_cell(x, y, field[self.__x][self.__y]) != -1:

                    collected = False
                    clear_pass = self.init_path_to_clear(current_pos)
                    if len(clear_pass) >= GameData.FIELD.defaultam_for_points:
                        last_el = clear_pass.pop()
                        first_el = clear_pass.pop(0)
                        from_last_ind = self.init_path_to_clear(last_el)
                        from_first_ind = self.init_path_to_clear(first_el)
                        if len(from_first_ind) >= GameData.FIELD.defaultam_for_points:
                            clear_pass = clear_pass + from_first_ind
                        else:
                            clear_pass.insert(0, first_el)
                        if len(from_last_ind) >= GameData.FIELD.defaultam_for_points:
                            clear_pass = clear_pass + from_last_ind
                        else:
                            clear_pass.insert(0, last_el)
                        self.count_points(clear_pass)
                        self.__points = self.__points + len(clear_pass)
                        collected = True
                    field[self.__x][self.__y] = 0

                    if GameData.FIELD.will_be_colored.count((x, y)) > 0:
                        GameData.FIELD.clear_all()
                        GameData.FIELD.color_next()

                    if not collected:
                        for coord in GameData.FIELD.will_be_colored:
                            color = GameData.FIELD.rand_color.pop(0)
                            field[coord[0]][coord[1]] = color
                            clear_pass = self.init_path_to_clear((coord[0], coord[1]))

                            if len(clear_pass) >= GameData.FIELD.defaultam_for_points:
                                last_el = clear_pass.pop()
                                first_el = clear_pass.pop(0)
                                from_last_ind = self.init_path_to_clear(last_el)
                                from_first_ind = self.init_path_to_clear(first_el)
                                if len(from_first_ind) >= GameData.FIELD.defaultam_for_points:
                                    clear_pass = clear_pass + from_first_ind
                                else:
                                    clear_pass.insert(0, first_el)
                                if len(from_last_ind) >= GameData.FIELD.defaultam_for_points:
                                    clear_pass = clear_pass + from_last_ind
                                else:
                                    clear_pass.insert(0, last_el)
                                self.count_points(clear_pass)

                            GameData.FIELD.rand_color.append(color)
                        GameData.FIELD.clear_all()
                        if self.count_free_cells() > GameData.FIELD.defaultam_for_points-1:
                            self.color_next(GameData.FIELD.defaultam_for_points)
                        else:
                            self.color_next(self.count_free_cells())

                    self.reset()
                    return self.count_free_cells()
            else:
                self.__x = x
                self.__y = y
        elif field[x][y] != 0:
            self.__x = x
            self.__y = y
        return self.count_free_cells()


    def count_points(self, clear_pass):
        for cell in clear_pass:
            # GameData.FIELD.change_cell(cell[0], cell[0], 0)
            GameData.FIELD.field[cell[0]][cell[1]] = 0

    def init_path_to_clear(self, current_pos):
        clear_pass = list()
        clear_pass.append(current_pos)
        d_right_up = self.d_right_up(current_pos)
        d_right_down = self.d_right_down(current_pos)
        d_left_up = self.d_left_up(current_pos)
        d_left_down = self.d_left_down(current_pos)
        up = self.up(current_pos)
        down = self.down(current_pos)
        left = self.left(current_pos)
        right = self.right(current_pos)
        # print(d_right_up)
        # print(d_right_down)
        # print(d_left_up)
        # print(d_left_down)
        # print(up)
        # print(down)
        # print(left)
        # print(right)
        if len(d_right_up) + len(d_left_down) >= 4:
            clear_pass = clear_pass + d_right_up + d_left_down
        if len(d_right_down) + len(d_left_up) >= 4:
            clear_pass = clear_pass + d_right_down + d_left_up
        if len(up) + len(down) >= 4:
            clear_pass = clear_pass + up + down
        if len(left) + len(right) >= 4:
            clear_pass = clear_pass + left + right
        return clear_pass

    def d_right_up(self, start_pos):
        path = list()
        current_pos = start_pos
        while current_pos[0] - 1 >= 0 and current_pos[1] + 1 <= 9 and \
                self.get_color(start_pos[0], start_pos[1]) == self.get_color(current_pos[0] - 1, current_pos[1] + 1):
            next_pos = (current_pos[0] - 1, current_pos[1] + 1)
            path.append(next_pos)
            current_pos = next_pos
        else:
            return path

    def d_left_down(self, start_pos):
        path = list()
        current_pos = start_pos
        while current_pos[0] + 1 <= 9 and current_pos[1] - 1 >= 0 and \
                self.get_color(start_pos[0], start_pos[1]) == self.get_color(current_pos[0] + 1, current_pos[1] - 1):
            next_pos = (current_pos[0] + 1, current_pos[1] - 1)
            path.append(next_pos)
            current_pos = next_pos
        else:
            return path

    def d_left_up(self, start_pos):
        path = list()
        current_pos = start_pos
        while current_pos[0] - 1 >= 0 and current_pos[1] - 1 >= 0 and \
                self.get_color(start_pos[0], start_pos[1]) == self.get_color(current_pos[0] - 1, current_pos[1] - 1):
            next_pos = (current_pos[0] - 1, current_pos[1] - 1)
            path.append(next_pos)
            current_pos = next_pos
        else:
            return path

    def color_next(self, amount):
        for i in range(amount):
            GameData.FIELD.color_next()

    def d_right_down(self, start_pos):
        path = list()
        current_pos = start_pos
        while current_pos[0] + 1 <= 9 and current_pos[1] + 1 <= 9 and \
                self.get_color(start_pos[0], start_pos[1]) == self.get_color(current_pos[0] + 1, current_pos[1] + 1):
            next_pos = (current_pos[0] + 1, current_pos[1] + 1)
            path.append(next_pos)
            current_pos = next_pos
        else:
            return path

    def up(self, start_pos):
        path = list()
        current_pos = start_pos
        while current_pos[0] - 1 >= 0 and \
                self.get_color(start_pos[0], start_pos[1]) == self.get_color(current_pos[0] - 1, current_pos[1]):
            next_pos = (current_pos[0] - 1, current_pos[1])
            path.append(next_pos)
            current_pos = next_pos
        else:
            return path

    def down(self, start_pos):
        path = list()
        current_pos = start_pos
        while current_pos[0] + 1 <= 9 and \
                self.get_color(start_pos[0], start_pos[1]) == self.get_color(current_pos[0] + 1, current_pos[1]):
            next_pos = (current_pos[0] + 1, current_pos[1])
            path.append(next_pos)
            current_pos = next_pos
        else:
            return path

    def right(self, start_pos):
        path = list()
        current_pos = start_pos
        while current_pos[1] + 1 <= 9 and \
                self.get_color(start_pos[0], start_pos[1]) == self.get_color(current_pos[0], current_pos[1] + 1):
            next_pos = (current_pos[0], current_pos[1] + 1)
            path.append(next_pos)
            current_pos = next_pos
        else:
            return path

    def left(self, start_pos):
        path = list()
        current_pos = start_pos
        while current_pos[1] - 1 >= 0 and \
                self.get_color(start_pos[0], start_pos[1]) == self.get_color(current_pos[0], current_pos[1] - 1):
            next_pos = (current_pos[0], current_pos[1] - 1)
            path.append(next_pos)
            current_pos = next_pos
        else:
            return path

    @staticmethod
    def kill_app():
        exit()

    @staticmethod
    def choose_color(x, y):
        if GameData.FIELD.field[x][y] == 0:
            return GameData.FIELD.default_colors[0]
        elif GameData.FIELD.field[x][y] == 1:
            return GameData.FIELD.default_colors[1]
        elif GameData.FIELD.field[x][y] == 2:
            return GameData.FIELD.default_colors[2]
        elif GameData.FIELD.field[x][y] == 3:
            return GameData.FIELD.default_colors[3]
        else:
            return GameData.FIELD.default_colors[4]

    @staticmethod
    def check_for_points():
        pass

    def can_attend(self, start, end):

        from pathfinding.core.diagonal_movement import DiagonalMovement
        from pathfinding.core.grid import Grid
        from pathfinding.finder.a_star import AStarFinder

        matrix = GameData.copy(GameData.FIELD)

        for i in range(10):
            for j in range(10):
                matrix[i][j] = matrix[i][j] * -1
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[i][j] + 10
        matrix[start[0]][start[1]] = 10
        # GameData.print_list(matrix)
        grid = Grid(matrix=matrix)
        # GameData.print_list(matrix)
        start_pos = grid.node(start[1], start[0])
        end_pos = grid.node(end[1], end[0])
        seeker = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = seeker.find_path(start_pos, end_pos, grid)
        grid.cleanup()
        return len(path) > 0

    def contain_coord(self, x, y):
        for i, item in enumerate(GameData.FIELD.will_be_colored):
            if item[0] == x and item[1] == y:
                return i
        return -1

    def get_color(self, x, y):
        return GameData.FIELD.field[x][y]

    @staticmethod
    def define_color(num):
        if num == 0:
            return GameData.FIELD.default_colors[0]
        elif num == 1:
            return GameData.FIELD.default_colors[1]
        elif num == 2:
            return GameData.FIELD.default_colors[2]
        elif num == 3:
            return GameData.FIELD.default_colors[3]
        else:
            return GameData.FIELD.default_colors[4]

    @staticmethod
    def count_free_cells():
        flat_list = [item for sublist in GameData.FIELD.field for item in sublist]
        return flat_list.count(0)


if __name__ == '__main__':
    game_logic = Logic()
    GameData.random_colored(GameData.FIELD.field, GameData.FIELD.default_start)
    game_logic.color_next(3)
    app = QApplication([])
    app.setStyleSheet("""
                        QPushButton:focus {
                        outline-color: transparent;
                        border: 2px solid;
                        border-color: rgba(151, 195, 243, 1);
                                            }
                                            """)

    window = mainMenu(game_logic)

    window.show()

    app.exec()
    # game_logic.check_for_points()
