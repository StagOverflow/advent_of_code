import operator
import re

class Monkey:
    # def __init__(self, items, operation, divider, true_monkey, false_monkey):
        # self.items = items
        # self.divisible_by = divider
        # self.true_monkey = true_monkey
        # self.false_monkey = false_monkey
        # self.operation = self.parse_operation(operation)

    def parse_operation(self, line: str):
        components = str.split(" ")
        operations = {'*': operator.mul,
                      '+': operator.add,
                      '-': operator.sub,
                      '//': operator.ifloordiv
        }

        def monkey_op(self, old, new):
            right_hand_side = 1
            if components[-1].isdigit():
                right_hand_side = int(components[-1])
            elif components[-1] == 'new':
                right_hand_side = new
            elif components[-1] == 'old':
                right_hand_side = old

            return operations[components[-2]](old, right_hand_side)

        return monkey_op

def get_numbers_from_string(items: str):
    return re.findall(r'\b\d+\b', items)


def parse_monkey_activities(input_path):
    monkeys = []
    current_monkey = None
    with open(input_path) as f:
        for line in f:
            line = line.rstrip()
            words = line.split()
            if words[0] == 'Monkey':
                current_monkey = Monkey()
            elif words[0] == 'Starting':
                current_monkey.items = get_numbers_from_string(line)
            elif words[0] == 'Operation':
                current_monkey.operation = current_monkey.parse_operation(line)
            elif words[0] == 'Test':
                current_monkey.divider = get_numbers_from_string(line)[0]
            elif words[1] == 'true':
                current_monkey.true_monkey = get_numbers_from_string(line)[0]
            elif words[1] == 'false':
                current_monkey.false_monkey = get_numbers_from_string(line)
            else: # else we're done with the current monkey
                monkeys.append(current_monkey)



