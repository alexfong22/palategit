def recommend(username,dtvv,minratingv=5,userstosourcev=30,minavgratingv=3,excludablev=True):
    from Critics import critics
#=============================================== Combinations that provide relevent results
#============--------Options--------============ 3-8
#=============================================== 20-50  5-35
    critics.update({username: eval(dtvv)})
    if len(eval(dtvv))==1:
        minrating = 2
        userstouse = 5
        minavgrating = 3
        usertorecommendfor = username
        excludable = excludablev
    else: 
        minrating = minratingv
        userstouse = userstosourcev
        minavgrating = minavgratingv
        usertorecommendfor = username
        excludable = excludablev
    #===============================================minratingv,userstosourcev,minavgratingv,usertorecommendforv,excludablev
    #===============================================
    #===============================================
    
    def theintersection(prefs,inpuk,inpuk2):
        keys_a = set(prefs[str(inpuk)].keys())
        keys_b = set(prefs[str(inpuk2)].keys())
        intersection = keys_a & keys_b # '&' operator is used for set intersection
        return intersection
    
    def gintersection(prefs,inpuk,inpuk2):
        keys_a = set(prefs[str(inpuk)].keys())
        keys_b = set(prefs[str(inpuk2)].keys())
        intersection = keys_a & keys_b # '&' operator is used for set intersection
        return [len(intersection),len(keys_a),len(keys_b)]
        
        
    def elargestn(arr,howmany):
        ppx = range(howmany)
        for each in arr:
            if each > min(ppx):
                ppx.remove(min(ppx))
                ppx.append(each)

        return sorted(ppx)[::-1]
    
 
    
    from math import sqrt
    def jaccard_index(prefs,p1, p2):
        n = gintersection(prefs,p1,p2)
        return int(n[0]) / float(int(n[1]) + int(n[2]) - int(n[0]))
     
    from Name import name
    count = 0
    
    
    
    #arr2 = [[1,'30'],[2,'20'],[5,'10'],[7,'20'],[3,'20']]
    #ppx = [[0,0],[0,0]]
    #for each in arr2:
    #    if each > min(ppx):
    #        ppx.remove(min(ppx))
    #        ppx.append(each)
    #print ppx
    
    from Criticsim import criticsim
    pg = []
    k2 = usertorecommendfor
    for key in critics:
        if key not in k2:
            k1 = key
            count +=1
            pg.append([jaccard_index(critics,k1,k2),k1])
    #print ppx
    #print pg      
            #if cmax<jaccard_index(critics,k1,k2):
            #    cmax=jaccard_index(critics,k1,k2)
            #    pg.append([jaccard_index(critics,k1,k2),k1])
    
    
    
    
    mv = sorted(pg)
    mlv = mv[::-1][:userstouse]#anything beyond 2:5 becomes more populist - enter a number 2-5 to tune > 5 takes top 5 matching critics - 20 takes 20 but becomes less relevent  
        
    cv = {}
    for dt in mlv:
        cv.update({dt[1]: critics[dt[1]]})
    
    
        
    
    #=============================
    
    
    
    
    ys = []
    for key in cv:
        for key2 in cv:
            x = theintersection(cv,key,key2)
            for y in x:
                if y not in ys:
                    ys.append(y)
                #print y,cv[key][y]
        pg = []
    bv = 0
    unrankedrecs = []
    for key in cv:
        vh = cv[key]
        for over in ys:
            try:
                if over not in ys:
                    ys.append(over)
                if over in ys:
                    ys.insert(int(ys.index(over)+1),str(vh[over]))#),vh[over])
                    
                #print vh[over]
                #print over,vh[over]
            except: pass
    
    sbl =  str(ys).replace("', '","|").replace("', ","#").replace(", '","|").strip("[']")
    
    def product_list(p):
        total =1 #critical step works for all list
        for i in p:
            total=total*i # this will ensure that each elements are multiplied by itself
        return total
        
    def min_ratings(p):
        if len(p)>=minrating:
            return 1
        else:
            return 0
        
    def sum_list(p):
        total =0 #critical step works for all list
        for i in p:
            total=total+i # this will ensure that each elements are multiplied by itself
        return total
        
    def avg_list(p):
        total =0 #critical step works for all list
        for i in p:
            total=total+i # this will ensure that each elements are multiplied by itself
        return total/len(p)

    def ranking_alg(p):
        positive = 0
        negative = 0
        avg = avg_list(p)
        for rank in p:
            if rank > 3:
                positive += 1
            if rank < 3:
                negative += 1
        if negative > positive:
            return 0
        else:
            return (positive - negative)+avg

    from Name import name
    ls = sbl.split("#")
    for ura in ls:
        uspr = ura.split("|")
        p = map(float, uspr[1:])
        unrankedrecs.append(str(ranking_alg(p)*min_ratings(p)) + ":" +  str(uspr[0]))
                                        # Sum * Average
    
    
    
    swrankedrecs = sorted(unrankedrecs, key=lambda x: float(x.split(":")[0]))[::-1]
    rankedrecs = []
    for each in swrankedrecs:
        mc = each.split(":")
        rankedrecs.append(mc[1] + ":" + mc[0])
    rankedarr = []
    ratingarr = []
    for rankedrec in rankedrecs:
        if excludable:
            if int(rankedrec.split(":")[0]) not in critics[usertorecommendfor]:
                if float(rankedrec.split(":")[1])>minavgrating:
                    rankedarr.append(str(name(rankedrec.split(":")[0])[0]))
        else:
            if float(rankedrec.split(":")[1])>minavgrating:
                rankedarr.append(str(name(rankedrec.split(":")[0])[0]))
    for rankedrec in rankedrecs:
        if excludable:
            if int(rankedrec.split(":")[0]) not in critics[usertorecommendfor]:
                if float(rankedrec.split(":")[1])>minavgrating:
                    ratingarr.append(str(round(float(rankedrec.split(":")[1]),2)).rjust(4))
        else:
            if float(rankedrec.split(":")[1])>minavgrating:
                ratingarr.append(str(round(float(rankedrec.split(":")[1]),2)).rjust(4))
    return rankedarr,ratingarr
    
