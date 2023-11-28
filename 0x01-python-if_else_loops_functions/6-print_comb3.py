#!/usr/bin/python3
for m in range(9):
    for n in range(m + 1, 10):
        if m * 10 + n < 89:
            print("{:d}{:d}".format(m, n), end=", ")
print("{:d}".format(89))
