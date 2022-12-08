class Solution:
    def __init__(self):
        self.grid = []

        with open("day8_2.in", "r") as file:
            file_lines = file.readlines()

            for line in file_lines:
                line = line.strip()
                self.grid.append(list(map(int, list(line))))

    def is_visible(self, x, y):
        row = self.grid[x]
        col = [self.grid[i][y] for i in range(len(self.grid))]

        left = row[0:y]
        right = row[y + 1 : None]
        up = col[0:x]
        down = col[x + 1 : None]
        value = self.grid[x][y]

        left_bool = True
        right_bool = True
        up_bool = True
        down_bool = True

        for tree in left:
            if tree >= value:
                left_bool = False
                break
        for tree in right:
            if tree >= value:
                right_bool = False
                break
        for tree in up:
            if tree >= value:
                up_bool = False
                break
        for tree in down:
            if tree >= value:
                down_bool = False
                break

        return left_bool or right_bool or up_bool or down_bool

    def calculate_scenic_score(self, x, y):
        scenic_score_dict = {"up": 0, "left": 0, "right": 0, "down": 0}

        row = self.grid[x]
        col = [self.grid[i][y] for i in range(len(self.grid))]

        left = reversed(row[0:y])
        right = row[y + 1 : None]
        up = reversed(col[0:x])
        down = col[x + 1 : None]
        value = self.grid[x][y]

        for tree in left:
            scenic_score_dict["left"] += 1
            if tree >= value:
                break
        for tree in right:
            scenic_score_dict["right"] += 1
            if tree >= value:
                break
        for tree in up:
            scenic_score_dict["up"] += 1
            if tree >= value:
                break
        for tree in down:
            scenic_score_dict["down"] += 1
            if tree >= value:
                break

        return (
            scenic_score_dict["up"]
            * scenic_score_dict["down"]
            * scenic_score_dict["right"]
            * scenic_score_dict["left"]
        )

    def solve_1(self):
        trees_visible = 0

        for idx, row in enumerate(self.grid):
            for idy, col in enumerate(row):
                if (
                    idx == 0
                    or idx == len(self.grid) - 1
                    or idy == 0
                    or idy == len(self.grid) - 1
                    or self.is_visible(idx, idy)
                ):
                    trees_visible += 1

        return trees_visible

    def solve_2(self):
        max_scenic_score = 0

        for idx, row in enumerate(self.grid):
            for idy, col in enumerate(row):
                scenic_score = self.calculate_scenic_score(idx, idy)
                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score

        return max_scenic_score


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve_2())
