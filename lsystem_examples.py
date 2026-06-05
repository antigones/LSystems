import turtle
from lsystem import LSystem
from renderer import render_pattern


def draw_system(omega, expansion_rules, draw_instructions, times, line_thickness=2):
    system = LSystem(omega, expansion_rules)
    pattern = system.expand(times=times)
    render_pattern(pattern, draw_instructions, line_thickness)


def draw_peano():
    peano_omega = "L"
    angle = 90
    times = 2
    step_size = 10
    peano_expansion_rules = {
        "L": "LFRFL-F-RFLFR+F+LFRFL",
        "R": "RFLFR+F+LFRFL-F-RFLFR",
        "F": "F",
        "+": "+",
        "-": "-"
    }

    peano_istructions = {
        "F": lambda: turtle.forward(step_size),
        "+": lambda: turtle.left(angle),
        "-": lambda: turtle.right(angle)
    }

    draw_system(
        omega=peano_omega,
        expansion_rules=peano_expansion_rules,
        draw_instructions=peano_istructions,
        times=times
        )


def draw_hilbert():
    hilbert_omega = "L"
    angle = 90
    times = 3
    step_size = 10
    hilbert_expansion_rules = {
        "L": "+RF-LFL-FR+",
        "R": "-LF+RFR+FL-",
        "F": "F",
        "+": "+",
        "-": "-"
    }
    
    hilbert_instructions = {
        "F": lambda: turtle.forward(step_size),
        "+": lambda: turtle.left(angle),
        "-": lambda: turtle.right(angle)
    }
    
    draw_system(
        omega=hilbert_omega,
        expansion_rules=hilbert_expansion_rules,
        draw_instructions=hilbert_instructions,
        times=times
    )


def draw_koch():
    koch_omega = "F"
    angle = 90
    times = 3
    step_size = 10
    koch_expansion_rules = {
        "F": "F+F-F-F+F",
        "+": "+",
        "-": "-"
    }
    
    koch_instructions = {
        "F": lambda: turtle.forward(step_size),
        "+": lambda: turtle.left(angle),
        "-": lambda: turtle.right(angle),
    }
    
    draw_system(
        omega=koch_omega,
        expansion_rules=koch_expansion_rules,
        draw_instructions=koch_instructions,
        times=times
    )


def draw_fractal_plant():
    fractal_plant_omega = "X"
    angle = 25
    times = 4
    step_size = 10
    fractal_plant_expansion_rules = {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF",
        "[": "[",
        "]": "]",
        "+": "+",
        "-": "-"
    }
    
    stack = []
    
    def push_pos_angle():
        stack.append((turtle.pos(), turtle.heading()))
    
    def pop_pos_angle():
        pos_, heading_ = stack.pop()
        turtle.penup()
        turtle.setposition(pos_)
        turtle.setheading(heading_)
        turtle.pendown()
    
    fractal_plant_instructions = {
        "F": lambda: turtle.forward(step_size),
        "+": lambda: turtle.left(angle),
        "-": lambda: turtle.right(angle),
        "[": push_pos_angle,
        "]": pop_pos_angle,
    }
    
    draw_system(
        omega=fractal_plant_omega,
        expansion_rules=fractal_plant_expansion_rules,
        draw_instructions=fractal_plant_instructions,
        times=times
    )


def draw_cantor():

    def move_forward(step_size):
        turtle.penup()
        turtle.setx(turtle.xcor()+step_size)
        turtle.pendown()

    cantor_omega = "A"
    times = 3
    step_size = 10
    cantor_expansion_rules = {
        "A": "ABA",
        "B": "BBB",
    }
    
    cantor_instructions = {
        "A": lambda: turtle.forward(step_size),
        "B": lambda: move_forward(step_size)
    }
    
    draw_system(
        omega=cantor_omega,
        expansion_rules=cantor_expansion_rules,
        draw_instructions=cantor_instructions,
        times=times
    )


def draw_sierpinsky():
    sierpinsky_omega = "F-G-G"
    angle = 120
    times = 3
    step_size = 10
    sierpinsky_expansion_rules = {
        "F": "F-G+F+G-F",
        "G": "GG",
        "+": "+",
        "-": "-"
    }
    
    sierpinsky_instructions = {
        "F": lambda: turtle.forward(step_size),
        "G": lambda: turtle.forward(step_size),
        "+": lambda: turtle.left(angle),
        "-": lambda: turtle.right(angle),
    }
    
    draw_system(
        omega=sierpinsky_omega,
        expansion_rules=sierpinsky_expansion_rules,
        draw_instructions=sierpinsky_instructions,
        times=times
    )


def draw_fractal_tree():
    fractal_tree_omega = "0"
    angle = 45
    times = 3
    step_size = 10
    fractal_tree_expansion_rules = {
        "1": "11",
        "0": "1{0}0",
        "{": "{",
        "}": "}",
    }
    
    stack = []
    
    def push_pos_set_angle():
        stack.append((turtle.pos(), turtle.heading()))
        turtle.setheading(45)
    
    def pop_pos_set_angle():
        pos_, _ = stack.pop()
        turtle.penup()
        turtle.setposition(pos_)
        turtle.setheading(-45)
        turtle.pendown()
    
    fractal_tree_instructions = {
        "0": lambda: turtle.forward(step_size),
        "1": lambda: turtle.forward(step_size),
        "{": push_pos_set_angle,
        "}": pop_pos_set_angle,
    }
    
    draw_system(
        omega=fractal_tree_omega,
        expansion_rules=fractal_tree_expansion_rules,
        draw_instructions=fractal_tree_instructions,
        times=times
    )


def draw_dragon_curve():
    dragon_curve_omega = "F"
    angle = 90
    times = 10
    step_size = 10
    dragon_curve_expansion_rules = {
        "F": "F+G",
        "G": "F-G",
        "+": "+",
        "-": "-",
    }
    
    dragon_curve_instructions = {
        "F": lambda: turtle.forward(step_size),
        "G": lambda: turtle.forward(step_size),
        "+": lambda: turtle.left(angle),
        "-": lambda: turtle.right(angle),
    }
    
    draw_system(
        omega=dragon_curve_omega,
        expansion_rules=dragon_curve_expansion_rules,
        draw_instructions=dragon_curve_instructions,
        times=times
    )

def main():
    # draw_peano()
    # draw_hilbert()
    draw_cantor()
    # draw_fractal_tree()
    # draw_sierpinsky()
    # draw_koch()
    # draw_dragon_curve()



if __name__ == '__main__':
    main()
