from __future__ import annotations

directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
tail_diff = {
    (-2, 0): (-1, 0),
    (2, 0): (1, 0),
    (0, -2): (0, -1),
    (0, 2): (0, 1),
    (1, 2): (1, 1),
    (2, 1): (1, 1),
    (2, -1): (1, -1),
    (1, -2): (1, -1),
    (-1, -2): (-1, -1),
    (-2, -1): (-1, -1),
    (-2, 1): (-1, 1),
    (-1, 2): (-1, 1),
    (2, 2): (1, 1),
    (2, -2): (1, -1),
    (-2, -2): (-1, -1),
    (-2, 2): (-1, 1),
}


def calculate_tail_movement(knot: Knot) -> tuple(int, int):
    """Calculates where the child of a knot needs to move based on his parent's movement.

    Args:
        knot (Knot): Knot for which the movement is calculated

    Returns:
        tuple (int, int): Returns the coordinates in a tuple structure (x, y)
    """
    x_diff = knot.parent.x - knot.x
    y_diff = knot.parent.y - knot.y

    return tail_diff[(x_diff, y_diff)]


class Rope:
    """Class representing a rope."""

    def __init__(self, nr_of_knots: int):
        self.head = Head("H")
        self.knots = [Knot("1", self.head)]

        for i in range(2, nr_of_knots):
            last_knot = self.knots[-1]
            self.knots.append(Knot(str(i), last_knot))

        last_knot = self.knots[-1]
        self.tail = Tail(str(nr_of_knots), last_knot)

    def update_state(self, direction: str):
        """Updates the status of the head which triggers the movement of the whole rope.

        Args:
            direction (str): Direction in which the rope needs to move
        """
        self.head.move(direction)

    def __str__(self):
        return f"{str(self.head)}: {str(self.knots)}"

    def __repr__(self):
        return str(self)


class Knot:
    """Class representing a knot in a rope."""

    def __init__(self, name: str, parent: Knot):
        self.name = name
        self.parent = parent
        self.x = 0
        self.y = 0

        if parent is not None:
            parent.child = self

    def move(self, x_diff: int, y_diff: int) -> None:
        """Movement method for a knot.

        Args:
            x_diff (int): Number with whom the x coordinate is incremented
            y_diff (int): Number with whom the y coordinate is incremented
        """
        self.x += x_diff
        self.y += y_diff

        self.notify()

    def notify(self) -> None:
        """Notifies the child that it needs to also calculate his next movement."""
        self.child.update()

    def update(self):
        """Receives an update from the parent and yields a movement."""
        if not self.is_touching():
            x_diff, y_diff = calculate_tail_movement(self)
            self.move(x_diff, y_diff)

    def is_touching(self) -> bool:
        """Checks if the current Knot object is touching with its parent.

        Returns:
            bool: True if the knots are touching, otherwise False
        """
        if -1 <= self.x - self.parent.x <= 1 and -1 <= self.y - self.parent.y <= 1:
            return True
        return False

    def __str__(self):
        return f"{self.name}-x:{self.x},y:{self.y}"

    def __repr__(self):
        return str(self)


class Head(Knot):
    """Class representing the head of a rope."""

    def __init__(self, name: str):
        super().__init__(name, None)

    def move(self, direction: str) -> None:
        """Movement method for the head.

        Args:
            direction (str): Either 'U', 'R', 'D' or 'L' depends on the direction of the movement
        """
        x_1, y_1 = directions[direction]
        self.x += x_1
        self.y += y_1

        self.notify()


class Tail(Knot):
    """Class representing the tail of a rope."""

    def __init__(self, name: str, parent: Knot):
        super().__init__(name, parent)
        self.visited_positions = [(0, 0)]

    def move(self, x_diff: int, y_diff: int) -> None:
        """Movement method for the tail. Compared to the knot movement, it also adds the newly visited positions in a list.

        Args:
            x_diff (int): Number with whom the x coordinate is incremented
            y_diff (int): Number with whom the y coordinate is incremented
        """
        self.x += x_diff
        self.y += y_diff

        if (self.x, self.y) not in self.visited_positions:
            self.visited_positions.append((self.x, self.y))


class Solution:
    def __init__(self):
        self.movements = []

        with open("day9_2.in", "r") as file:
            file_lines = file.readlines()

            for line in file_lines:
                direction, nr = line.strip().split(" ")
                self.movements.append((direction, int(nr)))

    def update_tail_position(self, knot_1: Knot, knot_2: Knot) -> tuple(int, int):
        x_diff = knot_1.x - knot_2.x
        y_diff = knot_1.y - knot_2.y

        return tail_diff[(x_diff, y_diff)]

    # Obsolote method after refactoring for Part 2.
    def solve_1(self, head: Knot, tail: Knot) -> int:
        for direction, nr in self.movements:
            for i in range(nr):
                head.move_with_direction(direction)
                if not head.is_touching(tail):
                    x_diff, y_diff = self.update_tail_position(head, tail)
                    tail.move_with_diff(x_diff, y_diff)

        return len(tail.visited_positions)

    def solve_2(self, rope: Rope) -> int:
        for direction, nr in self.movements:
            for i in range(nr):
                rope.update_state(direction)

        return len(rope.tail.visited_positions)


if __name__ == "__main__":
    rope = Rope(9)
    solution = Solution()

    print(f"Solution: {solution.solve_2(rope)}")
