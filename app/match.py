# -*- coding: utf-8 -*-
class Match:

    def __init__(self, player1, player2, pacted_sets):
        self.contP1 = 0
        self.contP2 = 0
        self.ganadores = []
        self.scoreP1 = []
        self.scoreP2 = []
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets

    def score(self):
        if(len(self.ganadores) == 0):
            result = self.p1 + " plays with " + self.p2 + " | 0-0"
            return result
        else:
            if(self.contP1 > self.contP2):
                result = self.p1 + " defeated " + \
                    self.p2 + " | " + self.results(self.p1)
                return result
            elif(self.contP2 > self.contP1):
                result = self.p2 + " defeated " + \
                    self.p1 + " | " + self.results(self.p2)
                return result

    def results(self, p):
        if(p == self.p1):
            if(len(self.ganadores) == 2):
                scores = str(self.scoreP1[
                             0]) + "-" + str(self.scoreP2[0]) + ", " + str(self.scoreP1[1]) + "-" + str(self.scoreP2[1])
                return scores
            if(len(self.ganadores) == 3):
                scores = str(self.scoreP1[0]) + "-" + str(self.scoreP2[0]) + ", " + str(self.scoreP1[
                    1]) + "-" + str(self.scoreP2[1]) + ", " + str(self.scoreP1[2]) + "-" + str(self.scoreP2[2])
                return scores
            if(len(self.ganadores) == 5):
                scores = str(self.scoreP1[0]) + "-" + str(self.scoreP2[0]) + ", " + str(self.scoreP1[1]) + "-" + str(self.scoreP2[1]) + ", " + str(self.scoreP1[
                    2]) + "-" + str(self.scoreP2[2]) + ", " + str(self.scoreP1[3]) + "-" + str(self.scoreP2[3]) + ", " + str(self.scoreP1[4]) + "-" + str(self.scoreP2[4])
                return scores
        elif(p == self.p2):
            if(len(self.ganadores) == 2):
                scores = str(self.scoreP2[
                             0]) + "-" + str(self.scoreP1[0]) + ", " + str(self.scoreP2[1]) + "-" + str(self.scoreP1[1])
                return scores
            if(len(self.ganadores) == 3):
                scores = str(self.scoreP2[0]) + "-" + str(self.scoreP1[0]) + ", " + str(self.scoreP2[
                    1]) + "-" + str(self.scoreP1[1]) + ", " + str(self.scoreP2[2]) + "-" + str(self.scoreP1[2])
                return scores
            if(len(self.ganadores) == 5):
                scores = str(self.scoreP2[0]) + "-" + str(self.scoreP1[0]) + ", " + str(self.scoreP2[1]) + "-" + str(self.scoreP1[1]) + ", " + str(self.scoreP2[
                    2]) + "-" + str(self.scoreP1[2]) + ", " + str(self.scoreP2[3]) + "-" + str(self.scoreP1[3]) + ", " + str(self.scoreP2[4]) + "-" + str(self.scoreP1[4])
                return scores

    def asignar(self, p, num_set, n1, n2):
        if(p == self.p1):
            self.contP1 = self.contP1 + 1
            self.ganadores = self.ganadores + [p]
            self.scoreP1 = self.scoreP1 + [n1]
            self.scoreP2 = self.scoreP2 + [n2]

        elif(p == self.p2):
            self.contP2 = self.contP2 + 1
            self.ganadores = self.ganadores + [p]
            self.scoreP2 = self.scoreP2 + [n1]
            self.scoreP1 = self.scoreP1 + [n2]
