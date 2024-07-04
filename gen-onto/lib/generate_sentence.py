import numpy as np

def generate_sentence(file, template):
    file = np.array(file)
    template = np.array(template)

    result = []
    for f in file:
        f = f.split('&')
        for j in range(template.shape[0]):
            temp = ""
            for k in range (len(template[j])):
                if(template[j][k] == '[class]'):
                    temp += f[0] + ' '
                elif (template[j][k] == '[instance]'):
                    temp += f[1] + ' '
                else:
                    temp += template[j][k] + ' '
            result.append(temp)

    return result
