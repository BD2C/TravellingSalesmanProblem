import math,copy,sys,random,time 
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
        
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
    def longueur(self,seq):
        return len(seq)
    def distance(self,seq):
        if self.longueur(seq)>1:
            cout=0
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
            cout+=self.graphe[seq[-1]][seq[0]]
            return cout
        else:
            return None
    def tabou(self,parcours,stop):
        bestSolution=copy.copy(parcours)
        bestCout=self.distance(parcours)
        print "parcours initial"
        print bestSolution
        print bestCout
        solutions=[]
        print "solutions meilleures que initial"
        while stop>0:
            v={}
            stop-=1
            p=copy.copy(bestSolution)
            for i in range(len(p)*(len(p)-2)+1):
                p=copy.copy(bestSolution)
                j=random.randint(2,len(p)-1)
                i=random.randint(0,j-1)
                p[i:(1+j)]=reversed(p[i:(1+j)])
                if self.distance(p)<bestCout and p not in v.values() and p not in solutions:
                    v[self.distance(p)]=p
            if len(v)>0:
                cout=v.keys()[0]
                cout=min(v.keys(),cout)
                solutions.append(v[cout])
                bestSolution=copy.copy(v[cout])
                bestCout=cout
                print bestSolution
                print bestCout
        print 'listes des meilleures solutions'
        print solutions
        print 'Solution finale'
        print bestSolution
        print bestCout

          
            
tps1 = time.clock()
w = [None, [None, None, 2, 12, 6, 15, 16, 20, 13, 14, 16, 23, 23, 29, 25, 26, 27],
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
g=Graphe(w)
g.tabou([1,2,3,7,6,5,16,15,14,13,12,11,10,9,8,4],100)
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
        

# listes des meilleures solutions
# [[1, 2, 3, 4, 5, 6, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16], [3, 2, 1, 4, 5, 6, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16]]
# Solution finale
# [3, 2, 1, 4, 5, 6, 7, 11, 10, 9, 8, 12, 13, 14, 15, 16]
# 120
# temps d'execution
# 1.97601871565