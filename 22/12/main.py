
class Location:
    def __init__(self, row, column, elevation):
        self.row = row
        self.col = column
        self.accessible_neighbors = None
        self.visited = False
        self.is_end = False
        self.is_start = False

        if Location.is_beginning(elevation):
            self.elevation = ord('a')
            self.is_start = True

        elif Location.is_end(elevation):
            self.elevation = ord('z')
            self.is_end = True
        else:
            self.elevation = ord(elevation)

    @staticmethod
    def is_beginning(elevation):
        return ord(elevation) == ord('S')

    @staticmethod
    def is_end(elevation):
        return ord(elevation) == ord('E')

    def __str__(self):
        return f"row: {self.row} - col: {self.col} - elevation: {self.elevation}"


def ingest_map(input_path):
    grid = []
    row = 0

    with open(input_path) as heatmap:
        start = None
        end = None

        for line in heatmap:
            line = line.strip()
            grid_row = []
            col = -1
            for c in line:
                col += 1
                new_location = Location(row, col, c)
                grid_row.append(new_location)

                start = new_location if new_location.is_start else start
                end = new_location if new_location.is_end else end


            grid.append(grid_row)
            row += 1

    return grid, start, end

def check_available_destinations(i, j, grid):
    available_directions = []
    current = grid[i][j]
    if i+1 < len(grid) and grid[i+1][j].elevation <= current.elevation + 1:
        available_directions.append(grid[i+1][j])
    if j+1 < len(grid[0]) and grid[i][j+1].elevation <= current.elevation + 1:
        available_directions.append(grid[i][j+1])
    if i-1 >= 0 and grid[i-1][j].elevation <= current.elevation + 1:
        available_directions.append(grid[i-1][j])
    if j-1 >= 0 and grid[i][j-1].elevation <= current.elevation + 1:
        available_directions.append(grid[i][j-1])

    return available_directions


def reset_visited(grid):
    for row in grid:
        for tile in row:
            tile.visited = False


def find_summit_path(grid, end):
    print(f"Start: {start}")
    print(f"End: {end}")

    possible_trail_starts = []

    for row in grid:
        for tile in row:
            if tile.elevation == ord('a'):
                possible_trail_starts.append(tile)

    valid_paths = []

    for trail_start in possible_trail_starts:
        available_paths = [[trail_start]]
        selected_path = 0
        reset_visited(grid)

        while selected_path < len(available_paths):
            cur_path = available_paths[selected_path]
            last_in_path = cur_path[-1]

            reachable_points = check_available_destinations(
                last_in_path.row,
                last_in_path.col,
                grid)

            if end in reachable_points:
                cur_path.append(end)
                valid_paths.append(cur_path)
                break

            for neighboring_tile in reachable_points:
                if not neighboring_tile.visited:
                    new_path = cur_path.copy()
                    new_path.append(neighboring_tile)
                    available_paths.append(new_path)
                    neighboring_tile.visited = True

            selected_path += 1

    path_lengths = list(map(lambda x: len(x), valid_paths))
    path_lengths.sort()

    return path_lengths



grid, start, end = ingest_map('input.txt')
print(find_summit_path(grid, end))
