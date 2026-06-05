class LSystem:
    def __init__(self, omega, expansion_rules):
        self.omega = omega
        self.expansion_rules = expansion_rules

    def expand(self, starting_pattern=None, times=1):
        if starting_pattern is None:
            starting_pattern = self.omega

        pattern = starting_pattern
        for _ in range(times):
            next_pattern = []
            for chr in pattern:
                next_pattern.append(self.expansion_rules.get(chr, chr))
            pattern = "".join(next_pattern)

        return pattern
