import numpy as np

def read_quest1(file):
    #1. DEFINISI 
    res_a = []
    def pertanyaan1a(x, file):
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
            
            if ('pre' in file[i,0]):
                break
                
        result = np.array(result)
        
        for i in result:
            pertanyaan1a(i, file)

    # res_b = []
    # def pertanyaan1b(x,file):
    #     result = []
    #     for i in range(file.shape[0]):
    #         if(file[i,0] == x and 'sub' not in file[i,0]): 
    #             result.append(file[i,2])
    #             if(file[i,1] != 'hasbPre' and file[i,1] != 'hascObj' and 
    #                 file[i,1] != 'hasdPel' and file[i,1] != 'haseKet' and 
    #                 file[i,1] != 'hasFnom' and file[i,1] != 'hasFadje' and
    #                 file[i,1] != 'hasFverb' and file[i,1] != 'hasFnum' and
    #                 file[i,1] != 'hasPewatas' and file[i,1] != 'hasKlausa' and
    #                 file[i,1] != 'hasFprep' and file[i,1] != 'hasZnext' and
    #                 file[i,1] != 'hasaSub'):
    #                 print(file[i,2],end=' ')
    #                 res_b.append(file[i,2])
                
    #     result = np.array(result)
        
    #     for i in result:
    #         pertanyaan1b(i, file)

    temp_res_soal = []
    
    def soal1(x, file): 
        pertanyaan1a (x,file)
    
        # pertanyaan1b (x,file)

    for i, f in enumerate(file):
        stc = f"s{i + 1}" 
        soal1(stc, file)

        tempa = ''
        # tempb = ''

        if len(res_a) != 0:
            tempa = "Definisi dari " + ' '.join(res_a).strip() + '.....'
            temp_res_soal.append(tempa)
        # if len(res_b) != 0:
        #     tempb = ' '.join(res_b) + " disebut?" + ' '  
        #     temp_res_soal.append(tempb)

        if len(res_a) == 0:
            continue
        
        res_a = []
        # res_b = []

    
    return temp_res_soal
