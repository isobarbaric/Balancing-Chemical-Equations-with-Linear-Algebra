
import re

a = "3Ca2PhO2G4K3O5+3H2O"

reactants = a.split('+')
cnt_g = dict()

for reactant in reactants:
    mult = 1
    start = 0
    if (reactant[0].isnumeric()):
        mult = int(reactant[0])
        start = 1
    elements = []
    counts = []
    ongoing = False
    for i in range(start, len(reactant)):
        if reactant[i].isnumeric():
            cnt = ''
            end = len(reactant)
            for j in range(i, len(reactant)):
                if not reactant[j].isnumeric():
                    end = j
                    break
                cnt += str(reactant[j])
            counts.append(int(cnt))
            i = end
            ongoing = False
        else:
            if ongoing:
                if reactant[i].isupper():
                    elements.append(reactant[i])
                    counts.append(1)
                else:
                    elements[-1] += reactant[i]
            else:  
                elements.append(reactant[i])
                ongoing = True
    counts = [mult*i for i in counts]
    if ongoing:
        counts.append(1) 
    for i in range(len(elements)):
        if elements[i] not in cnt_g.keys():
            cnt_g[elements[i]] = 0
        cnt_g[elements[i]] += counts[i]

print(cnt_g)