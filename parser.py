
def parser(reaction):
    species = reaction.split('+')
    cnt_char = dict()
    for entity in species:
        elements = []
        counts = []
        ongoing = False
        i = 0
        cnt_l = dict()
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
            if elements[i] not in cnt_l.keys():
                cnt_l[elements[i]] = 0
            cnt_l[elements[i]] += counts[i]
        for key in cnt_char.keys():
            if key not in cnt_l.keys():
                cnt_l[key] = 0
        for key in cnt_l.keys():
            if key not in cnt_char.keys():
                cnt_char[key] = []
            cnt_char[key].append(cnt_l[key])
    return cnt_char