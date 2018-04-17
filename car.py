from graphics import GraphWin, Point, Circle, Rectangle
from wheel import Wheel

# create a car object
class Car():
    def __init__(self, wheel_1, wheel_2, body):
        self.wheel_1 = Wheel(wheel_center_1, wheel_radius_1, tire_radius_1)
        self.wheel_2 = Wheel(wheel_center_2, wheel_radius_2, tire_radius_2)
        self.body = Rectangle(upper_left_point, bottom_right_point)

    def set_color(self, wheel_color, tire_color, body_color):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)
        self.body_rectangle.setFill(body_color)

    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n - 1)

def main():
    new_win = GraphWin("A Car", 700, 300)

    # 1st wheel centered at 50,50 with radius 15
    wheel_center_1 = Point(50, 50)
    wheel_radius_1 = 15
    tire_radius_1 = 0.6*tire_radius_1

    # 2nd wheel centered at 100,50 with radius 15
    wheel_center_2 = Point(100, 50)
    wheel_radius_2 = 15
    tire_radius_2 = 0.6*tire_radius_1

    # rectangle with a height of 40
    upper_left_point = Point(15,55)
    bottom_right_point = Point(75,15)

    wheel_1 = Wheel(wheel_center_1, 0.6 * tire_radius_1, tire_radius_1)
    wheel_2 = Wheel(wheel_center_2, 0.6 * tire_radius_2, tire_radius_2)
    body = Rectangle(upper_left_point, bottom_right_point)

    # Set its color
    wheel_1.set_color('OliveDrab1', 'Pink')
    wheel_2.set_color('OliveDrab1', 'Pink')
    body.setFill('Blue')

    # And finally, draw it
    wheel_1.draw(new_win)
    wheel_2.draw(new_win)
    body.draw(new_win)

    car1 = Car(wheel_1, wheel_2, body)
    car1.draw(new_win)

    # make the car move on the screen
    car1.animate(new_win, 1, 0, 400)

    new_win.mainloop()

main()

