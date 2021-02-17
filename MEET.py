#question:https://www.codechef.com/FEB21C/problems/MEET

from datetime import datetime
def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime <= endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime
t=int(input())
for _ in range(t):
    p=str(input())
    currentTime=""
    for each in p:
        if each!=" ":
            currentTime+=each
    n=int(input())
    l=[]
    for _ in range(n):
        time=[]
        starting,startingTime,ending,endingTime=map(str,input().split(" "))
        time.append(starting)
        time.append(startingTime)
        time.append(ending)
        time.append(endingTime)
        l.append(time)
    #print(l)
    answer=""
    for eachList in l:
        startTiming=eachList[0]+eachList[1]
        endTiming=eachList[2]+eachList[3]
        timeEnd = datetime.strptime(endTiming, "%I:%M%p")
        timeStart = datetime.strptime(startTiming, "%I:%M%p")
        timeNow = datetime.strptime(currentTime, "%I:%M%p")
        if  isNowInTimePeriod(timeStart,timeEnd,timeNow):
            answer+="1"
        else:
            answer+="0"
    print(answer)

        
