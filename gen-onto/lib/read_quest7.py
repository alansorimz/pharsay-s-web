import numpy as np

def read_quest7(file):
    
    res_a = []
    def pertanyaan7(x, file):
        result = []
        for i in range(file.shape[0]):
            if(file[i,0] == x): 
                result.append(file[i,2])
                if(file[i,1] != 'hasbPre' and file[i,1] != 'hascObj' and 
                file[i,1] != 'hasdPel' and file[i,1] != 'haseKet' and 
                file[i,1] != 'hasFnom' and file[i,1] != 'hasFadje' and
                file[i,1] != 'hasFverb' and file[i,1] != 'hasFnum' and
                file[i,1] != 'hasPewatas' and file[i,1] != 'hasKlausa' and
                file[i,1] != 'hasFprep' and file[i,1] != 'hasZnext' and
                file[i,1] != 'hasaSub'):
                    print(file[i,2],end=' ')
                    res_a.append(file[i,2])
            
            if (file[i,2]=="karena"):
                break
                
        result = np.array(result)
        
        for i in result:
            pertanyaan7(i, file)


    temp_res_soal = []
    
    def soal7(x, file):
        pertanyaan7 (x,file)
        
    for i, f in enumerate(file):
        stc = f"s{i + 1}" 
        soal7(stc, file)

        tempa = ''

        if len(res_a) != 0:
            tempa = ' '.join(res_a).strip() + '....' + ' '
            temp_res_soal.append(tempa)

        if len(res_a) == 0:
            continue
        
        res_a = []
    
    return temp_res_soal
