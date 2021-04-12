#https://www.codechef.com/APRIL21B/problems/SDICE

t=int(input())
for _ in range(t):
    n=int(input())
    #n==1 hidden state=die1(1) 
    if n==1:
        print(20)
    #n==2 hidden state=die1(1,2) die2(1,2)
    elif n==2:
        print(36)
    #n==3 hidden sides=die1(1,2) die2(1,2,3) die3(1,2)
    elif n==3:
        print(51)
    #n==4 hidden sides=die1(1,2,3) die2(1,2,3) die3(1,2,3) die4(1,2,3)
    elif n==4:
        print(60)
    #n==5 hidden state=die1(1,2,3) die2(1,2,3) die3(1,2,3) die4(1,2,3,4) die5(1)
    elif n==5:
        print("76")
    #n==6 hidden state=die1(1,2,3,4) die2(1,2,3) die3(1,2,3) die4(1,2,3,4) die5(1,2) die6(1,2)  
    elif n==6:
        print("88")
    #n==7 hidden state=die1(1,2,3,4) die2(1,2,3,4) die3(1,2,3) die4(1,2,3,4) die5(1,2) die6(1,2,3) die7(1,2)
    elif n==7:
        print("99") 
    #now for bigger cases as every 4 dice there is a sequence
    else:
        reminder = n%4
        answer = ((n-reminder)//4)*44
        if reminder==0:
            answer+=16
        elif reminder==1:
            answer+=32
        elif reminder==2:
            answer+=44
        elif reminder==3:
            answer+=55
        print(answer)

