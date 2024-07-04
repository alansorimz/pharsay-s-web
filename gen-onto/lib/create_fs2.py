
def create_fs2(inputs):
    inputs = inputs.split("\n")
    
    file1 = []
    for x, i in enumerate(inputs):
        a = i.replace("[", "")
        b = a.replace("]", "")
        b = b.replace("'", "")
        b = b.replace(",", "")
        c = b.replace("Pharmacho.", "")
        
        file1.append(c.strip())

        if(len(inputs) == x+1):
            continue
        
    return file1