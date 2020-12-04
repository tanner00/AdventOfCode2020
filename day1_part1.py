# Explanation:

# We want to find two numbers in a list that satisfy:
# e1 + e2 = K
# for an arbitrary K and return their product.
# This problem is well known and is given the name 2SUM.

# The naive approach is to have two nested for loops and check each pair of numbers for this property.
# This gives the time complexity O(n^2).
# However, this can be optimized.

# A better approach is to sort the list of numbers in nondecreasing order.
# This approach still uses two nested for loops, but you can break out of the inner loop if the current sum is already above K.
# This is because the sum will only increase as you move along to the right of the list.
# This gives the time complexity O(n * log2(n)) due to the sorting.
# This can be optimized too.

# The best approach is using a set or map.
# This is because we can rearrange the original equation into this:
# e2 = e1 - K
# This means we can just check if the set contains e1 - K, and if it does we know that there are
# two numbers that sum to K.
# Checking if an element exists in a set is considered to be O(1).
# We do this for each element in E until we get a match, so the time complexity is O(n) * O(1) = O(n).

import sys

REQUIRED_SUM = 2020

expenses = set()
for line in sys.stdin:
    expenses.add(int(line))

for e in expenses:
    if REQUIRED_SUM - e in expenses:
        product = (REQUIRED_SUM - e) * e
        print("Product of the numbers that sum to {}: {}".format(
            REQUIRED_SUM, product))
        sys.exit(0)
