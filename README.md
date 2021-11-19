# L-System

A class to draw curves expressed as L-System production rules

    koch_omega = "F"
    koch_expansion_rules = { 
    "F":"F+F-F-F+F",
    "+":"+",
    "-":"-"
    }
    koch = LSystem(koch_omega, koch_expansion_rules, 90, 3)
    koch.print_pattern()

 - omega: the axiom 
 - expansion_rules: the set of expansion rules 
 - angle: the angle to turn 
 - time:  the number of iteration

**Usage example**

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
