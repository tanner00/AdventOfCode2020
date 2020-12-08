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


ids = []

for line in sys.stdin:
    found_r = search(line[:7], 0, 127, "F", "B")
    found_c = search(line[7:], 0, 7, "L", "R")
    found_id = found_r * 8 + found_c
    ids.append(found_id)

ids = sorted(ids)
for i in range(0, len(ids) - 1):
    if ids[i] + 1 == ids[i + 1] - 1:
        print("Seat ID: {}".format(ids[i] + 1))
