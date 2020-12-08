import sys


def search(s, start_low, start_high, low_char, high_char):
    low = start_low
    high = start_high
    for c in s[:-1]:
        if c == low_char:
            high -= (high - low + 1) // 2
        if c == high_char:
            low += (high - low + 1) // 2
    return low if s[-1] == low_char else high


highest_id = 0

for line in sys.stdin:
    found_r = search(line[:7], 0, 127, "F", "B")
    found_c = search(line[7:], 0, 7, "L", "R")
    found_id = found_r * 8 + found_c

    highest_id = max(highest_id, found_id)

print("Highest seat ID: {}".format(highest_id))
