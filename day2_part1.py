# Explanation

# This is really just an implementation problem.

# We want to check that a given password has no less than L occurences of C but no more than H occurences of C.
# We just parse the input and loop over the string counting the number of times C occurs.
# If the occurences of C is in the specified range, we add 1 to the amount of valid passwords.

# Time complexity: O(n * m)
# n is the number of password checks.
# m is length of the longest password.

import sys

valid_passwords = 0

for line in sys.stdin:
    parts = line.split()

    occurences = parts[0].split("-")
    occurences_lower_bound = int(occurences[0])
    occurences_upper_bound = int(occurences[1])

    important_char = parts[1][0]
    password = parts[2]

    count = 0
    for c in password:
        if c == important_char:
            count += 1

    if occurences_lower_bound <= count <= occurences_upper_bound:
        valid_passwords += 1

print("Number of valid passwords according to their policies: {}".format(valid_passwords))
