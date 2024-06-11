from owlready2 import *
import numpy as np

def parent_recursion(onto):
    res_recursion = []

    def recursion(x):
        result = list(default_world.sparql("""
        PREFIX okbi: <http://purl.org/net/Pharmaco#>
        SELECT ?subjek ?predikat ?objek
        WHERE
        { 
        ?p rdf:type owl:ObjectProperty 
        ?predikat rdfs:subPropertyOf* ?p.
        ?subjek ?predikat ?objek. 
        FILTER (?subjek =""" + x + """
        )
        }
        """))
        
        #print(x)
        result = np.array(result)
        if(len(result) !=0 ):
            res_recursion.append(result)
        
        for i in result:
            if(str(i[1]).split('.')[1]!='hasNext'):
                recursion('okbi:'+str(i[2]).split('.')[1])

    for individual in onto.individuals():
        individual_name = individual.name
        if individual_name.startswith("s"):
            recursion(f"okbi:{individual_name}")

    res = ""
    for i, x in enumerate(res_recursion):
        res += str(x)
        if(len(res_recursion) == i+1):
            continue
        res += "\n"

    return res
    