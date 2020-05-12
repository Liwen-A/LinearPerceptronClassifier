#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:32:05 2020
Calculates the policy evaluation problem given in hw6
@author: liwenouyang
"""
def policyEval(P,U,R,gamma = 0.5):
    """
    Policy as a dic
    U,R as 2-d list 
    """
    NU = []
    for i in U:
        NU.append(i.copy())
    for i in range(len(U)):
        for j in range(len(U)):
            a,b = P[(i,j)]
            NU[i][j] = R[i][j]+ gamma*U[a][b]
    return NU


P = {(0,0):(1,0), (0,1):(1,1),(0,2):(1,2),
     (1,0):(2,0), (1,1):(2,1), (1,2):(2,2),
     (2,0):(2,1), (2,1): (2,2), (2,2):(2,2)
     }


U =[]
for i in range(3):
    U.append([0]*3)


R =[[0,0,0],[0,0,0],[-1,0,1]]


class RL:
    
    def __init__(self,P,R,gamma,U):
        self.P = P
        self.R = R
        self.gamma = gamma
        self.U = U
        
    def policyEval(self):
        NU = []
        for i in self.U:
            NU.append(i.copy())
        for i in range(len(NU)):
            for j in range(len(NU)):
                a,b = self.P[(i,j)]
                NU[i][j] = self.R[i][j]+ self.gamma * self.U[a][b]
        self.U = NU
        
        
M = RL(P,R,0.5,U)

for i in range(100):
    M.policyEval()
    print(M.U)