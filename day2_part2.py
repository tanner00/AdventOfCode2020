# Explanation

# This is still just an implementation problem.

# Now we want to check if (S[p1] = C) ^ (S[p2] = C) is true for each password.
# Here ^ is boolean XOR (exclusive OR).
# This means that either S[p1] is C or S[p2] is C but NOT both.

# We just parse the input and check for this property and add 1 to the amount of valid passwords if it holds.
# We don't have to loop over the entire string this time,
# so the time complexity is reduced to O(n).

import sys

valid_passwords = 0

for line in sys.stdin:
    parts = line.split()

    positions = parts[0].split("-")
    position1 = int(positions[0]) - 1
    position2 = int(positions[1]) - 1

    important_char = parts[1][0]
    password = parts[2]

    position1_matches = bool(password[position1] == important_char)
    position2_matches = bool(password[position2] == important_char)
    if position1_matches ^ position2_matches:
        valid_passwords += 1

print("Number of valid passwords according to their policies: {}".format(valid_passwords))
