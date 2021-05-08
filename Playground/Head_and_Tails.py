#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random

class Coin(object): #Coin object that has side dictionary 

    def __init__(self):
        self.sides = {'Heads': 0, 'Tails': 0} # Number of tails and heads


coin = Coin()

def flip(n):
    
    stepsH = []
    stepsT = []
    turns = []
    propH = []
    
    for flip in range(n):
        a = random.randint(0,1)
        
        if a == 0:
            coin.sides['Heads'] += 1 

            a = 2
        elif a == 1:
            coin.sides['Tails'] += 1
            a = 2
        
        stepsH.append(coin.sides['Heads']) # StepH contain number of Heads
        stepsT.append(coin.sides['Tails']) # StepT contain number of Tails
        turns.append(flip)
        propH.append(stepsH[flip] / (turns[flip] + 1)) # Contains probibilty of Heads
    
    #print("Flip: " + str(flip + 1) + " Heads: " + str(stepsH) + " Tails: " + str(stepsT) + " Propotions of Head: " + str(propH))    
    print("Heads: " + str(coin.sides['Heads']) + " Tails: " + str(coin.sides['Tails']))
    fig, ax = plt.subplots()
    ax = plt.scatter(turns, propH, s = 6, c = '#750e0e') # Scatter plot
    plt.xlabel("Flips") 
    plt.ylabel("Propotions of Head") 
    plt.title("Coin Flip Probability")
    plt.grid()
    plt.show()

    


if __name__ == '__main__':         
    
    n = int(input("Number of Flip: ")) # Number of flips 
    flip(n)