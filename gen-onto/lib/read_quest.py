import numpy as np

def read_quest(file):
    def quest1(x, file):
        result = []
        for i in range(file.shape[0]):
            if file[i,0] == x: 
                result.append(file[i,2])
                if (file[i,1] not in ['hasbPre', 'hascObj', 'hasdPel', 'haseKet', 
                                      'hasFnom', 'hasFadje', 'hasFverb', 'hasFnum', 
                                      'hasPewatas', 'hasKlausa', 'hasFprep', 'hasZnext', 
                                      'hasaSub', 'hasNext']):
                    temp = file[i,2] + ' '
                    res_quest.append(temp)
            
            if file[i,2] in ["dari", "ke", "di", "adalah", "merupakan"]:
                break

        result = np.array(result)
        
        for i in result:
            quest1(i, file)
    
    res_quest = []
    temp_res_quest = []
    

    def soal1(x, file):
        quest1(x, file)

    for i, f in enumerate(file):
        stc = f"s{i + 1}" 
        soal1(stc, file)

        if len(res_quest) == 0:
            continue
        
        concatenated_res = ''.join(res_quest).strip() + '.....'
        temp_res_quest.append(concatenated_res)
        res_quest = []
    
    return temp_res_quest