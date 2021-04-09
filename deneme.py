#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Deneme():

    def __init__(self):
        self.axes = [0, 0, 0]

def dot_product(point1, point2):
    

    result = 0.0

    result += point1[0] * point2[0]
    result += point1[1] * point2[1]   #Tek satırda yazmayı dene 
    result += point1[2] * point2[2]

    return result