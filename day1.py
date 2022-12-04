class Solution:
    elf_calories: list[int] = []

    def __init__(self) -> None:
        calorie_sum = 0

        with open("day1_1.in", "r") as file:
            file_lines = file.readlines()

        for line in file_lines:
            stripped_line = line.strip()
            if stripped_line == "":
                self.elf_calories.append(calorie_sum)
                calorie_sum = 0
            else:
                calorie_sum += int(stripped_line)

        self.elf_calories.append(calorie_sum)
        self.elf_calories = sorted(self.elf_calories, reverse=True)

    def get_max_calories(self):
        return self.elf_calories[0]

    def get_top_three_calories(self):
        return self.elf_calories[0] + self.elf_calories[1] + self.elf_calories[2]


if __name__ == "__main__":
    solution = Solution()
    print(solution.get_top_three_calories())
