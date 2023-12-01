import re


class Command:
    def __init__(self, cmd: list):
        self.utility = cmd[1]
        self.arguments = None if len(cmd) <= 2 else cmd[2:]


class FileExplorer:
    def __init__(self):
        self.current_dir = '/'
        self.previous_dirs = []
        self.dir_sizes = {'/': 0}
        self.dirs_to_backfill = {}

    def process(self, command: Command, output_buffer: list):
        if command.utility == 'cd':
            self._process_cd(command.arguments)
        elif command.utility == 'ls':
            self._process_ls(output_buffer)

    def _process_cd(self, directory: list):
        directory = directory[0]

        if directory == '..':
            self.dir_sizes[self.previous_dirs[-1]] = self.dir_sizes[self.previous_dirs[-1]] + self.dir_sizes[self.current_dir]
            self.current_dir = self.previous_dirs[-1]
            self.previous_dirs.pop()
        elif directory == '/':
            self.current_dir = '/'
            self.previous_dirs = []
        else:
            self.previous_dirs.append(self.current_dir)
            if self.previous_dirs[-1] == '/':
                self.current_dir = self.previous_dirs[-1] + directory
            else:
                self.current_dir = self.previous_dirs[-1] + '/' + directory

    def _process_ls(self, output):
        dir_size = 0
        backfills = []

        for line in output:
            if re.search('^dir', line):
                backfills.append(line.split(' ')[1])
            else:
                dir_size += int(re.search(r'\d+', line).group())

        self.dir_sizes[self.current_dir] = dir_size

    def total_directory_size(self, max_valid_size=100000):
        total = 0
        for v in self.dir_sizes.values():
            total = total + v if v <= max_valid_size else total

        return total

    def find_smallest_to_del(self, file_system_size=70000000, update_size=30000000):
        sorted_dict = dict(sorted(self.dir_sizes.items(), key=lambda item: item[1]))
        space_left = file_system_size - self.dir_sizes['/']
        #
        # if update_size < space_left:
        #     return None

        for k, v in sorted_dict.items():
            if space_left + v >= update_size:
                return k, v

# need 24825975
def compute_size(input_path, explorer: FileExplorer):
    output_buffer = []

    with open(input_path) as terminal:
        current_command = 'start'

        for line in terminal:
            if current_command == 'start':
                current_command = Command(line.strip().split(' '))
            elif line[0] == '$':
                explorer.process(current_command, output_buffer)  # We have collected the full output for the previous command
                current_command = Command(line.strip().split(' '))
                output_buffer = []
            else:
                output_buffer.append(line.strip())

        # We need to bring it back to the top at the very end
        explorer.process(current_command, output_buffer)
        while explorer.current_dir != '/':
            explorer.process(Command(['$', 'cd', '..']), [])

    return explorer.total_directory_size()


explorer = FileExplorer()
print(compute_size('input.txt', explorer))
#print(f"You should delete directory {explorer.find_smallest_to_del(file_system_size=3000, update_size=70)}")
print(f"You should delete directory {explorer.find_smallest_to_del()}")
