def roman_to_integer(roman: str):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    number = 0

    for i in range(len(roman)):
        if i + 1 < len(roman) and roman_values[i] < roman_values[i+1]:
            number -= roman_values[i]
        else:
            number += roman_values[i]
    return number