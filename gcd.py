# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:49:20 2021

@author: user
"""

num1=int(input("number1:"))
num2=int(input("number2:"))
while num1!=0 and num2!=0 :
    if num1>=num2 :
        num1%=num2
    else:
        num2%=num1
print("The gcd of number1 and number2 : ",num1+num2)