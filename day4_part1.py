# Explanation

# This problem is simply a matter of implementation.

# Each passport is a continuous sequence of lines delimited by a newline.
# We want to make sure every passport contains each field except for "cid" being the optional field.
# I put the required fields in a set and build the present fields line by line for each passport.
# If each field in the required fields shows up in the present fields, the passport is valid.

import sys

REQUIRED_FIELDS = {"byr", "iyr", "eyr",
                   "hgt", "hgt", "hcl", "ecl", "pid"}

valid_passports = 0
present_fields = set()

# Add a newline to the end of the file to signify a full passport at the end.
for line in sys.stdin.readlines() + ["\n"]:
    if line == "\n":
        valid_passport = True
        for rf in REQUIRED_FIELDS:
            if rf not in present_fields:
                valid_passport = False
                break

        if valid_passport:
            valid_passports += 1

        # Reset the present fields for the next passport.
        present_fields = set()

    fields = [l.split(":")[0] for l in line.split()]
    present_fields.update(fields)

print("Number of valid passports according to the required fields: {}".format(
    valid_passports))
