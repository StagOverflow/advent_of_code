import re


class Command:
    def __init__(self, cmd: list):
        self.utility = cmd[1]
        self.arguments = None if len(cmd) <= 2 else cmd[2:]


class FileExplorer:
    def __init__(self):
        self.current_dir = None
        self.previous_dirs = []
        self.dir_sizes = {}
        self.dirs_to_backfill = {}

    def process(self, command: Command, output_buffer: list):
        if command.utility == 'cd':
            self._process_cd(command.arguments)
        elif command.utility == 'ls':
            self._process_ls(output_buffer)

    def _process_cd(self, directory: list):
        directory = directory[0]

        if directory == '..':
            self.current_dir = self.previous_dirs[-1]
            self.previous_dirs.pop()
        elif directory == '.':
            pass
        elif directory == '/':
            self.current_dir = '/'
            self.previous_dirs = []
        else:
            self.previous_dirs.append(self.current_dir)
            self.current_dir = directory

    def _process_ls(self, output):
        dir_size = 0
        backfills = []

        if self.current_dir == '/':
            return 0

        for line in output:
            if re.search('^dir', line):
                backfills.append(line.split(' ')[1])
            else:
                dir_size += int(re.search(r'\d+', line).group())

        self.dir_sizes[self.current_dir] = dir_size

        #  We need to come back to fill the size of the missing directories
        #  but we'll have to walk the dict keys in reverse for that

        for d in backfills:
            if d in self.dirs_to_backfill:
                self.dirs_to_backfill[d].append(self.current_dir)
            else:
                self.dirs_to_backfill[d] = [self.current_dir]

    def backfill_sizes(self):
        for dir_to_count in reversed(sorted(self.dirs_to_backfill.keys())):
            for dir_missing_a_size in self.dirs_to_backfill[dir_to_count]:
                self.dir_sizes[dir_missing_a_size] = self.dir_sizes[dir_to_count]

    def total_directory_size(self, max_valid_size=10000):
        total = 0
        for v in self.dir_sizes.values():
            total = total + v if v <= max_valid_size else total

        return total


def compute_size(input_path):
    explorer = FileExplorer()

    with open(input_path) as terminal:
        current_command = 'start'
        output_buffer = []
        for line in terminal:
            if current_command == 'start':
                current_command = Command(line.strip().split(' '))
            elif line[0] == '$':
                explorer.process(current_command, output_buffer)  # We have collected the full output for the previous command
                current_command = Command(line.strip().split(' '))
            else:
                output_buffer.append(line.strip())
        explorer.backfill_sizes()

    return explorer.total_directory_size()


print(compute_size('sample.txt'))
