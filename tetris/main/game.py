class Dot:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        
class Field:
    def __init__(self, rows, cols, dots):
        self.rows = rows
        self.cols = cols
        self.dots = dots
        self.land = []
        self.fig = []
        self.fig_to_check = []
        self.struct_land()
        self.struct_fig()

    def struct_land(self):
        for i in self.dots:
            if i.value == '#':
                self.land.append(i)

    def struct_fig(self):
        for i in self.dots:
            if i.value == 'p':
                self.fig.append(i)

        for i in self.fig:
            self.fig_to_check.append(i)
            for t in self.fig_to_check:
                if i.x == t.x and i.y != t.y:
                    self.fig_to_check.remove(t)

    def get_dot(self, x, y):
        for i in self.dots:
            if i.x == x and i.y == y:
                return i

    def step(self):
        self.fig.reverse()
        for i in self.fig:
            self.get_dot(i.x, i.y).value = '.'
            self.get_dot(i.x, i.y+1).value = 'p'
        self.fig.clear()
        self.fig_to_check.clear()
        self.struct_fig()

    def check(self):
        for i in self.fig_to_check:
            for t in self.land:
                if i.x == t.x and (i.y + 1) == t.y:
                    return False
                elif (i.y + 1) >= self.rows:
                    return False
        return True

    def play(self):
        next = self.check()
        while next:
            self.step()
            next = self.check()

    def get_field(self):
        out = ''
        count = 0
        for i in self.dots:
            out = out + i.value
            count = count + 1
            if count % self.cols == 0:
                out = out + '\n'
        return out[:-1]


def create_field(data):
    data = data.split('\n')
    size = data.pop(0).split()

    field = []
    for i in range(len(data)):
        field.append(list(data[i]))

    dots = []
    for i1, t1 in enumerate(field):
        for i2, t2 in enumerate(t1):
            dot = Dot(i2, i1, t2)
            dots.append(dot)

    return Field(int(size[0]), int(size[1]), dots)
