from pprint import pprint


class Position:
    def __init__(self, x: str, y: str, value: int):
        self.x = x
        self.y = y
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.value == other.value

    def __hash__(self):
        return hash((self.x, self.y, self.value))

    def __str__(self):
        return f"Position(x:{self.x},y:{self.y},value:{self.value})"

    def __repr__(self):
        return str(self)


class InputParser:
    def __init__(self, file: str) -> None:
        self.file = file

    def parse(self) -> tuple[list[list[str]], Position, Position]:
        grid = []

        with open(self.file, "r") as f:
            for line in f:
                grid.append(list(line.rstrip()))

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col == "S":
                    grid[row_idx][col_idx] = 0
                    start = Position(row_idx, col_idx, 0)
                elif col == "E":
                    grid[row_idx][col_idx] = 25
                    end = Position(row_idx, col_idx, 25)
                else:
                    grid[row_idx][col_idx] = ord(col) - ord("a")

        return grid, start, end


class Solution:
    def __init__(
        self,
        grid: list[list[str]],
        start: Position,
        end: Position,
    ) -> None:
        self.grid = grid
        self.start = start
        self.end = end
        self.graph = {}

    def create_graph_util(self, position: Position) -> None:
        self.graph[position] = []

        if position.x - 1 >= 0 and (
            position.value - 1 <= self.grid[position.x - 1][position.y] <= position.value + 1
        ):
            self.graph[position].append(
                Position(
                    position.x - 1, position.y, self.grid[position.x - 1][position.y]
                )
            )

        if position.x + 1 < len(self.grid) and (
            position.value - 1 <= self.grid[position.x + 1][position.y] <= position.value + 1
        ):
            self.graph[position].append(
                Position(
                    position.x + 1, position.y, self.grid[position.x + 1][position.y]
                )
            )

        if position.y - 1 >= 0 and (
            position.value - 1 <= self.grid[position.x][position.y - 1] <= position.value + 1
        ):
            self.graph[position].append(
                Position(
                    position.x, position.y - 1, self.grid[position.x][position.y - 1]
                )
            )

        if position.y + 1 < len(self.grid[0]) and (
            position.value - 1 <= self.grid[position.x][position.y + 1] <= position.value + 1
        ):
            self.graph[position].append(
                Position(
                    position.x, position.y + 1, self.grid[position.x][position.y + 1]
                )
            )

    def create_graph(self) -> None:
        for row_idx, row in enumerate(self.grid):
            for col_idx, col in enumerate(row):
                self.create_graph_util(Position(row_idx, col_idx, col))

    def bfs(self) -> int | None:
        visited = []
        queue = [[self.start]]

        if self.start == self.end:
            return 0

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                neighbours = self.graph[node]

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == self.end:
                        return len(new_path)

                visited.append(node)

        print(f"{node} - {new_path}")
        return None


if __name__ == "__main__":
    grid, start, end = InputParser("day12_2.in").parse()
    solution = Solution(grid, start, end)
    solution.create_graph()
    # pprint(solution.graph)
    print(solution.bfs() - 1)
