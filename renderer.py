from turtle import (
    speed,
    pensize,
    color,
    begin_fill,
    end_fill,
    done,
)


def render_pattern(pattern, draw_instructions, line_thickness=2):
    """Renderizza `pattern` usando la mappa `draw_pattern` (symbol -> callable).

    draw_pattern deve essere un dizionario che mappa singoli caratteri
    a funzioni che eseguono le azioni di disegno (ad es. funzioni Turtle).
    """
    speed(10)
    pensize(line_thickness)
    color("red", "white")
    begin_fill()
    for chr in pattern:
        action = draw_instructions.get(chr)
        if action:
            action()
    end_fill()
    done()


def render_parametric_pattern(pattern, draw_instructions, line_thickness=2):
    """Renderizza un pattern parametric usando una mappa symbol -> callable(value)."""
    speed(10)
    pensize(line_thickness)
    color("red", "white")
    begin_fill()
    for symbol, value in pattern:
        action = draw_instructions.get(symbol)
        if action:
            action(value)
    end_fill()
    done()
