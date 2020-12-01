#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wendnesday Nov 18 01:44:42 2020

@author: Baran Berk Bağcı

"""



def hunt(months, salary_save, home_cost):          #####################################################################################################
    current_save = 0                               # This hunt function calculete monthly saving and also calculate how long it is take to buy a house.#
                                                   #####################################################################################################
    while current_save < home_cost:
        months += 1
        rate_save = current_save * 0.04/12
        current_save += rate_save + salary_save

    return months









if __name__ == "__main__":
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream house: "))
    
    salary = annual_salary / 12
    months = 0
    salary_save =  salary * portion_saved
    home_cost = total_cost * 0.25

    print("Number of months: ",hunt(months, salary_save, home_cost))


    ###########################################################################
    #This is main function and it take input values and exucute hunt function.#
    ###########################################################################