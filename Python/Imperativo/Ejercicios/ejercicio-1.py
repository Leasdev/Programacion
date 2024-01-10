""" 1) Given an integer array nums and an integer val, remove all occurrences of val in num in-place. 
    The order of the elements may be changed. then return the number of elements in nums which are not equal to val.

    Consider the number if elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
    The remaining elements of nums are not important as wall as the size of nums.
    return k."""
from random import *
import os 

# Funciones   
def crear_array():    
    entrada = "1"
    nums = []    
    
    while entrada.isnumeric():
        entrada = input("Ingrese un numero: ")
        if entrada.isnumeric():
            nums.append(int(entrada))
    return nums

def remove_element(nums, val):
    k = 0
    while val in nums: 
        nums.remove(val)
        k += 1
    return k

# Main
array = crear_array()
os.system("cls")
val = array[randint(0, len(array)-1)]

print("array: %s" %(array))
print("valor: %s" %(val))

k = remove_element(array, val)
print("se removio (%s) %s veces y queda: " %(val, k))
print("array: %s" %(array))









