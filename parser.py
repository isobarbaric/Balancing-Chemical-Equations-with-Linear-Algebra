
import re

def parser(reaction):
    species = reaction.split('+')
    cnt_g = dict()
    for entity in species:
        elements = []
        counts = []
        ongoing = False
        i = 0
        while i < len(entity):
            if entity[i].isnumeric():
                cnt = ''
                end = len(entity)
                for j in range(i, len(entity)):
                    if not entity[j].isnumeric():
                        end = j
                        break
                    cnt += str(entity[j])
                counts.append(int(cnt))
                i = end
                print(cnt)
                ongoing = False
            else:
                if ongoing:
                    if entity[i].isupper():
                        elements.append(entity[i])
                        counts.append(1)
                    else:
                        elements[-1] += entity[i]
                else:  
                    elements.append(entity[i])
                    ongoing = True
                i += 1
        if ongoing:
            counts.append(1) 
        for i in range(len(elements)):
            if elements[i] not in cnt_g.keys():
                cnt_g[elements[i]] = 0
            cnt_g[elements[i]] += counts[i]
    return cnt_g