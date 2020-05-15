def display():
    print("|SIZE || HARGA")
    print("______________")
    print("|S    || RM 45")
    print("|M    || RM 50")
    print("|L    || RM 55")
    print("\n\nWELCOME TO OUR SHOP ONLINE")
   
choose=0
total=0
while choose !=2:
    display()
    buy=input("Please choose your size and enter (eg : M) : ")
    if buy=="S" or buy=="s" :
          price=45
    elif buy=="M" or buy=="m":
          price=50
    elif buy=="L" or buy=="l":
          price=55
    else:
            input("You Input Wrong Key press Enter to continue  ")
            display()
        
    print ("RM :",price)

    total=price+total
    st=int(input ("PRESS 1 TO CONTINUE ADD MORE or 2 TO END SHOPPING: "))
    choose=st
    if choose==1:
        continue
    elif choose==2:
        break
    else :
        continue
    
print("YOUR TOTAL ITEM IS ")
print("RM ", total)
