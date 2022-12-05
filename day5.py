class Solution:
    queues = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    commands = []

    def __init__(self):
        with open("day5_2.in", "r") as file:
            file_lines = file.readlines()

            for line in file_lines:
                if line.strip() and not any(x in line for x in ["move", "1"]):
                    self.queues = self.parse_line_stack(line, self.queues)
                elif "move" in line:
                    el = line.strip().split(" ")
                    self.commands.append((int(el[1]), int(el[3]), int(el[5])))
                else:
                    pass

            for k, v in self.queues.items():
                self.queues[k] = list(reversed(v))

    def parse_line_stack(self, line: str, lists: dict[list[str]]):
        it = 1

        for i in range(0, len(line), 4):
            if line[i + 1] != " ":
                lists[it].append(line[i + 1])
            it += 1

        return lists

    def solve_1(self):
        res = ""

        for n, start_pos, end_pos in self.commands:
            for i in range(n):
                self.queues[end_pos].append(self.queues[start_pos].pop())

        for k, v in self.queues.items():
            if len(v) > 0:
                res += v.pop()

        return res

    def solve_2(self):
        res = ""
        for n, start_pos, end_pos in self.commands:
            moving_stack = self.queues[start_pos][-n:]
            del self.queues[start_pos][-n:]
            self.queues[end_pos].extend(moving_stack)

        for k, v in self.queues.items():
            if len(v) > 0:
                res += v.pop()

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.queues)
    print(solution.commands)
    print(solution.solve_2())
