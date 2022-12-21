import operator
import re


class Monkey:
    def __init(self):
        self.items = None
        self.divider = None
        self.inspect = None
        self.true_monkey = None
        self.false_monkey = None

    def parse_operation(self, line: str):
        components = line.split(" ")

        operations = {'*': operator.mul,
                      '+': operator.add,
                      '-': operator.sub,
                      '//': operator.ifloordiv}

        def inspect(old_worry_level: int):
            if components[-1].isdigit():
                right_hand_side = int(components[-1])
            elif components[-3] == 'old':
                right_hand_side = old_worry_level
            else:
                raise Exception('Unrecognized worry level')

            return operations[components[-2]](old_worry_level, right_hand_side)

        return inspect

    # Lucky us, all monkeys have the same worry check function :)
    def _throw_check(self, worry_level):
        return (worry_level // self.divider) == 0

    def throw(self, worry_level):
        return self.true_monkey if self._throw_check(worry_level) else self.false_monkey

    def __str__(self):
        return f"""\nitems: {self.items}\n
               divider: {self.divider}\n
               true_monkey: {self.true_monkey}\n
               false_monkey: {self.false_monkey}"""


def get_numbers_from_string(items: str):
    return list(map(lambda x: int(x), re.findall(r'\b\d+\b', items)))


def parse_monkey_activities(input_path):
    monkeys = []
    current_monkey = None
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            words = line.split(' ')
            if not (line.replace(" ", "")):  # we're done with the current monkey
                monkeys.append(current_monkey)
            elif words[0] == 'Monkey':
                current_monkey = Monkey()
            elif words[0] == 'Starting':
                current_monkey.items = get_numbers_from_string(line)
            elif words[0] == 'Operation:':
                current_monkey.inspect = current_monkey.parse_operation(line)
            elif words[0] == 'Test:':
                current_monkey.divider = get_numbers_from_string(line)[0]
            elif words[1] == 'true:':
                current_monkey.true_monkey = get_numbers_from_string(line)[0]
            elif words[1] == 'false:':
                current_monkey.false_monkey = get_numbers_from_string(line)[0]

            else:
                raise Exception(f'Unrecognized input: {line}')

    monkeys.append(current_monkey)
    return monkeys


processed_monkeys = parse_monkey_activities('input.txt')

i = 0

# Monkey parsing is working
# Monkey function is working
for ape in processed_monkeys:
    print(f"Monkey {i}:")
    print(ape)
    print(ape.inspect(2))
    i += 1

def play_keep_away(monkeys):
    for monkey in monkeys:
        while monkey.items:
            monkey