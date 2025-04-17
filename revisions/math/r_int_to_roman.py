def r_int_to_roman(number: int):
    roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
                 900: 'CM', 1000: 'M'}

    roman_map = dict(sorted(roman_map.items(), key= lambda item: -item[0]))
    roman = []

    for i in roman_map.keys():
        if number > i:
            quotient = number // i
            number = number % i
            roman.append(roman_map[i] * quotient)

    return  "".join(roman)

if __name__ == '__main__':
    print(r_int_to_roman(3245))

