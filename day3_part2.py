# Explanation

# Part 2 is a simple extension of part 1.
# I used the same logic as the previous part, I just
# repeat that logic for each slope value to get each individual tree count.

# The tree counts are multiplied to get the tree product while the solution is being computed.
# This saves us from wasting space to store each tree count.

# The time complexity is O(n * (G_height / Y_MOVE)).
# n is the amount of slopes needed to check.

import sys

UPDATES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

grid = []
for line in sys.stdin:
    # Remove the newline character so it doesn't appear in the grid.
    grid.append([c for c in line[:-1]])

tree_product = 1

for u in UPDATES:
    trees = 0

    grid_x = 0
    grid_y = 0
    while True:
        grid_x = (grid_x + u[0]) % len(grid[0])
        grid_y += u[1]
        if grid_y >= len(grid):
            break

        if grid[grid_y][grid_x] == '#':
            trees += 1

    tree_product *= trees

print("Product of all the trees encountered: {}".format(tree_product))
