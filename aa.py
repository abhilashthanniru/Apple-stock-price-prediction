def get_user_input():
    """
    Prompts the user for input values and returns them as a tuple.
    """

    n = int(input("Enter the size of the grid (n): "))
    grid = []
    for i in range(n):
        row = input(f"Enter row {i+1} values (separate by spaces, use '' for restricted pools): ").split()
        grid.append(row)
    M = int(input("Enter the oxygen capacity (M): "))
    target = input("Enter the destination corner (BR or TR): ").upper()
    return grid, M, target

def find_paths(grid, M, target, source=(0, 0)):
    """
    Finds all available paths and feasible paths considering oxygen consumption.

    Args:
        grid: A 2D list representing the pool setup.
        M: The oxygen capacity of the diver.
        target: The destination corner ("BR" or "TR").
        source: The starting point (default: (0, 0)).

    Returns:
        A tuple containing two lists: all_paths and feasible_paths.
    """

    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    all_paths, feasible_paths = [], []

    def dfs(x, y, oxygen, path):
        current_path = path + [(x, y)]
        if x == target[0] and y == target[1]:
            all_paths.append(current_path)
            if oxygen >= 0:
                feasible_paths.append(f"{''.join([str(p) for p in current_path])} {oxygen}")
            return

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] != "":
                new_oxygen = oxygen - (grid[x][y] + grid[new_x][new_y])
                dfs(new_x, new_y, new_oxygen, current_path)

    dfs(source[0], source[1], M, [])
    return all_paths, feasible_paths

if _name_ == "_main_":
    grid, M, target = get_user_input()
    all_paths, feasible_paths = find_paths(grid, M, target)

    if feasible_paths:
        print("The available paths are:")
        for path in all_paths:
            print(''.join([str(p) for p in path]))
        print("The feasible paths with remaining oxygen levels are:")
        for path in feasible_paths:
            print(path)
    else:
        print("No path available to reach the destination.")