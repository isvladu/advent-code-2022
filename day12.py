from queue import Queue


class Node:
    def __init__(self, pos: tuple[int, int], elev: int) -> None:
        self.pos = pos
        self.elev = elev
        self.paths = []

    def add_path(self, path) -> None:
        if path not in self.paths:
            self.paths.append(path)

    def generate_paths(self, hmap) -> None:
        x, y = self.pos
        possible_paths = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

        for path in possible_paths:
            if path in hmap and hmap[path].elev <= self.elev + 1:
                self.paths.append(path)

    def __str__(self):
        return f"Node(pos={self.pos},elev={self.elev})"

    def __repr__(self):
        return str(self)


class Solution:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def bfs(self, start_pos: tuple[int, int]) -> tuple[bool, int]:
        # https://www.redblobgames.com/pathfinding/a-star/introduction.html
        # Simple breadth-first search (BFS)

        frontier = Queue()
        frontier.put(start_pos)
        came_from = dict()
        came_from[start_pos] = None

        while not frontier.empty():
            current_pos = frontier.get()

            if current_pos == self.end_pos:
                break

            for next_position in self.height_map[current_pos].paths:
                if next_position not in came_from:
                    frontier.put(next_position)
                    came_from[next_position] = current_pos

        current_pos = self.end_pos
        path = []

        while current_pos != start_pos:
            path.append(current_pos)
            try:
                current_pos = came_from[current_pos]
            except KeyError:
                return False, came_from

        return True, len(path)

    def parse(self) -> None:
        with open(self.filename, "r") as f:
            grid = [line.rstrip() for line in f]

        self.height_map = {}

        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                if c == "S":
                    self.start_pos = (x, y)
                    elevation = 0
                elif c == "E":
                    self.end_pos = (x, y)
                    elevation = 25
                else:
                    elevation = ord(c) - 97
                self.height_map[(x, y)] = Node((x, y), elevation)

        for height in self.height_map:
            self.height_map[height].generate_paths(self.height_map)

    def solve(self) -> tuple[int, list[int]]:
        part_2_paths = []
        visited = set()

        for coord in self.height_map:
            if coord not in visited:
                if self.height_map[coord].elev == 0:
                    found, result = self.bfs(coord)
                    if found:
                        part_2_paths.append(result)
                    else:
                        for c in result:
                            visited.add(c)
                    if coord == self.start_pos:
                        part_1 = result

        return part_1, part_2_paths


if __name__ == "__main__":
    solution = Solution("day12_2.in")
    solution.parse()
    part_1, part_2 = solution.solve()
    print(f"Part 1: {part_1}, Part 2: {min(part_2)}")
