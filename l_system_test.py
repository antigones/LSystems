from l_system import LSystem


def draw_peano():
    peano_omega = "L"
    peano_expansion_rules = {
                "L": "LFRFL-F-RFLFR+F+LFRFL",
                "R": "RFLFR+F+LFRFL-F-RFLFR",
                "F": "F",
                "+": "+",
                "-": "-"
            }
    peano = LSystem(peano_omega, peano_expansion_rules, 90, 2)
    peano.print_pattern()


def draw_hilbert():
    hilber_omega = "L"
    hilbert_expansion_rules = {
        "L": "+RF-LFL-FR+",
        "R": "-LF+RFR+FL-",
        "F": "F",
        "+": "+",
        "-": "-"
    }

    hilbert = LSystem(hilber_omega, hilbert_expansion_rules, 90, 3)
    hilbert.print_pattern()


def draw_koch():
    koch_omega = "F"
    koch_expansion_rules = {
        "F": "F+F-F-F+F",
        "+": "+",
        "-": "-"
    }

    koch = LSystem(koch_omega, koch_expansion_rules, 90, 3)
    koch.print_pattern()


def draw_fractal_plant():
    fractal_plant_omega = "X"
    fractal_plant_expansion_rules = {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF",
        "[": "[",
        "]": "]",
        "+": "+",
        "-": "-"
    }
    fractal_plant = LSystem(fractal_plant_omega, fractal_plant_expansion_rules, 25, 4)
    fractal_plant.print_pattern()


def draw_cantor():
    cantor_omega = "A"
    cantor_expansion_rules = {
        "A": "ABA",
        "B": "BBB",
    }
    cantor_set = LSystem(cantor_omega, cantor_expansion_rules, 0, 2)
    cantor_set.print_pattern()


def draw_sierpinsky():
    sierpinsky_omega = "F-G-G"
    sierpinsky_expansion_rules = {
        "F": "F-G+F+G-F",
        "G": "GG",
        "+": "+",
        "-": "-"
    }
    sierpinsky = LSystem(sierpinsky_omega, sierpinsky_expansion_rules, 120, 3)
    sierpinsky.print_pattern()


def draw_fractal_tree():
    fractal_tree_omega = "0"
    fractal_tree_expansion_rules = {
        "1": "11",
        "0": "1{0}0",
        "{": "{",
        "}": "}",
    }
    fractal_tree = LSystem(fractal_tree_omega, fractal_tree_expansion_rules, 45, 3)
    fractal_tree.print_pattern()

def draw_dragon_curve():
    dragon_curve_omega = "F"
    dragon_curve_expansion_rules = {
        "F": "F+G",
        "G": "F-G",
        "+": "+",
        "-": "-",
    }
    fractal_tree = LSystem(dragon_curve_omega, dragon_curve_expansion_rules, 90, 10)
    fractal_tree.print_pattern()

def main():
    # draw_fractal_tree()
    # draw_sierpinsky()
    # draw_koch()
    draw_dragon_curve()

if __name__ == '__main__':
    main()
