import numpy as np
def read_triplet(lines):
    subject = []

    for x in lines:
        x = x.strip()
        x = x.split()
        subject.append(x)

    return subject