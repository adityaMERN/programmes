
n=int(input())
d={}
l=[]
for i in range(n):
    calender=str(input())
    value=int(input())
    l.append([calender,value])
for j in l:
    #if j[0] not in l:
        d[j[0]]=j[1]
#print(d)
import calendar
def dayData(data):
        year,month,day=map(int,data.split("-"))
        dayNumber = calendar.weekday(year, month, day)
        days =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"] 
        return days[dayNumber]
def missing_date(d):
    startDate=list(d.keys())[0]
    #print(startDate)
    start=list(map(int,startDate.split("-")))
    lastDate=list(d.keys())[-1]
    last=list(map(int,lastDate.split("-")))
    dictionary={}
    finalList=[]
    for key in d:
        startYear,startMonth,startDay=map(int,key.split("-"))
        finalList.append(startDay)
    for k in range(start[2],last[2]+1):
        if k in finalList:
            continue
        else:
            if len(str(startMonth))==1:
                startMonth="0"+str(startMonth)
            if len(str(k))==1:
                k="0"+str(k)
            return [str(startYear)+"-"+str(startMonth)+"-"+str(k),start[2],last[2]]
def nextDate(date):
    year,month,day=map(int,date.split("-"))
    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    if len(str(month))==1:
        month="0"+str(month)
    if len(str(day))==1:
        day="0"+str(day)
    return str(year)+"-"+str(month)+"-"+str(day)

answer=missing_date(d)

#answer[0] use karo
#print (answer)
#print(dateList)
if len(d)!=answer[2]-answe[1]+1:
newList=[]
for key in d:
    newList.append([list(map(str,key.split("-"))),d[key]])
#print(newList)
xxxx=list(map(str,answer[0].split("-")))[2]
#print(xxxx)
for k in range(len(newList)):
    if int(xxxx)-int(newList[k][0][2])==1:
        real=newList[k][0]
        ssss="-".join(real)
        nextOne=nextDate(ssss)
        xyz="-".join(newList[k][0])
        #print(x)
        # 
        newList[k]=[[xyz],newList[k][1]]
        newList.insert(int(k)+1,[[nextOne],0])
        break
#print(newList)
for i in range(len(newList)):
    #print(len(newList[i][0]))
    if len (newList[i][0])>1:
       
        xyz="-".join(newList[i][0])
        newList[i]=[xyz,newList[i][1]]
        #print(newList[i])

print(newList)
newestDict={}

dateList=[]
for key in d:
    x=dayData(key)
    dateList.append([x,d[key]])


mondayvalue=0
tuesdayvalue=0
wednesdayvalue=0
thrusdayvalue=0
fridayvalue=0
saturdayvalue=0
sundayvalue=0


       


