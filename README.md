# L-System

A class to expand strings with L-System production rules and render them with Turtle.

    from lsystem import LSystem
    from renderer import render_pattern
    import turtle

    koch_omega = "F"
    koch_expansion_rules = {
        "F": "F+F-F-F+F",
        "+": "+",
        "-": "-"
    }

    koch = LSystem(koch_omega, koch_expansion_rules)
    pattern = koch.expand(times=3)

    koch_instructions = {
        "F": lambda: turtle.forward(10),
        "+": lambda: turtle.left(90),
        "-": lambda: turtle.right(90),
    }

    render_pattern(pattern, koch_instructions, line_thickness=2)

 - omega: the axiom
 - expansion_rules: the set of expansion rules
 - expand(times): generate the pattern after the specified number of iterations

<p align="center" width="100%">
    <img src="https://github.com/antigones/LSystems/blob/main/imgs/koch.jpg?raw=true" alt="koch curve">
</p>

**Usage example**

    dragon_curve_omega = "F"
    dragon_curve_expansion_rules = {
      "F": "F+G",
      "G": "F-G",
      "+": "+",
      "-": "-"
    }
    dragon_curve = LSystem(dragon_curve_omega, dragon_curve_expansion_rules)
    dragon_curve_pattern = dragon_curve.expand(times=10)

    dragon_curve_instructions = {
      "F": lambda: turtle.forward(10),
      "G": lambda: turtle.forward(10),
      "+": lambda: turtle.left(90),
      "-": lambda: turtle.right(90),
    }
    render_pattern(dragon_curve_pattern, dragon_curve_instructions, line_thickness=2)

<p align="center" width="100%">
    <img src="https://github.com/antigones/LSystems/blob/main/imgs/dragon_curve.jpg?raw=true" alt="generated dragon curve">
</p>

**References**

- https://www.wikiwand.com/en/L-system
- https://en.wikipedia.org/wiki/L-system
