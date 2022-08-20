class Rectangle(object):
    def __init__(self, width=0, height=0):
        self.line = None
        self.width = int(width)
        self.height = int(height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, x):
        self.width = int(x)

    def set_height(self, x):
        self.height = int(x)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        self.line = ""
        for number in range(self.height):
            self.line += "*" * self.width
            self.line += "\n"
        if self.width > 50 or self.height > 50:
            self.line = "Too big for picture."
        return self.line

    def get_amount_inside(self, shape):
        if self.height >= shape.height and self.width >= shape.width:
            height_div = self.height / shape.height
            width_div = self.width / shape.width
        else:
            height_div = 0
            width_div = 0
        return int(height_div) * int(width_div) if height_div >= 1 and width_div >= 1 else 0


class Square(Rectangle):
    def __init__(self, side=0):
        Rectangle.__init__(self, width=0, height=0)
        self.side = None
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, x):
        self.width = x
        self.height = x

    def set_height(self, x):
        self.height = x
        self.width = x
    
    def set_side(self, x):
        self.side = x
        self.set_width(x)
        self.set_height(x)
