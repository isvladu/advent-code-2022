class Solution:
    rucksacks: list[str] = []

    def __init__(self):
        with open("day3_1.in", "r") as file:
            file_lines = file.readlines()

        for line in file_lines:
            self.rucksacks.append(line.strip())

    def get_priority(self, item: str):
        if ord(item) < 91:
            return ord(item) - 38
        else:
            return ord(item) - 96

    def find_error(self, rucksack: str):
        rucksack_1, rucksack_2 = (
            rucksack[: len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )

        for index in range(len(rucksack) // 2):
            if rucksack_1[index] in rucksack_2:
                return rucksack_1[index]
            elif rucksack_2[index] in rucksack_1:
                return rucksack_2[index]
            else:
                continue

        return "Error"

    def find_common_item(self, elf_1: str, elf_2: str, elf_3: str):
        elf_group = [elf_1, elf_2, elf_3]
        common_item = set.intersection(*map(set, elf_group))

        return list(common_item)[0]

    def solve_1(self):
        priority_sum = 0

        for rucksack in self.rucksacks:
            priority_sum += self.get_priority(self.find_error(rucksack))

        return priority_sum

    def solve_2(self):
        priority_sum = 0

        for index in range(len(self.rucksacks) // 3):
            priority_sum += self.get_priority(
                self.find_common_item(
                    self.rucksacks[3*index],
                    self.rucksacks[3*index + 1],
                    self.rucksacks[3*index + 2],
                )
            )

        return priority_sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve_2())
