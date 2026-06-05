class ParametricLSystem:
    def __init__(self, omega, expansion_rules):
        """
        omega: A list of tuples representing the initial state, e.g., [("A", 0)]
        expansion_rules: A dictionary where keys are symbols and values are lambdas
                         that accept the current value and return a list of tuples.
        """
        self.omega = omega
        self.expansion_rules = expansion_rules

    def expand(self, times=1):
        pattern = self.omega
        
        for _ in range(times):
            next_pattern = []
            for symbol, value in pattern:
                # If the symbol has an expansion rule, execute it passing its current value
                if symbol in self.expansion_rules:
                    rule_function = self.expansion_rules[symbol]
                    new_elements = rule_function(value)
                    next_pattern.extend(new_elements)
                else:
                    # If no rule exists, keep the symbol and its value unchanged
                    next_pattern.append((symbol, value))
            pattern = next_pattern

        return pattern