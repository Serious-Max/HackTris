class Tetris:
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.board = [list([0] * xsize) for _ in range(ysize)]

    # def get_board(self):
    #    return self.board

    def figure(self, type, pozition):
        figure_list = [
            # 0 - line, 1 - square, 2 - 'L',
            # 3 - 'Z', 4 - 'T', 5 - 'L's, 6 - 'Z's
            [[1, 4, '1111', 0, 0, 2],
             [4, 1, '1111', 0, -1, 1]],

            [[2, 2, '1111', 1, -1, 2]],

            [[2, 3, '101011', 2, 0, 4],
             [3, 2, '111100', 2, 1, 1],
             [2, 3, '110101', 2, 2, 2],
             [3, 2, '001111', 2, -1, 3]],

            [[3, 2, '011110', 3, 0, 2],
             [2, 3, '101101', 3, -1, 1]],

            [[3, 2, '010111', 4, 0, 4],
             [2, 3, '101110', 4, 1, 1],
             [3, 2, '111010', 4, 2, 2],
             [2, 3, '011101', 4, -1, 3]],

            [[2, 3, '010111', 5, 0, 4],
             [3, 2, '100111', 5, 1, 1],
             [2, 3, '111010', 5, 2, 2],
             [3, 2, '111001', 5, -1, 3]],

            [[3, 2, '110011', 6, 0, 2],
             [2, 3, '011110', 6, -1, 1]]
        ]
        return figure_list[type][pozition]

    def is_intersection(self, figure, x, y):
        if (figure[0] + x > self.xsize) \
                or (x < 0) or (figure[1] + y > self.ysize):
            return True
        else:
            temp = list(figure[2])
            for i in range(len(temp)):
                if (temp[i] == '1') \
                        and (self.board[x + i % figure[0]][y + i // figure[1]] != '0'):
                    return True
            return False

    def rotate(self, degree=0, figure):
        if degree == 0:
            return self.figure(figure[3], figure[4] + 1)
        else:
            return self.figure(figure[3], figure[5] + 1)

    def render(self, figure, x, y):
        temp1 = self.board
        temp2 = list(figure[2])
        for i in range(len(temp)):
            temp1[x + i % figure[0]][y + i // figure[1]] = temp2[i]
        return temp1

    def add(self, figure, x, y):
        temp2 = list(figure[2])
        for i in range(len(temp)):
            self.boardx[x + i % figure[0]][y + i // figure[1]] = temp2[i]
