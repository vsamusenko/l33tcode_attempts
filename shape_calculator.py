class Rectangle:


    def __init__(self, width, height):
        self.width_in = width
        self.height_in = height
        self.area = 0.0
        self.diagonal = 0.0
        self.perimeter = 0
        self.picture_str = ''
        self.shape_type = 'Rectangle'
        self.times_fit = 0


    def set_width(self, new_width):
        self.width_in = new_width

    def set_height(self, new_height):
        self.height_in = new_height

    def get_area(self):
        self.area = self.width_in * self.height_in
        return self.area

    def get_perimeter(self):
        self.perimeter = (2 * self.width_in) + (2 * self.height_in)
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = ((self.width_in ** 2) + (self.height_in ** 2)) ** 0.5
        return self.diagonal

    def get_picture(self):
        if self.width_in > 50 or self.height_in > 50:
            return 'Too big for picture.'
        else:
            for line in range(self.height_in):
                self.picture_str += '*' * self.width_in + '\n'

            return self.picture_str

    def get_amount_inside(self, shape):
        if isinstance(shape, Rectangle):
            if shape.width_in <= self.width_in and shape.height_in <= self.height_in:
                self.times_fit = int(self.width_in / shape.width_in) * int(self.height_in / shape.height_in)
                return self.times_fit
            else:
                return 0
        else:
            return 0

    def __str__(self):
        return self.shape_type + f'(width={self.width_in}, height={self.height_in})'


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.shape_type = 'Square'

    def set_width(self, new_width):
        self.width_in = new_width
        self.height_in = new_width

    def set_height(self, new_height):
        self.height_in = new_height
        self.width_in = new_height

    def set_side(self, side_new):
        self.set_width(side_new)
        self.set_height(side_new)

    def __str__(self):
        return self.shape_type + f'(side={self.height_in})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))