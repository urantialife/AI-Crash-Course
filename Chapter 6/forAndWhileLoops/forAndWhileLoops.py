# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:16:59 2019

@author: janwa
"""

for i in range(1, 20):
    print(i)


L3 = [3,4,1,6,7,5]
for element in L3:
    print(element)
    
    
stop = False
i = 0
while stop == False:  #Alternatively it can be "while not stop:"
    i += 1
    print(i)
    if i >= 19:
        stop = True


L4 = [[2, 9, -5], [-1, 0, 4], [3, 1, 2]]
for row in L4:
    for element in row:
        print(element)
