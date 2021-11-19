from l_system import LSystem

peano_omega = "L"
peano_expansion_rules = {
            "L": "LFRFL-F-RFLFR+F+LFRFL",
            "R": "RFLFR+F+LFRFL-F-RFLFR",
            "F":"F",
            "+":"+",
            "-":"-"
        }
peano = LSystem(peano_omega,peano_expansion_rules,90,2)
# peano.print_pattern()

hilber_omega = peano_omega
hilbert_expansion_rules = {
    "L":"+RF-LFL-FR+",
    "R":"-LF+RFR+FL-",
    "F":"F",
    "+":"+",
    "-":"-"
}

hilbert = LSystem(hilber_omega, hilbert_expansion_rules, 90, 3)
# hilbert.print_pattern()

koch_omega = "F"
koch_expansion_rules = {
    "F":"F+F-F-F+F",
    "+":"+",
    "-":"-"
}

koch = LSystem(koch_omega, koch_expansion_rules, 90, 3)
# koch.print_pattern()

fractal_plant_omega = "X"
fractal_plant_expansion_rules = {
    "X":"F+[[X]-X]-F[-FX]+X",
    "F":"FF",
    "[":"[",
    "]":"]",
    "+":"+",
    "-":"-"
}
fractal_plant = LSystem(fractal_plant_omega, fractal_plant_expansion_rules, 25, 4)
fractal_plant.print_pattern()