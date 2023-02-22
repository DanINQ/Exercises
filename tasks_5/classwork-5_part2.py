class Commons:
    def side_sum_p(self, sides, figure_name):
        self.figure_p = sum(sides)
        print('{} perimeter is :'.format(figure_name), self.figure_p)
        return self.figure_p

    def existance_check(self, sides, figure_name):
        return max(sides) <= sum(sides) - max(sides)

    def not_exists_print(self, figure_name):
        print("Wrong sides! {} doesn't exists!".format(figure_name))

    def half_perimeter(self, perimeter):
        return perimeter / 2

class Square:
    def __init__(self, side):
        self.sqr_p = side * 4
        print('Suares perimeter is: ',self.sqr_p)

        self.sqr_s = side * side
        print('Suares square is: ',self.sqr_s)

class Rectangle(Commons):
    def __init__(self, sides):
        self.rct_p = self.side_sum_p(sides, 'Rectangle')

        self.rct_s = sides[0] * sides[1]
        print('Rectangles square is: ', self.rct_s)

class Triangle(Commons):
    def __init__(self, sides):
        if self.existance_check(sides, 'Triangle'):
            print('Triangle exists!')

            self.trg_p = self.side_sum_p(sides, 'Triangle')

            self.half_trg_p = self.half_perimeter(self.trg_p)
            self.trg_s = (self.half_trg_p * (self.half_trg_p - sides[0]) * (self.half_trg_p - sides[1]) * (self.half_trg_p - sides[2])) ** (0.5)
            print('Triangles square is :', self.trg_s)
        else:
            self.not_exists_print('Triangle')

class Polygon(Commons):
    def __init__(self, sides):
        if self.existance_check(sides, 'Polygon'):
            print('Polygon exists!')

            self.poly_p = self.side_sum_p(sides, 'Polygon')

            self.half_poly_p = self.half_perimeter(self.poly_p)
            self.poly_s = ((self.half_poly_p - sides[0]) * (self.half_poly_p - sides[1]) * (self.half_poly_p - sides[2]) * (self.half_poly_p - sides[3])) ** (0.5)
            print('Polygon square is: ', self.poly_s)
        else:
            self.not_exists_print('Polygon')



while True:
    try:
        user_sides = input('\n\nEnter the sides length for figure to calc a perimeter and a square.\n'
                       'Split the sides length numbers by the space.\n'
                       'One for square, two for rectangle, three for triangle, four for polygon.\n'
                       '*For polygons use the sides of quadrilateral, around which a circle can be circumscribed*\n')
        sides = [int(i) for i in user_sides.split()]
        if len(sides) == 1:
            square = Square(sides[0])
            break
        elif len(sides) == 2:
            rectangle = Rectangle(sides)
            break
        elif len(sides) == 3:
            triangle = Triangle(sides)
            break
        elif len(sides) == 4:
            polygon = Polygon(sides)
            break
        else:
            print('Only 1-4 sides!')
    except ValueError as v:
        print('Use only numbers please!')