import re


class CraneCommand:
    def __init__(self, command_list: list[int]):
        command_list = list(map(lambda x: int(x), command_list))
        self.number_of_crates_to_move = command_list[0]
        self.from_stack = command_list[1] - 1
        self.to_stack = command_list[2] - 1


class CraneProcessor:
    crate_stacks = None
    _item_index = None
    beginning_of_commands = None

    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.process_stacks()

        pass

    def get_or_create_stacks(self):
        if not self.crate_stacks:
            with open(self.input_file_path) as f:
                first_line = f.readline().strip('\n')
                number_of_stacks = range(1, len(first_line), 4)
                self.crate_stacks = [[] for _ in number_of_stacks]
                self._items_index = list(number_of_stacks)
        return self.crate_stacks

    @staticmethod
    def is_capital_letter(char):
        return bool(65 <= ord(char) <= 90)

    def process_stacks(self):
        stacks = self.get_or_create_stacks()
        line_counter = 0
        with open(self.input_file_path) as f:
            for line in f:
                line_counter += 1
                if line[1] == '1':
                    self.beginning_of_commands = line_counter
                    return stacks

                i = 0
                for j in self._items_index:
                    if CraneProcessor.is_capital_letter(line[j]):
                        stacks[i].insert(0, line[j])
                    i += 1
        return stacks

    def process_commands(self):
        with open(self.input_file_path) as f:
            line_counter = 0
            for line in f:
                if line_counter <= self.beginning_of_commands:
                    line_counter += 1
                else:
                    command = CraneCommand(re.findall(r'\d+', line))
                    for i in range(command.number_of_crates_to_move):
                        crate = self.crate_stacks[command.from_stack].pop()  # First, the number of crates to move
                        self.crate_stacks[command.to_stack].append(crate)

    def process_commands_over_9000(self):
        with open(self.input_file_path) as f:
            line_counter = 0
            for line in f:
                if line_counter <= self.beginning_of_commands:
                    line_counter += 1
                else:
                    command = CraneCommand(re.findall(r'\d+', line))
                    crates_to_move = []
                    for i in range(command.number_of_crates_to_move):
                        crates_to_move.insert(0, self.crate_stacks[command.from_stack].pop())  # First, the number of crates to move

                    self.crate_stacks[command.to_stack] = self.crate_stacks[command.to_stack] + crates_to_move

    def show_top_of_stacks(self):
        result = ''
        for i in range(len(self.crate_stacks)):
            crate = self.crate_stacks[i][-1]
            print(f"{i}: [{crate}]")
            result += crate
        print(f'\n{result}')


c = CraneProcessor('input.csv')
c.process_stacks()
c.process_commands_over_9000()
c.show_top_of_stacks()