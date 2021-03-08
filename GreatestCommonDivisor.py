# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:59:37 2021

@author: user
"""
def gcd(num1,num2):
    if num2==0 :
        return num1
    else:
        return gcd(num2,num1%num2)
def main():
    a, b = eval(input("Please input two positive integers -- "))
    while (a>0 and b>0):
        print("GCD({0},{1}) = {2}".format( a, b, gcd(a,b) ) )
        a, b = eval(input("Please input two positive integers -- "))

if __name__ == "__main__":
    main()
