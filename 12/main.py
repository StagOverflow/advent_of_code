
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
            self.elevation = ord('d')
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
                if c == 'S':
                    print('bloup')

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


def find_summit_path(grid, start, end):
    print(f"Start: {start}")
    print(f"End: {end}")

    to_visit = [start]
    steps = 0
    shortest_path = None
    path = []

    while to_visit:
        current_location = to_visit[-1]
        print('current')
        print(current_location)
        path.append(to_visit.pop())

        unvisited_neighbors = []

        reachable_points = check_available_destinations(
            current_location.row,
            current_location.col,
            grid)

        if not current_location.visited:
            current_location.visited = True

            unvisited_neighbors = list(filter(lambda x: not x.visited, reachable_points))

            for location in unvisited_neighbors:
                to_visit.append(location)

        if end in reachable_points:
            if (not shortest_path) or (steps < shortest_path):
                print(path)
                for node in path:
                    print(node)
                shortest_path = steps + 1

        # If this is a dead end, we need to backtrack, else we are moving forward
        if unvisited_neighbors:
            steps = steps + 1
        else:
            steps - 1
            path.pop()

    return shortest_path


grid, start, end = ingest_map('sample.txt')
print(find_summit_path(grid, start, end))
    # Create a stack of nodes to explore
    # Pop from stack when going back
    # Depth first search


