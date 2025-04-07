def int_to_roman(num: int):
    roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    result = ""
    roman_keys = list(roman.keys())
    for j in range(2, len(roman_keys)+2, 2):
        print(j)
        reminder = num % 10
        match reminder:
            case 4:
                result += roman[roman_keys[j-1]] + roman[roman_keys[j-2]]
            case 9:
                result += roman[roman_keys[j]] + roman[roman_keys[j-2]]
            case _:
                if reminder < 4:
                    result += reminder * roman[roman_keys[j-2]]
                else:
                    print("here")
                    result += (reminder - 5) * roman[roman_keys[j - 2]] + roman[roman_keys[j - 1]]


        num = num // 10

        if num == 0:
            break
    return result[::-1]




if __name__ == '__main__':
    print(int_to_roman(49))

