#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wendnesday Nov 18 01:44:42 2020

@author: Baran Berk Bağcı

"""

def hunt(months, starting_salary, home_cost, semi_annual_raise, max_rate, min_rate):
    #current_save = 0
    portion_saved = int((max_rate + min_rate) / 2)

    months = 36
    steps = 0
    found = False
     

    while abs(min_rate - max_rate) > 1:
        steps += 1
        annual_salary = starting_salary
        
        
        #rate_save = current_save * 0.04/12
          
        monthly_saved = (annual_salary / 12.0) * (portion_saved/10000)
        current_save = 0.0
        
        for i in range(1, months + 1):
            monthly_return = current_save * (0.04/12)
            current_save += monthly_return + monthly_saved

            if abs(current_save - home_cost) < 100:
                min_rate = max_rate
                found = True
                break
            
            elif current_save > home_cost + 100:
                break
            if i % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise
                monthly_saved = (annual_salary / 12.0) * (portion_saved/10000)

        if current_save < home_cost - 100:
            min_rate = portion_saved

        elif current_save > home_cost + 100:
            max_rate = portion_saved

        portion_saved = int((max_rate + min_rate) / 2)

        
    if found:
        print("Best savings rate: ", portion_saved/10000)
        print("Steps in bisection search: ", steps)

    else:
        print("Is is not possible to pay the down payment in three years.")

    ##############################################################################################
    # hunt function calculete best interest rate in order to                                     #
    # buy a 250000$ house in 3 years by using bisection method wich has max 1000 and min 0 value.#
    ##############################################################################################








if __name__ == "__main__":
    starting_salary = int(input("Enter your annual salary: "))
    
    total_cost = 1000000
    semi_annual_raise = .07
    
    min_rate = 0        
    max_rate = 10000
    
    
    
    months = 0
    home_cost = total_cost * 0.25

    hunt(months, starting_salary, home_cost, semi_annual_raise, max_rate, min_rate)

    #main function execute hunt function