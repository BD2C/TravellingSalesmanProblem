import math,copy,sys,random,time 
class Graphe:
    def __init__(self,graphe,T = -1, alpha = -1, stop_t = -1):
        self.graphe =graphe
        self.start = math.sqrt(7) if T == -1 else T 
        self.alpha = 0.995 if alpha == -1 else alpha
        self.stop = 0.00000001 if stop_t == -1 else stop_t
        
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
    def proba(self,dist_parcours,dist_p):
        return math.exp(-abs(dist_p-dist_parcours)/self.start)
    def recuit(self,parcours):
        bestSolution=copy.copy(parcours)
        bestCout=self.distance(parcours)
        bestSolution.append(bestSolution[0])
        print "parcours initial"
        print bestSolution
        print bestCout
        
        print "solutions meilleures que initial"
        while self.start>self.stop:
            p=copy.copy(parcours)
            j=random.randint(2,len(p)-1)
            i=random.randint(0,j-1)
            p[i:(1+j)]=reversed(p[i:(1+j)])
            if self.distance(p)<bestCout:
                bestSolution=copy.copy(p)
                bestCout=self.distance(p)
                parcours=copy.copy(p)
                bestSolution.append(bestSolution[0])
                print bestSolution
                print bestCout
            else:
                if random.Random()<self.proba(self.distance(parcours),self.distance(p)):
                    parcours=copy.copy(p)
            self.start *= self.alpha
        print 'Solution finale'
        print bestSolution
        print bestCout

          
            
tps1 = time.clock() 
w=[0,[0,0,5,8,4,3,2],
   [0,5,0,4,2,1,3],
   [0,8,4,0,7,5,4],
   [0,4,2,7,0,9,8],
   [0,3,1,5,9,0,4],
   [0,2,3,4,8,4,0]]
g=Graphe(w)
g.recuit([1,2,3,4,5,6])
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)


#         ----------------
# Route getRoute(Ville b){
# for (Route r : this.voisins) {
# if (r.a.id == b.id || r.b.id == b.id) return r;
# }
# return null;
# }
#
# public static void marquage(Ville v) {
# v.marque=true;
# LinkedList<Route> l=v.voisins;
# while (! l.isEmpty()) {
# Route r=l.removeFirst();
# Ville a=r.a, b=r.b;
# if (!a.marque) marquage(a);
# if (!b.marque) marquage(b);
# }
# }
# public static boolean connexe() {
# for (int i=0;i<n;i++)
# villes[i].marque=false;
# marquage(villes[0]);
# for (int i=0;i<n;i++)
# if (!villes[i].marque) return false;
# return true;
# }
#
# class Ville {
# String nom;
# Liste<Route> voisins;
# int id;
# boolean marque;
# // ...
# }
#
#
# public int longueur() {
# int n=t;
# int l=Tsp.distance[t[n-1]][t[0]];
# for (int i=0;i<n-1;i++)
# l=l+Tsp.distance[t[i]][t[i+1]];
# return l;
# }
#
#
#
#
