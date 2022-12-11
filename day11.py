from dataclasses import dataclass


@dataclass
class Monkey:
    id: int
    items: list[int]
    operation: str
    operation_arg: str
    test_nr: int
    monkey_true: int
    monkey_false: int
    nr_of_items_inspected: int = 0

    def do_operation(self, item: int, operation: str, operation_arg: str) -> int | None:
        if operation_arg == "old":
            operation_arg = item
        else:
            operation_arg = int(operation_arg)

        if operation == "+":
            return item + operation_arg
        elif operation == "*":
            return item * operation_arg
        else:
            return None

    def do_turn(self) -> None:
        for item in self.items:
            self.nr_of_items_inspected += 1
            item = self.do_operation(item, self.operation, self.operation_arg) // 3
            if item % self.test_nr == 0:
                monkeys[self.monkey_true].items.append(item)
            else:
                monkeys[self.monkey_false].items.append(item)

        self.items = []

    def do_turn_part_two(self) -> None:
        for item in self.items:
            self.nr_of_items_inspected += 1
            item = self.do_operation(item, self.operation, self.operation_arg)
            item %= max_worry
            if item % self.test_nr == 0:
                monkeys[self.monkey_true].items.append(item)
            else:
                monkeys[self.monkey_false].items.append(item)

        self.items = []


class InputParser:
    def __init__(self, file: str):
        self.file = file
        self.max_worry = 1

    def parse(self) -> list[Monkey]:
        monkey_list = []

        with open(self.file, "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines), 7):
                monkey_id = int(lines[i].strip().replace(":", "").split(" ")[1])
                monkey_items = [
                    int(item_id)
                    for item_id in lines[i + 1].strip().replace(",", "").split(" ")[2:]
                ]
                monkey_operation = lines[i + 2].strip().split(" ")[-2]
                monkey_operation_nr = lines[i + 2].strip().split(" ")[-1]
                test_nr = int(lines[i + 3].strip().split(" ")[-1])
                monkey_true = int(lines[i + 4].strip().split(" ")[-1])
                monkey_false = int(lines[i + 5].strip().split(" ")[-1])
                monkey_list.append(
                    Monkey(
                        monkey_id,
                        monkey_items,
                        monkey_operation,
                        monkey_operation_nr,
                        test_nr,
                        monkey_true,
                        monkey_false,
                    )
                )
                self.max_worry *= test_nr

        return monkey_list
    
    def get_max_worry(self):
        return self.max_worry


if __name__ == "__main__":
    input_parser = InputParser("day11_2.in")
    monkeys = input_parser.parse()
    max_worry = input_parser.get_max_worry()

    i = 1
    while i < 10001:
        if i % 1000 == 0:
            print(f"Round {i}")
        for monkey in monkeys:
            monkey.do_turn_part_two() # change this to monkey.do_turn() for part 1 solution

        for monkey in monkeys:
            if i % 1000 == 0:
                print(f"Monkey #{monkey.id}: {monkey.items}")

        i += 1

    inspections = sorted([monkey.nr_of_items_inspected for monkey in monkeys])

    print(f"Solution: {inspections[-1] * inspections[-2]}")
