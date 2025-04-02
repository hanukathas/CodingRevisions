def encode(strs: list[str]) -> str:
    return ','.join(strs)

def decode(s: str) -> []:
    return s.split(',')

if __name__ == '__main__':
    encoded = encode(["neet","code","love","you"])
    decoded = decode(encoded)
    print(encoded)
    print(decoded)