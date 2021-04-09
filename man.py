#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from deneme import *

li = Deneme()
li2 = Deneme()
max_Reach = 74.85


def crd_multipication(point, factor):
    cord = []
    new_x = factor * point[0]
    new_y = factor * point[1]
    new_z = factor * point[2]

    cord.append(new_x)
    cord.append(new_y)
    cord.append(new_z)
    
    return cord 


if __name__ == "__main__":
    

    li.axes[0] = 1
    li.axes[1] = 2
    li.axes[2] = 3


    li2.axes[0] = 1
    li2.axes[1] = 2
    li2.axes[2] = 3
    
    result = dot_product(li.axes, li2.axes)
    #crd_multipication(li.axes, 2)
  	
	
    print(crd_multipication(li.axes, 2)[0])
