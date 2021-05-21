#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import statistics


def stat(n, lit):
    lit.sort()
    
    print("This is sorting of values:", lit)
    print("\nSample lenght is:",n)
    print("\nMode:", statistics.mode(lit))
    print("\nMode Multi:", statistics.multimode(lit))
    print("\nMean(int):",statistics.mean(lit))
    print("\nMean(float):",statistics.fmean(lit))
    print("\nMean grouped:", statistics.median_grouped(lit))
    print("\nMedian:", statistics.median(lit))
    print("\nLow Median:", statistics.median_low(lit))
    print("\nHigh Median:", statistics.median_high(lit))
    print("\nCeyrekler Acikligi:", statistics.median_high(lit) - statistics.median_low(lit))
    print("\nStandard Deviation of Sample is:", statistics.stdev(lit))
    print("\nStandard Variance of the Sample is:", statistics.variance(lit))
    print("\nPopulation Deviation of the Sample is:", statistics.pstdev(lit))
    print("\nPopulation Variance of the Sample is:", statistics.pvariance(lit))





    

    





if __name__ == '__main__':

    x = eval(input("Do you wish to continue[Y = 1/ N = 0]:"))
    
    while (x == 1):

        

        n = int(input("Enter number of elements : ")) 
  
        # Below line read inputs from user using map() function  
        lit = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 

        stat(n, lit)
        print("\n",lit)

        x = x + 1
        
        x = int(input("Do you wish to continue[Y = 1/ N = 0]:"))

    
        
    