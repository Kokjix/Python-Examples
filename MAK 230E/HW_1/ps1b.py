#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wendnesday Nov 18 01:44:42 2020

@author: Baran Berk Bağcı

"""

def hunt(months, salary_save, home_cost, semi_annual_raise):       ###############################################################################################
    current_save = 0                                               # This function's name is hunt and it is calculate the saving rate and semi annual rise value.#
                                                                   # This function take 4 parameter                                                              #
    while current_save < home_cost:                                ###############################################################################################                 
        months += 1
        rate_save = current_save * 0.04/12
        current_save += rate_save + salary_save

        if months % 6 == 0:
            salary_save += salary_save * semi_annual_raise

    return months









if __name__ == "__main__":
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream house: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
    
    salary = annual_salary / 12
    months = 0
    salary_save =  salary * portion_saved
    home_cost = total_cost * 0.25

    print("Number of months: ",hunt(months, salary_save, home_cost, semi_annual_raise))


    ######################################################################################
    # This is main function and it is take 4 input which are annual slary, portion save, # 
    # total cost and semi annual raise, an it is calculate monthly salary and salary save#
    ######################################################################################