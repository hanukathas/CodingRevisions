from pickletools import long4


def calculate_power(a,b):
    MOD = 1000000007
    result = 1
    base = a % MOD


    while b > 0:
        if b % 2 == 1:  # If the current bit is set
            print(b)
            result = (result * base) % MOD
            
        base = (base * base) % MOD  # Square the base
        b //= 2  # Move to the next bit
        print(b)

    return result



if __name__ == '__main__':
    print(calculate_power(2,10))