from tkinter import Tk, Canvas, Frame, BOTH

WHITE = '#FFFFFF'

colors = ['#007BB8',
          '#FFDF00',
          '#CC3333',
          '#FE28A2',
          '#39FF14',
          '#007F5C',
          '#F4C430',
          '#701C1C',
          '#D1E231',
          '#DDA0DD',
          '#682860',
          '#1CA9C9',
          '#2D383A',
          '#DA70D6',
          '#FF5800',
          '#CFB53B',
          '#48BF91',
          '#E4000F',
          '#00CCCC',
          '#FADA5E']

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1100
SQUARE_GAP = 1
PADDING = 5
MAX_SQUARE_LEN = 90


class HNBEGrid(Frame):
    def __init__(self, map_arr, square_width, square_gap, shape_type):
        super().__init__()

        self.n = len(map_arr)
        self.m = len(map_arr[0])
        self.map_arr = map_arr
        self.square_width = square_width
        self.square_gap = square_gap
        self.type = shape_type

        self.fill_canvas()

    def add_rectangle(self, canvas, y1_pads, y1_cells, x1_pads, x1_cells,
                      y2_pads, y2_cells, x2_pads, x2_cells, fill, width):
        canvas.create_rectangle(PADDING + self.square_gap * y1_pads + self.square_width * y1_cells,
                                PADDING + self.square_gap * x1_pads + self.square_width * x1_cells,
                                PADDING + self.square_gap * y2_pads + self.square_width * y2_cells,
                                PADDING + self.square_gap * x2_pads + self.square_width * x2_cells,
                                fill=fill,
                                width=width)

    def fill_canvas(self):
        self.master.title('Grid')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        width = 0

        if self.type == 'dsc_shape_border':
            width = 1

        for i in range(self.m):
            for j in range(self.n):
                self.add_rectangle(canvas, (i + 1), i, (j + 1), j, (i + 1), (i + 1), (j + 1), (j + 1),
                                   fill=get_color(self.map_arr[j][i]), width=width)

        if self.type == 'cnt_shape':
            for i in range(self.m):
                for j in range(self.n - 1):
                    if self.map_arr[j][i] == self.map_arr[j + 1][i]:
                        self.add_rectangle(canvas, (i + 1), i, (j + 1), (j + 1), (i + 1), (i + 1), (j + 2), (j + 1),
                                           fill=get_color(self.map_arr[j][i]), width=0)

            for i in range(self.m - 1):
                for j in range(self.n):
                    if self.map_arr[j][i] == self.map_arr[j][i + 1]:
                        self.add_rectangle(canvas, (i + 1), (i + 1), (j + 1), j, (i + 2), (i + 1), (j + 1), (j + 1),
                                           fill=get_color(self.map_arr[j][i]), width=0)

            for i in range(self.m - 1):
                for j in range(self.n - 1):
                    if self.map_arr[j][i] == self.map_arr[j + 1][i + 1]:
                        self.add_rectangle(canvas, (i + 1), (i + 1), (j + 1), (j + 1), (i + 2), (i + 1), (j + 2),
                                           (j + 1), fill=get_color(self.map_arr[j][i]), width=0)

        canvas.pack(fill=BOTH, expand=1)


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def draw_grid(map_arr, shape_type):
    """
    :param map_arr: list of lists of numbers
        inner lists' lengths should be the same, every number represents a piece of final puzzle
    :param shape_type: on of the following:
        @I   cnt_shape:         for a shape with continuous pieces (try this if you are not sure what to choose :D)
        @II  dsc_shape:         for a shape with pieces made of identical squares
        @III dsc_shape_border:  for a shape with pieces made of identical squares with borders
    """
    window_height = WINDOW_HEIGHT
    window_width = WINDOW_WIDTH
    square_gap = SQUARE_GAP
    n = len(map_arr)
    m = len(map_arr[0])

    square_width = min(
        (window_height - (square_gap * (n + 1))) / n,
        (window_width - (square_gap * (m + 1))) / m,
        MAX_SQUARE_LEN
    )

    window_width = square_width * n + square_gap * (n + 1) + PADDING * 2
    window_height = square_width * m + square_gap * (m + 1) + PADDING * 2

    root = Tk()

    HNBEGrid(map_arr, square_width, square_gap, shape_type)
    root.geometry(str(int(window_height)) + 'x' + str(int(window_width)))
    center(root)
    root.mainloop()


def get_color(piece):
    if piece == -1:
        return WHITE
    else:
        return colors[color_map[piece]]


color_map = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 3,
    6: 4,
    7: 0,
    8: 0,
    9: 3,
    10: 1,
    11: 1,
    12: 0,
    13: 3,
    14: 2,
    15: 4,
    16: 1,
    17: 1,
    18: 3,
    19: 4,
    20: 0,
    21: 2,
}

map_arr = [[-1, -1, 0, 0, 0, 1, 1, 1, 2, 2, -1, -1, 2, -1, 3, -1, 4, 4, 4],
           [-1, -1, 0, 0, 5, 5, -1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4],
           [0, 0, 0, 0, -1, 5, -1, 6, 6, 7, -1, 2, 2, -1, 8, -1, 4, 4, 4],
           [-1, 9, 10, 10, -1, 5, 5, 6, 6, 7, 7, 2, 2, -1, 8, 8, 8, 8, 8],
           [-1, 9, 10, 10, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 8, 8, 8, 8, 8],
           [9, 9, 10, 10, 10, 10, 10, 13, -1, 11, 11, 11, 11, 11, -1, 8, 8, 8, -1],
           [9, 9, 10, 10, -1, 12, -1, 13, 14, 14, -1, -1, 15, -1, -1, 8, 8, 8, 16],
           [17, 17, 19, 12, 12, 12, -1, 13, 14, 14, 18, 18, 15, 15, 15, 16, 16, 16, 16],
           [17, -1, 19, -1, -1, 12, 14, 14, 14, 14, -1, 18, 18, 20, -1, 16, 16, 21, -1],
           [19, 19, 19, 19, 19, 19, 14, 14, 14, 14, -1, -1, 18, 20, -1, 16, 16, 21, 21],
           [19, 19, 19, 19, -1, -1, 14, 14, 14, 14, -1, -1, 20, 20, 20, 16, 16, -1, 21]]


def main():
    draw_grid(map_arr, shape_type='cnt_shape')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
