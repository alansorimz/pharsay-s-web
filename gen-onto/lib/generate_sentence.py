import numpy as np

def generate_sentence(file, template):
    file = np.array(file)
    template = np.array(template)

    result = []
    for i in range(file.shape[0]): # jumlah triplet
        for j in range(template.shape[0]): #jumlah template
            temp = ""
            for k in range (len(template[j])): #jumlah kata dalam kalimat template
                if(template[j][k] == '[class]'):
                    temp += file[i,2] + ' '
                elif (template[j][k] == '[instance]'):
                    temp += file[i,0] + ' '
                else:
                    temp += template[j][k] + ' '
            result.append(temp)

    return result
