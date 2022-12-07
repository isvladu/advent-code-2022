class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"File({self.name}, {self.size})"

    def __repr__(self):
        return self.__str__()


class Directory:
    def __init__(self, name: str, parent_dir=None):
        self.name = name
        self.parent_dir = parent_dir
        self.contents = []

    def add(self, item) -> None:
        self.contents.append(item)

    def get_dir(self, name: str):
        for item in self.contents:
            if item.name == name and isinstance(item, Directory):
                return item

        raise Exception(f"Directory '{name}' not found!")

    def get_size(self):
        total_size = 0

        for item in self.contents:
            if isinstance(item, File):
                total_size += item.size
            else:
                total_size += item.get_size()

        return total_size

    def __str__(self):
        return f"Directory({self.name}, {self.contents})"

    def __repr__(self):
        return self.__str__()


class Solution:
    root_dir: Directory = Directory("/")
    total_sum: int = 0
    directory_sizes = []

    def __init__(self):
        with open("day7_2.in", "r") as file:
            current_dir = self.root_dir
            file_lines = file.readlines()[1:]

            for line in file_lines:
                line = line.strip().split(" ")

                try:
                    arg = line[2]
                except IndexError:
                    arg = None

                if line[0] == "$":
                    current_dir = self.parse_command(current_dir, line[1], arg)
                elif line[0] == "dir":
                    current_dir.add(Directory(line[1], current_dir))
                else:
                    current_dir.add(File(size=int(line[0]), name=line[1]))

    def parse_command(
        self, current_dir: Directory, command: str, arg: str
    ) -> Directory:
        if command == "cd" and arg == "..":
            return current_dir.parent_dir
        elif command == "cd":
            return current_dir.get_dir(arg)
        else:
            return current_dir

    def solve_1(self, dir):
        for item in dir.contents:
            if isinstance(item, Directory):
                if item.get_size() < 100000:
                    self.total_sum += item.get_size()
                self.solve_1(item)

    def solve_2(self, dir):
        for item in dir.contents:
            if isinstance(item, Directory):
                self.directory_sizes.append(item.get_size())
                self.solve_2(item)


if __name__ == "__main__":
    solution = Solution()
    free_space = 70000000 - solution.root_dir.get_size()
    solution.solve_2(solution.root_dir)
    for size in sorted(solution.directory_sizes):
        if size > 30000000 - free_space:
            print(size)
            break
