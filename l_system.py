from turtle import *

class LSystem:
    
    def walk_F(self):
        return forward(self.step_size)

    def walk_L(self):
        return left(self.angle)

    def walk_R(self):
        return right(self.angle)

    def push_pos_angle(self):
        return self.stack.append((pos(),heading()))

    def pop_pos_angle(self):
        pos, heading = self.stack.pop()
        penup()
        setposition(pos)
        setheading(heading)
        pendown()

    def push_pos_set_angle(self):
        self.stack.append((pos(),heading()))
        setheading(45)
    
    def pop_pos_set_angle(self):
        pos, _ =  self.stack.pop()
        penup()
        setposition(pos)
        setheading(-45)
        pendown()

    def move_forward(self):
        penup()
        setx(xcor()+self.step_size)
        pendown()

    def draw_tip(self):
        return forward(self.step_size//2)

    def print_pattern(self):
        draw_pattern = {
            "F":self.walk_F,
            "+":self.walk_L,
            "-":self.walk_R,
            "[":self.push_pos_angle,
            "]":self.pop_pos_angle,
            "A":self.walk_F,
            "B":self.move_forward,
            "G":self.walk_F,
            "0":self.draw_tip,
            "1":self.walk_F,
            "{":self.push_pos_set_angle,
            "}":self.pop_pos_set_angle,
        }
        speed(10)
        pensize(self.line_thickness)
        color('red', 'white')
        begin_fill()
        for chr in self.end_pattern:
            if chr in draw_pattern:
                draw_pattern[chr]()   
        end_fill()
        done()

    def expand(self, starting_pattern:str, times:int):
        for i in range(times):
            end_pattern = ""
            for chr in starting_pattern:
                end_pattern += self.expansion_rules[chr]
            starting_pattern = end_pattern           
        return starting_pattern

    def __init__(self, omega, expansion_rules, angle, times):
        self.line_thickness = 2
        self.step_size = 10
        self.omega = omega
        self.expansion_rules = expansion_rules
        self.angle = angle
        self.times = times
        self.stack = []
        self.end_pattern = self.expand(self.omega,times)