test1 = ["G", "B", "G", "G", "R", "B", "R", "G"]

def dutch_flags(balls: []) -> []:
    low, mid, high = 0, 0, len(balls) - 1
    while mid <= high:
        if balls[mid] == 'B':
            balls[high], balls[mid] = balls[mid], balls[high]
            high -= 1
            # mid += 1
        elif balls[mid] == 'R':
            balls[low], balls[mid] = balls[mid], balls[low]
            low += 1
            mid += 1
        else:
            mid += 1

    return balls

if __name__ == '__main__':
    print(dutch_flags(test1))