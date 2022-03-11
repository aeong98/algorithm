from itertools import product

def solution(word):
    dict_list=[]
    for i in range(1,6):
        dict_list += list(map(''.join, product("AEIOU", repeat=i)))
    
    dict_list.sort()
    
    return dict_list.index(word)+1
