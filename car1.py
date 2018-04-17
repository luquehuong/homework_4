from graphics import Point, Rectangle, GraphWin
from wheel import Wheel

class Car():
    WHEEL_TO_TIRE_RATIO = 0.6

    def __init__(self, back_wheel_center, back_tire_radius, front_wheel_center, front_tire_radius, body_height):
        upper_left_point = Point(back_wheel_center.x, back_wheel_center.y - body_height)
        bottom_right_point = front_wheel_center
        self.body = Rectangle(upper_left_point, bottom_right_point)

        self.back_wheel = Wheel(back_wheel_center, back_tire_radius * Car.WHEEL_TO_TIRE_RATIO, back_tire_radius)
        self.front_wheel = Wheel(front_wheel_center, front_tire_radius * Car.WHEEL_TO_TIRE_RATIO, front_tire_radius)

    def set_color(self, tire_color, wheel_color, body_color):
        self.body.setFill(body_color)

        self.back_wheel.set_color(wheel_color, tire_color)
        self.front_wheel.set_color(wheel_color, tire_color)

    def draw(self, win):
        self.body.draw(win)
        self.back_wheel.draw(win)
        self.front_wheel.draw(win)

    def move(self, dx, dy):
        self.back_wheel.move(dx, dy)
        self.front_wheel.move(dx, dy)
        self.body.move(dx, dy)

    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(10, self.animate, win, dx, dy, n - 1)

def main():
    win = GraphWin("An Awesome Car", 700, 300)

    car = Car(Point(50, 50), 15, Point(100,50), 15, 40)
    car.set_color('black', 'gray', 'pink')
    car.draw(win)
    car.animate(win, 1, 0, 550)

    win.mainloop()

if __name__ == '__main__':
    main()
