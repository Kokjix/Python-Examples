#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:21:42 2020

@author: Baran Berk Bağcı

"""
import numpy as np

def isPowerOfTwo(n): # isPowerOfTwo function decide that number is power of two or not if number is poweroftwo therefore function return True or else it return False 
    if (n == 0): 
        return False                ###################################################
    while (n != 1):                 # While loop controln value if it is power of two #
            if (n % 2 != 0):        ###################################################                                                   
                return False        
            n = n // 2
              
    return True

def task(x, y): #define task function 
    res1 = x**y      # res1 variable that store x to the power y

    if isPowerOfTwo(x):
        res2 = int(np.log2(x)) # res2 variable store base 2 log of variable x log is method from numpy library if x is power of two therefore res2 value is int

    else:
        res2 = np.log2(x) # res2 variable store base 2 log of variable x log is method from numpy library if x is not a poweroff two therefore res2 is float

    str1 = "X**y = " + str(res1) #str1 is string 
    str2 = "log(x) = " + str(res2) #str2 is string
    
    print(str1) #print function print st1 string
    print(str2) #print function print st2 string


if __name__ == '__main__': #run main function
    x = input("Enter number x:") #x variable store from input function which take variable from user
    y = input("Enter number y:") #y variable store from input function which take variable from user

    task(int(x), int(y)) #run task function


