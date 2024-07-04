import numpy as np
def read_template(namaFile):
    lines = []
    with open(namaFile,'r+') as f:
        line=f.read().splitlines()
        lines.append(line)
    lines = np.array(lines)
    subjek = []
    for i in range(lines.shape[1]):
        a = lines[0,i].split(" ")
        subjek.append(a)
    return subjek