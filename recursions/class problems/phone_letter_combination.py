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

def phone_letter_combination_revision(digits: str):
    result = []
    letters = {"2": "abc", "3": "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    def helper(i, slate):
        if i == len(digits):
            result.append(slate[:])
            return
        for letter in letters[digits[i]]:
            slate.append(letter)
            helper(i+1, slate)
            slate.pop()


    helper(0, [])
    return result

def phone_letter_combination_revision_2(digits: str):
    result = []
    letters = {"1":" ", "0":" ","2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    def helper(i, slate):

        if len(slate) == len(digits):
            result.append(str("".join(slate[:]).strip()))
            return

        for letter in letters[digits[i]]:
            slate.append(letter)
            helper(i+1, slate)
            slate.pop()

    helper(0,[])
    return result

if __name__ == '__main__':
    # print(phone_letter_combination("23"))
    # print(phone_letter_combination_revision("23"))
    print(phone_letter_combination_revision_2("1010101"))