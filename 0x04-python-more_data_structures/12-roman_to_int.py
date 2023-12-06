#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [values[x] for x in roman_string] + [0]
    _integers = 0

    for m in range(len(numbers) - 1):
        if numbers[m] >= numbers[m+1]:
            _integers += numbers[m]
        else:
            _integers -= numbers[m]

    return _integers

