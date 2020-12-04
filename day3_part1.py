# Explanation

# The important property of this problem is that the grid is made
# by placing identical columns side-by-side.
# This means that instead of trying to construct what this grid would actually
# look like, we can exploit this property to use no extra memory.

# Defining the important property looks like this:
# G(x, y) = G(x2, y) if x1 = x2 (mod G_width)
# This means that two cells share the same value if they share the same y
# and their x values are equal to each other when taken mod G_width.

# To help explain this statement:
# Say we had a list L with the values 3, 5, 10.
# And we decided to repeat this list infinitely: 3, 5, 10, 3, 5, 10, 3, 5, ...
# L[1] = 5 = L[4] = L[7] = L[10] = ... = L[1 + 3k]
# This means that instead of trying to construct this infinitely long list to
# check if two elements would be equal, we can just check that they
# are at the same position modulo L_length.
# L[1] = L[4] is known without constructing the list because 1 % 3 = 4 % 3.

# This solution basically uses a 2D extension of the above statement.

# We just walk down the grid using our slopes.
# If we ever pass the X boundaries of the grid,
# we loop back around to what our position would be mod G_width.

# This makes our update rules for our position:
# G_x = (G_x + X_MOVE) % G_width
# G_y = G_y + Y_MOVE

# Then we just check if our current position contains a tree and update
# the counter if so.

# When we exhaust the Y space on the grid, we know we reached the end.

# The time complexity is O(G_height / Y_MOVE) because
# we move along the height of the grid by Y_MOVE until we have no
# grid left to explore.

import sys

RIGHT = 3
DOWN = 1

grid = []
for line in sys.stdin:
    # Remove the newline character so it doesn't appear in the grid.
    grid.append([c for c in line[:-1]])

trees = 0

grid_x = 0
grid_y = 0
while True:
    grid_x = (grid_x + RIGHT) % len(grid[0])
    grid_y += DOWN
    if grid_y >= len(grid):
        break

    if grid[grid_y][grid_x] == '#':
        trees += 1

print("Trees encountered: {}".format(trees))
