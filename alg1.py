import math
import random
import copy

class SimRecuit(object):

    def __init__(self, parcour,graphe ,T = -1, alpha = -1, stop_t = -1):
        self.parcour = parcour
        self.N = len(parcour)
        self.T = math.sqrt(self.N) if T == -1 else T 
        self.alpha = 0.995 if alpha == -1 else alpha
        self.stop_temp = 0.00000001 if stop_t == -1 else stop_t

        self.matrice_distance = graphe

        self.cur_solution = parcour
        self.best_solution = copy.copy(self.cur_solution)
        

        self.cur_f = self.f(self.cur_solution)
        self.initial_f = self.cur_f
        self.best_f = self.cur_f

        self.f_list = [self.cur_f]
        

    def f(self, sol):
        ''' valeur objectif de la solution f(x) ou x est la solution page 5 smaha ampleur de la deterioration l9itha sur le net ''' 
        return round(sum( [ self.matrice_distance[sol[i-1]-1][sol[i]-1] for i in range(1,self.N) ] ) + self.matrice_distance[sol[0]-1][sol[self.N-1]-1], 3)

    def P_accept(self, candidat_f):
        '''
        probabilite daccepter un voisin plus mauvais
        exp(-delta f ij/t)page 5
        '''
        return math.exp( -abs(candidat_f-self.cur_f) / self.T  )

    def accept(self, candidat):
        '''
        accepter si meilleur avec p=1
        accepter avec p=exp(-delta f ij/t) si mauvais
        '''
        candidat_f = self.f(candidat)
        if candidat_f < self.cur_f:
            self.cur_f = candidat_f
            self.cur_solution = candidat
            if candidat_f < self.best_f:
                self.best_f = candidat_f
                self.best_solution = candidat

        else:
            if random.random() < self.P_accept(candidat_f):
                self.cur_f = candidat_f
                self.cur_solution = candidat

    def arcExist(self,i,j):
        if self.matrice_distance[i][j]!=0:
            return True
        return False

    def longueur(self,seq):
        return len(seq)    

    def distance(self,seq):
        cout=0
        if self.longueur(seq)>1:
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i]-1,seq[i+1]-1):
                    cout+=self.matrice_distance[seq[i]-1][seq[i+1]-1]
        return cout

    def Recuit(self):
        '''
        algorithme 
        '''
        while self.T >= self.stop_temp:
            candidat = copy.copy(self.cur_solution)
            l = random.randint(2, self.N-1)
            i = random.randint(0, self.N-l)
            candidat[i:(i+l)] = reversed(candidat[i:(i+l)])
            self.accept(candidat)
            self.T *= self.alpha

            self.f_list.append(self.cur_f)

        print("parcours ameliore:")
        print(self.best_solution)
        print("distance parcours ameliore:")
        print self.distance(self.best_solution)