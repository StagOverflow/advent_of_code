import operator
import re


class Monkey:
    def __init__(self):
        self.items = None
        self.divider = None
        self._inspect = None
        self.true_monkey = None
        self.false_monkey = None
        self.inspected = 0
        self.id = None

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

            return operations[components[-2]](old_worry_level, right_hand_side) // 3

        return inspect


    # Lucky us, all monkeys have the same worry check function :)

    def _throw_check(self, worry_level):
        return (worry_level // self.divider) == 0

    def inspect_and_throw_first(self):
        print(f"Throwing item: {self.items[0]} ")

        inspected_worry = self._inspect(self.items[0])
        not_thrown_worry = inspected_worry // 3

        thrown_item = self.items.pop(0)
        selected_monkey = self.true_monkey if self._throw_check(not_thrown_worry) else self.false_monkey
        selected_monkey.items.append(thrown_item)

        self.inspected += 1
        print(f"Item thrown to monkey {selected_monkey.id} with final worry level: {not_thrown_worry}")


    def __str__(self):
        return f"""\nitems: {self.items}\n
               divider: {self.divider}\n"""


def get_numbers_from_string(items: str):
    return list(map(lambda x: int(x), re.findall(r'\b\d+\b', items)))


def parse_monkey_activities(input_path):
    monkeys = [Monkey() for _ in range(8)]
    monkey_num = 0
    current_monkey = monkeys[0]

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            words = line.split(' ')
            if not (line.replace(" ", "")):  # we're done with the current monkey
                monkey_num += 1
                current_monkey = monkeys[monkey_num]
            elif words[0] == 'Monkey':
                current_monkey.id = get_numbers_from_string(line)
            elif words[0] == 'Starting':
                current_monkey.items = get_numbers_from_string(line)
            elif words[0] == 'Operation:':
                current_monkey._inspect = current_monkey.parse_operation(line)
            elif words[0] == 'Test:':
                current_monkey.divider = get_numbers_from_string(line)[0]
            elif words[1] == 'true:':
                current_monkey.true_monkey = monkeys[get_numbers_from_string(line)[0]]
            elif words[1] == 'false:':
                current_monkey.false_monkey = monkeys[get_numbers_from_string(line)[0]]

            else:
                raise Exception(f'Unrecognized input: {line}')
    return monkeys


processed_monkeys = parse_monkey_activities('input.txt')

# i = 0

# Monkey parsing is working
# Monkey function is working
# for ape in processed_monkeys:
#     print(f"Monkey {i}:")
#     print(ape)
#     print(ape._inspect(23))
#     i += 1


def play_keep_away(monkeys, rounds=20):
    for r in range(rounds):
        for monkey in monkeys:
            for _ in monkey.items:
                monkey.inspect_and_throw_first()

    ranking = [monkey.inspected for monkey in monkeys]
    ranking.sort()

    return ranking[0] * ranking[1]

processed_monkeys[0].inspected

result = play_keep_away(processed_monkeys)

print(f"Monkey Business: {result}")
