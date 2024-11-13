import math
from typing import Union, List

class Circle:
    def __init__(self, radius: Union[int, float] = None, diameter: Union[int, float] = None):
        if radius is not None and diameter is not None:
            raise ValueError("Specify either radius or diameter, not both")
        elif radius is not None:
            self._radius = float(radius)
        elif diameter is not None:
            self._radius = float(diameter) / 2
        else:
            raise ValueError("Must specify either radius or diameter")

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def diameter(self) -> float:
        return self._radius * 2

    @property
    def area(self) -> float:
        return math.pi * self._radius ** 2

    def __str__(self) -> str:
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __add__(self, other: 'Circle') -> 'Circle':
        if not isinstance(other, Circle):
            raise TypeError("Can only add Circle objects together")
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other: 'Circle') -> bool:
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle objects")
        return self.radius < other.radius

    def __eq__(self, other: 'Circle') -> bool:
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle objects")
        return math.isclose(self.radius, other.radius, rel_tol=1e-9)

def draw_circles(circles: List[Circle]):
    try:
        import turtle
        screen = turtle.Screen()
        t = turtle.Turtle()
        t.speed(0)
        
        max_radius = max(c.radius for c in circles)
        spacing = max_radius * 3
        
        y_pos = (len(circles) - 1) * spacing / 2
        
        for circle in circles:
            t.penup()
            t.goto(0, y_pos)
            t.pendown()
            
            t.circle(circle.radius)
            
            y_pos -= spacing
        
        screen.exitonclick()
        
    except ImportError:
        print("Turtle module not available. Cannot draw circles.")

c1 = Circle(radius=17)

print(c1)