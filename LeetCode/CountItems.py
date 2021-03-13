#link: https://leetcode.com/contest/weekly-contest-230/problems/count-items-matching-a-rule/
def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    types=0
    color=0
    name=0
    count=0
    for each in items:
        if ruleKey==color:
            x=each[1]
            if x==ruleValue:
                count+=1
        elif ruleKey==type:
            x=each[0]
            if x==ruleValue:
                count+=1 
        elif ruleKey==name:
            x=each[2]
            if x==ruleValue:
                count+=1   
    return count        

l=[]
ruleKey=str(input())
ruleValue=str(input())
x=print(countMatches(l,ruleKey,ruleValue))
