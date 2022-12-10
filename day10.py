class CathodeRayTube:
    def __init__(self):
        self.x: int = 1
        self.cycle: int = 0
        self.signal_sum = 0
        self.screen = []

    def run(self, file: str):
        with open(file, "r") as f:
            for line in f:
                instruction = line.rstrip().split()
                if instruction[0] == "noop":
                    self.noop()
                elif instruction[0] == "addx":
                    self.addx(int(instruction[1]))

    def addx(self, value: int):
        for _ in range(2):
            self.noop()

        self.x += value

    def noop(self):
        self.screen.append("") if self.cycle % 40 == 0 else None
        self.screen[-1] += (
            "#" if self.x - 1 <= self.cycle % 40 <= self.x + 1 else "."
        )

        self.cycle += 1
        self.signal_sum += self.cycle * self.x if (self.cycle - 20) % 40 == 0 else 0
        
    def show_screen(self):
        return "\n".join(self.screen)


if __name__ == "__main__":
    crt = CathodeRayTube()
    crt.run("day10_2.in")
    print(f"Part 1: {crt.signal_sum}")
    print(f"Part 2:\n{crt.show_screen()}")
