import time,random
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
    def longueur(self,seq):
        return len(seq)
    def distance_parcours(self,seq):
        if self.longueur(seq)>1:
            cout=0
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
            return cout
        else:
            return None
    def auHazard(self,nb_sommet):
        parcours=[]
        for i in range(nb_sommet+1):
            if i!=0:
                parcours.append(i)
        parcours.append(1)
        dist=self.distance_parcours(parcours)
        distprec=dist
        print(parcours)
        print(dist)
        i=nb_sommet-1
        while(i>1):
            j=random.randint(1,i-1)
            temp=parcours[i]
            parcours[i]=parcours[j]
            parcours[j]=temp
            dist=self.distance_parcours(parcours)
            if dist < distprec:
                print(parcours)
                distprec=dist
                print(dist)
            i=i-1               
        
tps1 = time.clock()
villes2 = [None, [None, None, 2, 12, 6, 15, 16, 20, 13, 14, 16, 23, 23, 29, 25, 26, 27],
           [None, 2, None, 10, 8, 17, 18, 18, 15, 16, 18, 25, 25, 27, 27, 28, 29],
           [None, 12, 10, None, 14, 15, 14, 10, 25, 26, 26, 19, 23, 17, 29, 28, 27],
           [None, 6, 8, 14, None, 17, 18, 16, 15, 16, 18, 25, 26, 23, 27, 28, 29],
           [None, 15, 17, 15, 17, None, 1, 5, 16, 17, 19, 16, 20, 14, 26, 25, 24],
           [None, 16, 18, 14, 18, 1, None, 4, 17, 18, 20, 15, 19, 13, 25, 24, 23],
           [None, 20, 18, 10, 16, 5, 4, None, 21, 20, 18, 11, 15, 9, 21, 20, 19],
           [None, 13, 15, 25, 15, 16, 17, 21, None, 1, 3, 10, 12, 16, 14, 15, 16],
           [None, 14, 16, 26, 16, 17, 18, 20, 1, None, 2, 9, 13, 15, 15, 16, 17],
           [None, 16, 18, 26, 18, 19, 20, 18, 3, 2, None, 7, 15, 13, 17, 18, 19],
           [None, 23, 25, 19, 25, 16, 15, 11, 10, 9, 7, None, 12, 6, 18, 17, 16],
           [None, 23, 25, 23, 26, 20, 19, 15, 12, 13, 15, 12, None, 6, 18, 17, 16],
           [None, 29, 27, 17, 23, 14, 13, 9, 16, 15, 13, 6, 6, None, 12, 11, 10],
           [None, 25, 27, 29, 27, 26, 25, 21, 14, 15, 17, 18, 18, 12, None, 1, 2],
           [None, 26, 28, 28, 28, 25, 24, 20, 15, 16, 18, 17, 17, 11, 1, None, 1],
           [None, 27, 29, 27, 29, 24, 23, 23, 19, 16, 17, 19, 16, 16, 10, 2, 1, None]]
g=Graphe(villes2)
g.auHazard(16)
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1]
# 138
# temps d'execution
# 0.000919133368989



# au hasard
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1]
# 138
# temps d'execution
# 0.000189293178248