def r_roman_to_integer(roman: str):
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
        if i + 1 <= len(roman) - 1 and roman_values[roman[i+1]] > roman_values[roman[i]]:
            number -= roman_values[roman[i]]
        else:
            number += roman_values[roman[i]]
    return number

if __name__ == '__main__':
    print(r_roman_to_integer('XIX'))