P=int(input("Enter value of p:"))
Q=int(input("Enter value of q:"))

while True:
    ruleNo=int(input("Enter rule np for solving waterjug problem :"))
    if ruleNo==1:
       if P<4:
            P=4
            
    if ruleNo==2:
        if Q<3:
            Q=3
            
    if ruleNo==5:
        if P>0:
            p=0
            
    if ruleNo==6:
        if Q>0:
            Q=0
            
    if ruleNo==7:
        if P+Q>=4 and Q>0:
            P,Q=4,Q-(4-P)
            
    if ruleNo==8:
        if P+Q>=3 and P>0:
            P,Q=P-(3-Q),3
    
    if ruleNo==9:
        if P+Q<=4 and Q>0:
            P,Q=P+Q,0
            
    if ruleNo==10:
        if P+Q<-3 and P>0:
            P,Q=0,P+Q
        
    print("P=",P)
    print("Q=",Q) 

    if(P==2):
        print("Now we are reached at goal state")