import random

def random_mix(seq_a, seq_b):
    iters = [iter(seq_a), iter(seq_b)]
    lens = [len(seq_a), len(seq_b)]
    while all(lens):
        r = random.randrange(sum(lens))
        itindex = r < lens[0]
        it = iters[itindex]
        lens[itindex] -= 1
        yield next(it)
    for it in iters:
        for x in it: yield x
        iters = [iter(seq_a), iter(seq_b)]
