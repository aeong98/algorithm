function solution(id_list, report, k) {
    var answer = [];
    var user={};
    var getwarned={};
    var checkList={};
    
    for (var id of id_list){
        user={
            ...user,
            [id]:[]
        }
        
        getwarned={
            ...getwarned,
            [id]:0
        }
         
        checkList={
            ...checkList,
            [id]:0
        }
    }
    
    for (var rp of report){
        var [x, y]=rp.split(" ")
 
        // 신고당한 횟수 추가
        if(!user[x].includes(y)){
            getwarned[y]+=1
        }
        
        // 신고한 사람으로 추가
        user[x].push(y)
    }
    
    // 로직
    for (var id of id_list){
        if(getwarned[id]>=k){
            for (var id_ of id_list){
                if(user[id_].includes(id)){
                    checkList[id_]+=1
                }
            }
        }
    }
    
    // 값 추출 
    return Object.values(checkList);
}