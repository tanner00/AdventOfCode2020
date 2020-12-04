# Explanation

# This is an extension of the previous problem.
# It is also well known and is given the name 3SUM.

# All of previous solutions will still work, they just need to be extended.

# Here, I implemented the set solution because it gives the best time complexity.
# The time complexity is O(n^2).

# In general, K-sums can be solved in O(n^(k - 1)) time.

import sys

REQUIRED_SUM = 2020

expenses = set()
for line in sys.stdin:
    expenses.add(int(line))

for e1 in expenses:
    for e2 in expenses:
        if REQUIRED_SUM - e1 - e2 in expenses:
            product = (REQUIRED_SUM - e1 - e2) * e1 * e2
            print("Product of the numbers that sum to {}: {}".format(
                REQUIRED_SUM, product))
            sys.exit(0)
