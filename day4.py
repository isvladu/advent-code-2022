class Solution:
    elf_pairs = []

    def __init__(self):
        with open("day4_2.in", "r") as file:
            file_lines = file.readlines()

            for line in file_lines:
                pair = line.strip().split(",")
                first_elf = list(
                    range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1]) + 1)
                )
                second_elf = list(
                    range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1]) + 1)
                )
                self.elf_pairs.append((first_elf, second_elf))

    def is_assign_contained(self, pair):
        return all(i in pair[0] for i in pair[1]) or all(i in pair[1] for i in pair[0])

    def is_overlapped(self, pair):
        start_1, stop_1 = pair[0][0], pair[0][-1]
        start_2, stop_2 = pair[1][0], pair[1][-1]

        if start_1 > stop_2 or stop_1 < start_2:
            return False
        return True

    def solve_1(self):
        counter = 0
        for pair in self.elf_pairs:
            if self.is_assign_contained(pair):
                counter += 1

        return counter

    def solve_2(self):
        counter = 0
        for pair in self.elf_pairs:
            if self.is_overlapped(pair):
                counter += 1

        return counter


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve_2())
