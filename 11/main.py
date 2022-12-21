class Monkey:
    def __init__(self, items, operation, divider, true_monkey, false_monkey):
        self.items = items
        self.divisible_by = divider
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.operation = self.parse_operation(operation)

    def parse_operation(self, line: str):
        components = str.split(" ")

        def monkey_op(s, old, new):
            multiplier = 1
            if components[-1].isdigit():
                multiplier = int(components[-1])
            elif components == 'new':
                multiplier = new
            elif components[-1] == 'old'


        return


def parse_monkey_activities(input_path):
    with open(input_path) as f:
        for line in f:
