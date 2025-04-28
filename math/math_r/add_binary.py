def add_binary(a: str, b: str):
    reminder = 0
    solutions = { "100": [0,1], "110": [1,0],"101": [1,0],"111": [1,1], "001":[0, 1], "011": [1,0], "010":[0,1]}
    i = max(len(a), len(b))
    j = i - 1
    result = ""
    while j >= 0:
        a_int = int(a[j])
        b_int = int(b[j])
        print(f"{a_int}{b_int}{reminder}")
        reminder, literal = solutions[f"{a_int}{b_int}{reminder}"]
        result = f"{literal}{result}"
        j -= 1



    return str(reminder) + result

if __name__ == '__main__':
    print(add_binary('1010', '1011'))





