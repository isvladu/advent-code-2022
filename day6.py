class Solution:
    buffer = ""

    def __init__(self):
        with open("day6_1.in", "r") as file:
            self.buffer = file.readline()

    def marker_is_unique(self, marker: str) -> bool:
        marker_d = {}

        for c in marker:
            if c in marker_d.keys():
                return False
            else:
                marker_d[c] = 1

        return True

    def msg_is_unique(self, msg: str) -> bool:
        msg_d = {}

        for c in msg:
            if c in msg_d.keys():
                return False
            else:
                msg_d[c] = 1

        return True

    def solve_1(self) -> int:
        for i in range(len(self.buffer)):
            if self.marker_is_unique(self.buffer[i : i + 4]):
                return i + 4

    def solve_2(self) -> int:
        for i in range(len(self.buffer)):
            if self.marker_is_unique(self.buffer[i : i + 14]):
                return i + 14


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve_2())
