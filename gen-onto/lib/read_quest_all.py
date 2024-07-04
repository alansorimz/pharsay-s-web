import numpy as np
from lib.read_quest1 import read_quest1
from lib.read_quest2 import read_quest2
from lib.read_quest3 import read_quest3
from lib.read_quest4 import read_quest4
from lib.read_quest5 import read_quest5
from lib.read_quest6 import read_quest6
from lib.read_quest7 import read_quest7
from lib.read_quest8 import read_quest8
from lib.read_quest9 import read_quest9
from lib.read_quest10 import read_quest10
from lib.read_quest11 import read_quest11

def read_quest_all(file):
    #PEMBANGKITAN SOAL DARI 1 KALIMAT KE BANYAK TIPE SOAL
    output = []
    # result = []
    def pertanyaan(file,soal):
        result = []
        if(soal == 1):
            for i in range(file.shape[0]):
                if(file[i,2] == 'adalah' or file[i,2] == 'merupakan'):
                    if not any(" ".join(read_quest1(file)) in x for x in result):
                        result.extend(read_quest1(file))
        if(soal == 2): 
            for i in range(file.shape[0]):
                if(file[i,2] == 'oleh'): 
                    if not any(" ".join(read_quest2(file)) in x for x in result):
                        result.extend(read_quest2(file))      
        if(soal == 3): 
            for i in range(file.shape[0]):
                if(file[i,2] == 'digunakan'):
                    if not any(" ".join(read_quest3(file)) in x for x in result):
                        result.extend(read_quest3(file))    
        if(soal == 4): 
            for i in range(file.shape[0]):
                if(file[i,2] == 'setelah'): 
                    if not any(" ".join(read_quest4(file)) in x for x in result):
                        result.extend(read_quest4(file))   
        if(soal == 5): 
            for i in range(file.shape[0]):
                if(file[i,2] == 'ke' or file[i,2] == 'di'): 
                    if not any(" ".join(read_quest5(file)) in x for x in result):
                        result.extend(read_quest5(file))   
        if(soal == 6): 
            for i in range(file.shape[0]):
                if(file[i,2] == 'ketika'): 
                    if not any(" ".join(read_quest6(file)) in x for x in result):
                        result.extend(read_quest6(file))    
        if(soal == 7): 
            for i in range(file.shape[0]):
                if(file[i,2] == 'karena' or file[i,2] == 'sebab'): 
                    if not any(" ".join(read_quest7(file)) in x for x in result):
                        result.extend(read_quest7(file))    
        if(soal == 8): 
            # print(f"Iki Quest 8 {read_quest8(file)}")
            if (read_quest8(file)[0]):
                result.extend(read_quest8(file)[0])
            else:
                result.extend(read_quest8(file))
        # if(soal == 9): 
        #     for i in range(file.shape[0]):
        #         if(file[i,1] == '9'): 
        #             if not any(" ".join(read_quest9(file)) in x for x in result):
        #                 if (read_quest9(file)[0]):
        #                     result.extend(read_quest9(file)[0])
        #                 else:
        #                     result.extend(read_quest9(file))
        if(soal == 9): 
            if not any(" ".join(read_quest10(file)) in x for x in result):
                if (read_quest10(file)[0]):
                    result.extend(read_quest10(file)[0])
                else:
                    result.extend(read_quest10(file))
        if(soal == 10): 
            if not any(" ".join(read_quest11(file)) in x for x in result):
                if (read_quest11(file)[0]):
                    result.extend(read_quest11(file)[0])
                else:
                    result.extend(read_quest11(file))
        
        print("")
        
        return "".join(result)
        
    # get_soal = []

    batas = 11
    for i in range(1,batas):
        temp = pertanyaan(file, i)
        if temp != "":
            output.append(temp)
        else:
            output.append('-')
        # print (f'Soal ke {i}:', end='') 
        # get_soal.extend(temp)
    
    return output