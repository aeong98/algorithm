from itertools import combinations
import math 

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i ==0:
            return False
    return True

def solution(nums):
    cnt=0
    combination=list(combinations(nums,3))
    for com in combination:
        if(is_prime_number(sum(com))):
            cnt +=1
    return cnt
