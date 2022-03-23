// index 0: winner, 1 :looser
function findWinner(x,y){
    if(x=="S"){
        if(y=="P") return ["S","P"]
        else if(y=="R") return ["R","S"]
    }
    else if(x=="P"){
        if(y=="S") return ["S","P"]
        else if(y=="R") return ["P","R"]
    }
    else{
        if(y=="S") return ["R","S"]
        else if(y=="P") return ["P","R"]
    }
}


function solution(n, m, points, hands) {
    var answer = 0;
    const scoreList = Array.from(Array(n), ()=>0);
    var score=0;

    // 라운드 실행  
    for (let i=0; i<m; i++){
        const handsArray=hands[i].split('');
        // // 모양 종류
        const kind=Array.from(new Set(handsArray));

        // 1. 모양 한개일때, 
        if(kind.length === 1){
            // 다음 라운드로 넘어가고, 점수 합쳐짐
            score +=points[i];
            continue;
        }
        // 2. 모양 2개일 때,
        else if(kind.length==2){
            // 점수가 0 이상인경우
            if(points[i]>=0){
                // 가위바위보를 이긴 그룹
                var winner=findWinner(kind[0],kind[1])[0]
                score+=points[i]
                // 이긴 그룹에 속해있는 사람들이 점수를 가져감.
                handsArray.map((hd,j)=>{
                    if(hd===winner){
                        scoreList[j]+=score
                    }
                })
                score=0;
                continue
            }
            // 점수가 음수인경우
            else{
                // 가위바위보를 진 그룹이 점수를 가져감.
                var looser=findWinner(kind[0], kind[1])[1]
                score+=points[i];
                handsArray.map((hd,j)=>{
                    if(hd===looser){
                        scoreList[j]+=score
                    }
                })
                score=0;
                continue;
            }

        }
        // 3. 모양 3개일 때,
        else{
            var SGroup=[];
            var PGroup=[];
            var RGroup=[];
            for (let i=0; i<handsArray.length ;i++){
                if(handsArray[i]==='S'){
                    SGroup.push(handsArray[i])
                }
                else if(handsArray[i]==='P'){
                    PGroup.push(handsArray[i])
                }
                else {
                    RGroup.push(handsArray[i])
                }
            }
            // 3-1. 세그룹의 크기가 모두 같은 경우
            if((SGroup.length === PGroup.length) && (PGroup.length=== RGroup.length)){
                score+=points[i]
                continue
            }
            // 3-2. 두 그룹의 크기가 같은 경우
            else if(SGroup.length===PGroup.length){
                score += points[i];
                handsArray.map((hd,j)=>{
                    if(hd==="R"){
                        scoreList[j]+=score
                    }
                })
                score=0;
                continue;
            }
            else if(SGroup.length===RGroup.length){
                score += points[i];
                handsArray.map((hd,j)=>{
                    if(hd==="P"){
                        scoreList[j]+=score
                    }
                })                
                score=0;
                continue;
            } 
            else if(PGroup.length===RGroup.length){
                score += points[i];
                handsArray.map((hd,j)=>{
                    if(hd==="S"){
                        scoreList[j]+=score
                    }
                })
                score=0;
                continue;
            }
            // 3-3. 그룹의 크기가 모두 다른 경우
            else{
                //크기가 가장 크고 작은 그룹의 인덱스 구하
                const Type =["S", "P", "R"];
                const maxIndex=[SGroup.length, PGroup.length, RGroup.length].indexOf(Math.max(SGroup.length, PGroup.length, RGroup.length));
                const minIndex=[SGroup.length, PGroup.length, RGroup.length].indexOf(Math.min(SGroup.length, PGroup.length, RGroup.length));
                if (points[i] >=0){
                    // 그룹의 크기 가장 큰 그룹 제외
                    const parsedType= Type.filter((tp)=> tp!==Type[maxIndex]);
                    // 가위바위보를 이긴 그룹
                    var winner=findWinner(parsedType[0],parsedType[1])[0]
                    score+=points[i]
                    // 이긴 그룹에 속해있는 사람들이 점수를 가져감.
                    handsArray.map((hd,j)=>{
                        if(hd===winner){
                            scoreList[j]+=score
                        }
                    })
                    score=0;
                    continue
                }
                else{
                    // 그룹의 크기 가장 작은 그룹 제외
                    const parsedType= Type.filter((tp)=> tp!==Type[minIndex]);
                    // 가위바위보를 진 그룹
                    var looser=findWinner(parsedType[0],parsedType[1])[1]
                    score+=points[i]
                    // 진 그룹에 속해있는 사람들이 점수를 가져감.
                    handsArray.map((hd,j)=>{
                        if(hd===looser){
                            scoreList[j]+=score
                        }
                    })
                    score=0;
                    continue
                }
                
            }

        }
    }
    var maxResult=-1000009;
    for (sc of scoreList){
        if(sc>maxResult){
            maxResult=sc
        }
    }
    return maxResult;
}