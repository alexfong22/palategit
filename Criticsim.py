def intl(set1,set2):
        keys_a = set(set1)
        keys_b = set(set2)
        intersection = keys_a & keys_b # '&' operator is used for set intersection
        return len(intersection)

def unl(set1,set2):
        keys_a = set(set1)
        keys_b = set(set2)
        intersection = keys_a | keys_b # '|' operator is used for set union
        return len(intersection)

def unle(set1,set2,set3,set4): #union extended
        keys_a = set(set1)
        keys_b = set(set2)
        keys_c = set(set3)
        keys_d = set(set4)
        intersection = keys_a | keys_b | keys_c | keys_d # '|' operator is used for set union
        return len(intersection)







#   0 = l1
#   1 = d1
#   2 = l2
#   3 = d2
def criticsim(prefs,critic1,critic2):
    l1 = set(dict((k, v) for k, v in prefs[str(critic1)].items() if v >= 4))   # 3 = meh  / is omitted
    d1 = set(dict((k, v) for k, v in prefs[str(critic1)].items() if v <= 2))
    l2 = set(dict((k, v) for k, v in prefs[str(critic2)].items() if v >= 4))
    d2 = set(dict((k, v) for k, v in prefs[str(critic2)].items() if v <= 2))
    ld = l1,d1,l2,d2
    likesp1 = ld[0]
    dislikesp1 = ld[1]
    likesp2 = ld[2]
    dislikesp2 = ld[3]
    nl = intl(likesp1,likesp2) # matching likes
    nd = intl(dislikesp1,dislikesp2) # matching dislikes

    
    nld = intl(likesp1,dislikesp2)  # conflicting likes/dislikes
    nld2 = intl(likesp2,dislikesp1) # conflicting likes/dislikes
    unlv = unle(likesp1,likesp2,dislikesp1,dislikesp2) # union = non-omitted set
    sm = float(float(nl+nd-nld-nld2) / float(unlv))
    return sm
    
    
#print criticsim(critics,"ind","Birdlaw")

def gintersection(prefs,inpuk,inpuk2):
    keys_a = set(prefs[str(inpuk)].keys())
    keys_b = set(prefs[str(inpuk2)].keys())
    intersection = keys_a & keys_b # '&' operator is used for set intersection
    return [len(intersection),len(keys_a),len(keys_b)]
        

def jaccard_index(prefs,p1, p2):
    n = gintersection(prefs,p1,p2)
    return int(n[0]) / float(int(n[1]) + int(n[2]) - int(n[0]))