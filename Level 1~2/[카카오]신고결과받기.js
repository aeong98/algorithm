function solution(id_list, report, k) {
    let sendDict={};
    let getDict={};
    let overK=[];
    
    for (let id of id_list){
        sendDict[id]=[]
        getDict[id]=0
    }
    
    for (let re of report){
        const [send, get]=re.split(" ")
        if(!sendDict[send].includes(get)){
            sendDict[send].push(get)
            getDict[get]+=1       
        }
    }

    for (let key of Object.keys(getDict)){
        if(getDict[key]>=k){
            overK.push(key)
        }
    }

    let answer=[];
    for (let key of Object.keys(sendDict)){
        let cnt=0;
        let values=sendDict[key]
        overK.map(over=> values.includes(over)?cnt+=1:cnt)
        answer.push(cnt)
    }
    return answer;
}