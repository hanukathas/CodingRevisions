def secret_guess(secret: str, guess: str):
    n = len(secret)
    if n != len(guess):
        return [-1, -1]
    secret = secret.split()
    guess = guess.split()

    # black
    blacks = sum(1 for i in range(len(secret)) if secret[i] == guess[i])
    secret_freq = dict()
    guess_freq = dict()


    # for duplicates get frequency for both
    for s, g in zip(secret, guess):
        if s != g: # not blacks
            secret_freq[s] = secret_freq.get(s, 0) + 1
            guess_freq[g] = guess_freq.get(g, 0) + 1

    # calculate whites
    whites = 0
    for color in guess_freq:
        if color in secret_freq:
            whites += min(guess_freq[color], secret_freq[color])
    return [blacks, whites]

