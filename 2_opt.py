import time,sys
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
        return False
    def longueur(self,seq):
        return len(seq)
    def distance(self,seq):
        cout=0
        if self.longueur(seq)>1:
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
        return cout
    
    def two_opt(self, points):
        print 'parcours initial'
        print points
        print 'cout parcours initial'
        print self.distance(points)
        for i in range(len(points) - 1):
            for j in range(i + 2, len(points) - 1):
                if self.dist(points[i], points[i+1]) + self.dist(points[j], points[j+1]) > self.dist(points[i], points[j]) + self.dist(points[i+1], points[j+1]):
                    points[i+1:j+1] = reversed(points[i+1:j+1])
        print 'parcours final'
        print points
        print 'cout parcours final'
        print self.distance(points)
    def dist(self, a, b):
        if self.arcExist(a,b):
            return self.graphe[a][b]


                    
                
        
tps1 = time.clock() 

w=[0,[0,0,5,8,4,3,2],
   [0,5,0,4,2,1,3],
   [0,8,4,0,7,5,4],
   [0,4,2,7,0,9,8],
   [0,3,1,5,9,0,4],
   [0,2,3,4,8,4,0]]

w2=w=[None,[None,None,76,43,38,51,42,19,80],
   [None,42,None,49,26,78,52,39,87],
   [None,48,28,None,40,63,44,68,61],
   [None,72,31,29,None,42,49,50,38],
   [None,30,52,38,47,None,64,72,82],
   [None,66,51,83,51,22,None,37,71],
   [None,77,62,93,54,69,38,None,26],
   [None,42,58,66,76,41,52,83,None]]
g=Graphe(w2)
g.two_opt([1, 7, 8, 4, 2, 3, 6, 5, 1])
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)
