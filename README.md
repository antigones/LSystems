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
 - angle: the angle to turn when turning left or right
 - time:  the number of iteration

<p align="center" width="100%">
    <img src="https://github.com/antigones/LSystems/blob/main/imgs/koch.jpg?raw=true" alt="koch curve">
</p>

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
    
<p align="center" width="100%">
    <img src="https://github.com/antigones/LSystems/blob/main/imgs/plant.jpg?raw=true" alt="generated plant">
</p>

    dragon_curve_omega = "F"
    fractal_plant_expansion_rules = {
      "F":"F+G",
      "G":"F-G",
      "+":"+",
      "-":"-"
    }
    dragon_curve = LSystem(dragon_curve_omega, fractal_plant_expansion_rules, 90, 10)
    dragon_curve.print_pattern()

<p align="center" width="100%">
    <img src="https://github.com/antigones/LSystems/blob/main/imgs/dragon_curve.jpg?raw=true" alt="generated dragon curve">
</p>

**References**

- https://www.wikiwand.com/en/L-system
- https://en.wikipedia.org/wiki/L-system
