def letter_combinations(digits: str):
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    def combinator(i: int, slate: list):
        if i == len(digits):
            result.append("".join(slate[:]))
            return
        else:
            for letter in letters[digits[i]]:
                slate.append(letter)
                combinator(i + 1, slate)
                slate.pop()

    combinator(0, [])
    return result


if __name__ == '__main__':
    # print(phone_letter_combination("23"))
    # print(phone_letter_combination_revision("23"))
    print(letter_combinations("23"))
    print(letter_combinations("2323"))