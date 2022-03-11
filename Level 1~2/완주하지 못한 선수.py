def solution(participant, completion):
    hash_dict={}
    for com in completion:
        if com not in hash_dict.keys():
            hash_dict[com]=1
        else:
            hash_dict[com]+=1
            
    for part in participant:
        if(part not in hash_dict.keys()):
            return part
        else:
            hash_dict[part]-=1
        
        if(hash_dict[part] < 0 ):
            return part
