from referral.wordlist import words

import random

def generate_referral_code():
    word = words[random.randint(0, len(words))]
    number = random.randint(0,9999)
    return word + str(number)
