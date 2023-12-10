def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'


class SchematicBuffer:

    def __init__(self, row_size=140):
        self.current_below_part_num = 0
        self.current_above_part_num = 0
        self.total = 0
        self.incoming_line = []
        self.row_size = row_size
        self.top_line = []
        self.incoming_valid_ends = set()
        self.top_valid_ends = set()

    def __repr__(self):
        return f"{list(self.top_line)}\n{list(self.incoming_line)}"

    def is_adjacent_symbol(self, col, candidate_line, neighboring_line):
        if not (candidate_line and neighboring_line):
            return False

        if is_symbol(neighboring_line[col]):  # Check directly above or below
            return True
        if col - 1 >= 0 and (is_symbol(neighboring_line[col - 1]) or is_symbol(candidate_line[col - 1])):
            # Checked left side or diagonal left
            return True
        if col + 1 < len(neighboring_line) and (is_symbol(neighboring_line[col + 1]) or is_symbol(
                candidate_line[col + 1])):
            # Checked right side or diagonal right
            # Note the immediate left/right check might happen multiple times for a given slot,
            return True

        return False

    def push(self, line: str) -> None:
        self.top_line = self.incoming_line
        self.top_valid_ends = self.incoming_valid_ends
        self.incoming_line = line.strip()
        self.incoming_valid_ends = set()
        self.current_above_part_num = (0, False)
        self.current_below_part_num = (0, False)

        for i, char in enumerate(line.strip()):
            if len(line) != self.row_size:
                raise ValueError(f"A line of length {len(line)} was "
                                 f"pushed to a SchematicBuffer with row_size={self.row_size}")
            if char.isdigit():
                part_num = self.current_below_part_num[0] * 10 + int(char)
                is_valid = self.is_adjacent_symbol(i, line, self.top_line) or self.current_below_part_num[1]
                self.current_below_part_num = (part_num, is_valid)

            if self.top_line and self.top_line[i].isdigit():
                part_num = self.current_above_part_num[0] * 10 + int(self.top_line[i])
                is_valid = self.is_adjacent_symbol(i, self.top_line, line) or self.current_above_part_num[1]
                self.current_above_part_num = (part_num, is_valid)

            if not char.isdigit() or i == self.row_size - 1:
                if self.current_below_part_num[1]:  # Tally up if valid part, else toss the number
                    self.total += self.current_below_part_num[0]
                    # We mark this part number end to not double count it on the next pass - that might have happened
                    # if there is an adjacent symbol on the yet-unseen line below
                    self.incoming_valid_ends.add(i)
                self.current_below_part_num = (0, False)

            if (self.top_line and not self.top_line[i].isdigit()) or i == self.row_size - 1:
                # if the valid number has ended, and we have not marked it yet, tally up from top line
                if self.current_above_part_num[1] and i not in self.top_valid_ends:
                    self.total += self.current_above_part_num[0]
                self.current_above_part_num = (0, False)


if __name__ == '__main__':
    sb = SchematicBuffer(row_size=140)
    with open('input.csv') as f:
        for i, line in enumerate(f):
            sb.push(line.strip())  # Push is behaving
    print(sb.total)