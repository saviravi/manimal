from manimlib.imports import *

class TestScene1(Scene):
    def moving_circles(self, circ1, circ2):
        self.play(GrowFromCenter(circ1))
        self.play(ApplyMethod(circ1.shift, RIGHT), GrowFromCenter(circ2))
        self.play(ApplyMethod(circ2.shift, 2*RIGHT), ApplyMethod(circ1.move_to, LEFT))
        self.play(FadeOutAndShift(circ2, RIGHT))

    def construct(self):
        circle1 = Circle(color=PURPLE)
        circle1.move_to(RIGHT)
        circle2 = Circle(color=RED)
        circle2.move_to(LEFT)
        # self.play(GrowFromEdge(circle1, LEFT))
        self.moving_circles(circle1, circle2)
        