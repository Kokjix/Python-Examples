#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Baran Berk Bağcı
"""
import numpy as np
import math

"""This code is wrote for HW2 quastion 2"""

def function(x): #regression functions when you give x values it is return y value.
    y = []
    for i in x:
        y.append(0.0224*math.pow(i,2) -(3.16132 * i) + 242.292) # Reggresion curve
    return y

def trapz(f,a,b,N): # Trapzeoid numeric method
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x) # y values
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    h = (b - a)/N # h value
    Trapzoid = (h/2) * np.sum(y_right + y_left) # Trapzeoid method
    return Trapzoid # Trapzeoid value returned

def simpson(f,a,b,N): # Simspons 1/3 rule
    x = np.linspace(a, b, N) # N+1 points make N subintervals
    h = (b - a) / (N - 1) # h value
    y = f(x) # regression function
    I_simp = (h/3) * (y[0] + 2*sum(y[:N-2:2]) + 4*sum(y[1:N-1:2]) + y[N-1]) # Simpson 1/3 rule
    return I_simp # Simpson value returned


if __name__ == "__main__": # main function
    T1 = trapz(function,20,70,10)# First Trapzoid
    T2 = trapz(function,70,120,20) # Second Trapzoid

    S1 = simpson(function,20,70,10) # First Simpson
    S2 = simpson(function,70,120,20) # Second Simpson

    print("\nMultiple Trapzoid: ",T1+T2) # Print trapzoid integral
    print("\nMultiple Simpson: ",S1+S2) # Print Sİmpson İntegral

    print("\nNormal Mean: ", 152.2727273) # Normal mean
    print("\nRegression Mean: ", 152.2156) # Regression mean

    error = 100 * (abs(152.2727273 - 152.2156)/152.2727273) # Regression and normal mean error

    print("\nMean Error: ", error) # Print error