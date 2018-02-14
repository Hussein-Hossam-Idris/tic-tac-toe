PB=[0,0,0,0,0,0,0,0,0]
fill=["_","_","_","_","_","_","_","_","_"]
choose=[0,1,2,3,4,5,6,7,8]
indexVS=["0","1","2","3","4","5","6","7","8"]
playerOneList=[1,3,5,7,9]
playerTwoList=[0,2,4,6,8]
condition = True

print ("*******Hello in Tic-Tac-Toe Game Made By Hussein*******")

#player one options
while condition:
    print("")
    print("")
    print("|",indexVS[0],"|",indexVS[1],"|",indexVS[2],"|")
    print("|",indexVS[3],"|",indexVS[4],"|",indexVS[5],"|")
    print("|",indexVS[6],"|",indexVS[7],"|",indexVS[8],"|")
    print("")
    print("")
    print("player One choose a number from the squares above: ")
    index=int(input("enter an index from the above slots: "))
    while index>=len(choose):
        index=int(input("index larger than lenght of list choose another one"))
    while (fill[index]!= "_"):
        index=int(input("this slot is already take choose another one"))
    print(playerOneList)
    num1=int(input("choose an index from the above list: "))
    while num1>=len(playerOneList):
        num1=int(input("index larger than lenght of list choose another one"))
    PB[index]=playerOneList[num1]
    fill[index]=playerOneList[num1]
    print("|",fill[0],"|",fill[1],"|",fill[2],"|")
    print("|",fill[3],"|",fill[4],"|",fill[5],"|")
    print("|",fill[6],"|",fill[7],"|",fill[8],"|")
    playerOneList.pop(num1)
    if((PB[0]+PB[1]+PB[2]==15) or (PB[3]+PB[4]+PB[5]==15) or (PB[6]+PB[7]+PB[8]==15)
        or (PB[0]+PB[3]+PB[6]==15) or (PB[1]+PB[4]+PB[7]==15) or (PB[2]+PB[5]+PB[8]==15)
        or (PB[0]+PB[4]+PB[8]==15) or (PB[2]+PB[4]+PB[6]==15)):
        print("PLAYER ONE WINS")
        break
    if (len(playerOneList)==0 and len(playerTwolist)==1):
        print("Draw!")
        break
    if (len(playerOneList)==1 and len(playerTwolist)==0):
        print("Draw!")
        break


    #player two settings
    print("")
    print("")
    print("|",indexVS[0],"|",indexVS[1],"|",indexVS[2],"|")
    print("|",indexVS[3],"|",indexVS[4],"|",indexVS[5],"|")
    print("|",indexVS[6],"|",indexVS[7],"|",indexVS[8],"|")
    print("")
    print("")
    print("player Two choose a number from the squares above: ")
    index=int(input("enter an index from the above slots: "))
    while index>=len(choose):
        index=int(input("index larger than lenght of list choose another one"))
    while (fill[index]!= "_"):
        index=int(input("this slot is already take choose another one"))
    print(playerTwoList)
    num2=int(input("choose an index from the above list: "))
    while num2>=len(playerTwoList):
        num2=int(input("index larger than lenght of list choose another one"))
    PB[index]=playerTwoList[num2]
    fill[index]=playerTwoList[num2]
    print("|",fill[0],"|",fill[1],"|",fill[2],"|")
    print("|",fill[3],"|",fill[4],"|",fill[5],"|")
    print("|",fill[6],"|",fill[7],"|",fill[8],"|")
    playerTwoList.pop(num2)
    if((PB[0]+PB[1]+PB[2]==15) or (PB[3]+PB[4]+PB[5]==15) or (PB[6]+PB[7]+PB[8]==15)
        or (PB[0]+PB[3]+PB[6]==15) or (PB[1]+PB[4]+PB[7]==15) or (PB[2]+PB[5]+PB[8]==15)
        or (PB[0]+PB[4]+PB[8]==15) or (PB[2]+PB[4]+PB[6]==15)):
        print("PLAYER TWO WINS")
        break
    if (len(playerOneList)==0 and len(playerTwolist)==1):
        print("Draw!")
        break
    if (len(playerOneList)==1 and len(playerTwolist)==0):
        print("Draw!")
        break


        
           
        
        
    
    
    
    
    
    


