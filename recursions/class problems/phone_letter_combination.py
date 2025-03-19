def phone_letter_combination(digits: str):
    result = []
    letters = {"2": "abc", "3": "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    def helper(ip, i, slate):
        if i == len(ip):
            result.append(slate[:])
            return
        for letter in letters[ip[i]]:
            slate.append(letter)
            helper(ip, i+1, slate)
            slate.pop()

    helper(digits, 0, [])
    return result

if __name__ == '__main__':
    print(phone_letter_combination("23"))