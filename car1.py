from graphics import Point, Rectangle, GraphWin

class Car():
    def __init__(self, back_wheel_center, back_wheel_radius, front_wheel_center, front_wheel_radius, body_height):
        upper_left_point = Point(back_wheel_center.x, back_wheel_center.y - body_height)
        bottom_right_point = front_wheel_center
        self.body = Rectangle(upper_left_point, bottom_right_point)

    def set_color(self, tire_color, wheel_color, body_color):
        self.body.setFill(body_color)

    def draw(self, win):
        self.body.draw(win)

    def animate(self, win, dx, dy, n):
        pass

def main():
    win = GraphWin("An Awesome Car", 700, 300)

    car = Car(Point(50, 50), 15, Point(100,50), 15, 40)
    car.set_color('black', 'gray', 'pink')
    car.draw(win)

    win.mainloop()

main()
