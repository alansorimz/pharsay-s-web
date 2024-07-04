import numpy as np
# belum berhasil 
def read_quest2(file):
    #2. OBJEK /SUBJEK 
    res_a = []
    def pertanyaan2a(x, file):
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
            
            if ('oleh' in file[i,2]):
                break
                
        result = np.array(result)
        
        for i in result:
            pertanyaan2a(i, file)

    # res_b = []
    # def pertanyaan2b(file):
    #     result = []
    #     for i in range(file.shape[0]):
    #         if('type' in file[i,1] ):  
    #             print(file[i,2],end=' ')
    #             res_b.append(file[i,2])
    #             break;
            
    #     result = np.array(result)
        
    #     for i in result:
    #         pertanyaan2b(file)

    temp_res_soal = []
    
    def soal2(x, file):
        pertanyaan2a (x,file)
        
        # print ('Sebutkan contoh dari',end=' ')
        # pertanyaan2b (file)

    for i, f in enumerate(file):
        stc = f"s{i + 1}" 
        soal2(stc, file)

        tempa = ''
        # tempb = ''

        if len(res_a) != 0:
            tempa = ' '.join(res_a).strip() + '.....' + ' '
            temp_res_soal.append(tempa)
        # if len(res_b) != 0:
        #     tempb = "Sebutkan contoh dari" + ' '.join(res_b) + '\n'  
        #     temp_res_soal.append(tempb)

        if len(res_a) == 0:
            continue
        
        res_a = []
        # res_b = []
    
    return temp_res_soal
