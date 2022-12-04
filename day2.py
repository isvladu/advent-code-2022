class Solution:
    strategy_guide: list[(str, str)] = []

    def __init__(self):
        with open("day2_1.in", "r") as file:
            file_lines = file.readlines()

        for file in file_lines:
            stripped_line = file.strip()
            (a, b) = stripped_line.split(" ")
            self.strategy_guide.append((a, b))

    def calculate_shape_score(self, shape: str):
        return ord(shape) - ord("W")

    def calculate_round_score(self, opp: str, me: str):
        if ord(me) - ord(opp) == 23:
            return 3 + self.calculate_shape_score(me)
        elif ord(me) - ord(opp) == 24 or ord(me) - ord(opp) == 21:
            return 6 + self.calculate_shape_score(me)
        else:
            return self.calculate_shape_score(me)

    def solve1(self):
        score_sum = 0

        for (a, b) in self.strategy_guide:
            score_sum += self.calculate_round_score(a, b)

        return score_sum
    
    def calculate_round_score_2(self, a, b):
        if b == 'X':
            return ord(a) % 3 + 1
        elif b == 'Y':
            return 4 + (ord(a) + 1) % 3
        else:
            return 7 + (ord(a) + 2) % 3
        
    def solve2(self):
        score_sum = 0
        
        for (a, b) in self.strategy_guide:
            score_sum += self.calculate_round_score_2(a, b)
            
        return score_sum


if __name__ == "__main__":
    solution = Solution()
    print(f"Part 1: {solution.solve1()} - Part 2: {solution.solve2()}")