
def parser(reaction):
    species = reaction.split('+')
    cnt_char = dict()
    iterNum = 1
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
        for key in cnt_l.keys():
            if key not in cnt_char.keys():
                cnt_char[key] = []
            cnt_char[key].append([iterNum, cnt_l[key]])
        iterNum += 1
    for key in cnt_char.keys():
        for i in range(1, len(species)+1):
            # find 'i' as first element in the nested list
            found = False
            for j in range(len(cnt_char[key])):
                if (cnt_char[key][j][0] == i):
                    found = True
            if not found:
                cnt_char[key].append([i, 0])
        cnt_char[key].sort()
    # for key in cnt_char.keys():
        # print(key, cnt_char[key])
    return cnt_char