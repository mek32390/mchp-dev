from referral.wordlist import words

import random

def generate_referral_code():
    word = words[random.randint(0, len(words))]
    number = random.randint(0,9999)
    return word + str(number)

def write_code():
    with open("newfile.txt", "w") as f:
        for x in range(100):
            code = generate_referral_code()
            f.write(code + '\n')

