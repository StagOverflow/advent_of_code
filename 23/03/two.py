def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'


class SchematicBuffer:

    def __init__(self, row_size=140, row_count=140):
        self.symbol_cache = {}
        self.current_above_part_num = (0, set())
        self.current_below_part_num = (0, set())
        self.total = 0
        self.incoming_line = []
        self.row_size = row_size
        self.top_line = []
        self.push_count = -1
        self.row_count = row_count

    def __repr__(self):
        return f"{list(self.top_line)}\n{list(self.incoming_line)}"  # Note we push in the queue from 0, so this is the right repr

    def is_adjacent_symbol(self, col, candidate_line, neighboring_line, push_count, d_next_line=1, side_check=True):
        coords = []

        if not (candidate_line and neighboring_line):
            return coords

        if is_symbol(neighboring_line[col]):  # Check directly above or below
            coords.append((col, push_count - d_next_line))

        if col + 1 < len(neighboring_line):
            if is_symbol(neighboring_line[col + 1]):  # Check top right corner
                coords.append((col + 1, push_count - d_next_line))
            if is_symbol(candidate_line[col + 1]) and side_check:  # Check right or top right
                coords.append((col + 1, push_count))

        if col - 1 >= 0:
            if is_symbol(neighboring_line[col - 1]):  # Check top left corner
                coords.append((col - 1, push_count - d_next_line))
            if is_symbol(candidate_line[col - 1]) and side_check:  # Check left, same line
                coords.append((col - 1, push_count))

        return coords

    def push(self, line: str) -> None:
        self.top_line = self.incoming_line
        self.incoming_line = line.strip()
        self.current_above_part_num = (0, set())
        self.current_below_part_num = (0, set())
        self.push_count += 1  # push count is correct, number of current line with first one = 0

        for i, char in enumerate(line.strip()):
            if len(line) != self.row_size:
                raise ValueError(f"A line of length {len(line)} was "
                                 f"pushed to a SchematicBuffer with row_size={self.row_size}")
            if char.isdigit():
                self.current_below_part_num = (
                    self.current_below_part_num[0] * 10 + int(char), self.current_below_part_num[1])

                symbol_coord = self.is_adjacent_symbol(i, line, self.top_line, self.push_count)
                for coord in symbol_coord:
                    self.current_below_part_num[1].add(coord)

            if self.top_line and self.top_line[i].isdigit():
                self.current_above_part_num = (
                    self.current_above_part_num[0] * 10 + int(self.top_line[i]), self.current_above_part_num[1])
                symbol_coord = self.is_adjacent_symbol(i, self.top_line, line, self.push_count - 1, -1,
                                                       side_check=False)
                for coord in symbol_coord:
                    self.current_above_part_num[1].add(coord)

            if not char.isdigit() or i == self.row_size - 1:
                self.update_symbol_cache(self.current_below_part_num)
                self.current_below_part_num = (0, set())

            if (self.top_line and not self.top_line[i].isdigit()) or i == self.row_size - 1:
                self.update_symbol_cache(self.current_above_part_num)
                self.current_above_part_num = (0, set())

            if i == self.row_size - 1:
                # At the end of the line, collect the values that are out of scope, tally the valid gear parts
                for coord, numbers in list(self.symbol_cache.items()):
                    if coord[1] <= self.push_count - 1 or self.push_count == self.row_count - 1:
                        if len(numbers) == 2:
                            self.total += numbers[0] * numbers[1]
                        del (self.symbol_cache[coord])

    def update_symbol_cache(self, part_num):
        for symbol_coord in part_num[1]:
            if symbol_coord not in self.symbol_cache:
                self.symbol_cache[symbol_coord] = [part_num[0]]
            else:
                self.symbol_cache[symbol_coord].append(part_num[0])


if __name__ == '__main__':

    with open('input.csv') as f:
        row_count = sum(1 for row in f)
        sb = SchematicBuffer(row_size=140, row_count=row_count)
    with open('input.csv') as f:
        for i, line in enumerate(f):
            sb.push(line.strip())  # Push is behaving
    print(sb.total)
