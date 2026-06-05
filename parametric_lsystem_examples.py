import turtle
from parametric_lsystem import ParametricLSystem
from renderer import render_parametric_pattern

def draw_sunflower():
    angle = 137.5
    times = 500
    scale_factor = 15

    # ω : A(0)
    sunflower_omega = [("A", 0)]

    # Parametric expansion rule: A(n) -> +(137.5) [ f(n^0.5) ~D ] A(n+1)
    sunflower_expansion_rules = {
        "A": lambda n: [
            ("+", angle), 
            ("[", None), 
            ("f", n**0.5), 
            ("~D", None), 
            ("]", None), 
            ("A", n + 1)
        ]
    }

    stack = []
    
    def push_position():
        stack.append(turtle.pos())
    
    def pop_position():
        saved_pos = stack.pop()
        turtle.penup()
        turtle.setposition(saved_pos)
        turtle.pendown()

    sunflower_instructions = {
        "+": lambda current_angle: turtle.left(current_angle),
        "f": lambda distance: (turtle.penup(), turtle.forward(distance * scale_factor), turtle.pendown()),
        "~D": lambda _: turtle.dot(8, "darkgreen"),
        "[": lambda _: push_position(),
        "]": lambda _: pop_position(),
    }

    system = ParametricLSystem(sunflower_omega, sunflower_expansion_rules)
    pattern = system.expand(times=times)
    
    render_parametric_pattern(pattern, sunflower_instructions, line_thickness=2)

if __name__ == "__main__":
    draw_sunflower()