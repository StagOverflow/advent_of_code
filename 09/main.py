# Rules

# 1. The head (H) and tail (T) must always be touching
# (diagonally adjacent and even overlapping both count as touching):
#
# 2. If the head is ever two steps directly up, down, left, or right from the tail,
# the tail must also move one step in that direction so it remains close enough:
#
# 3. Otherwise, if the head and tail aren't touching and aren't
# in the same row or column, the tail always moves one step diagonally to keep up:

from enum import Enum


class Direction(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


class HeadInput:
    def __init__(self, command: str):
        self.direction = Direction(command[0])
        self.steps = range(int(command[2]))


def move_head(head_position, direction: Direction):
    if direction == Direction.UP:
        return head_position[0] - 1, head_position[1]

    elif direction == Direction.DOWN:
        return head_position[0] + 1, head_position[1]

    elif direction == Direction.LEFT:
        return head_position[0], head_position[1] - 1

    elif direction == Direction.RIGHT:
        return head_position[0], head_position[1] + 1

    else:
        raise(Exception("Invalid direction input"))

def move_tail(tail_position, head_position):
    if tail_position == head_position:
        return tail_position
    elif tail_position[0] == head_position[0]:
        tail_position[1] = head_position


def parse_grid(input_path, grid_size=100):
    # A bit of shortcut, we could expand a grid on the fly or something fancy
    grid = [[0] * grid_size] * grid_size

    head_position = (0,0)
    tail_position = (0,0)

    with open(input_path) as instructions:
        for line in instructions:
            motions = HeadInput(line)

            for _ in motions.steps:
                head_position = move_head(head_position, motions.direction)
                tail_position = move_tail(tail_position, head_position)




    pass


h = HeadInput("U 3")
print(h.direction)
for s in h.steps:
    print(s)

