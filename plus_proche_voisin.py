import time,sys
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe

    def plusProche(self,nb_sommet,sommet):
        tete=sommet
        parcours=[]
        cycle=[]
        parcours.append(tete)
        while(len(parcours)<nb_sommet):
            minArc=sys.maxint
            minSommet=None
            for i in range(nb_sommet):
                i=i+1
                if i not in parcours:
                    if self.graphe[parcours[-1]][i]<minArc:
                        minArc=self.graphe[parcours[-1]][i]
                        minSommet=i
            parcours.append(minSommet)
        print parcours
                    
                
        
tps1 = time.clock() 

w=w=[None,[None,None,76,43,38,51,42,19,80],
   [None,42,None,49,26,78,52,39,87],
   [None,48,28,None,40,63,44,68,61],
   [None,72,31,29,None,42,49,50,38],
   [None,30,52,38,47,None,64,72,82],
   [None,66,51,83,51,22,None,37,71],
   [None,77,62,93,54,69,38,None,26],
   [None,42,58,66,76,41,52,83,None]]
g=Graphe(w)
g.plusProche(8,1)
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
