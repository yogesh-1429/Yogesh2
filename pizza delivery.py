print("welcome to the pizza order!")
pizza=input("do you want pizza:")
if pizza=="yes":
    print("buy pizza")
    size=input("pizza size:")
    if size=="small":
        bill=15
        print("pay rupess 15")
    elif size=="medium":
        bill=20
        print("pay rupess 20")
    elif size=="large":
        bill=25
        print("pay rupess 25")
    else:
        print("no need")
    add_pepperoni=input("do you want pepperoni for small pizza:")
    if add_pepperoni=="yes":
        bill=bill+2
    else:
        print("not needed")
    pepperoni=input("do u need peperoni for med or large size pizza:")
    if pepperoni=="yes":
        bill=bill+3
    else:
        print("not needed")    
    
    
    extra=input("if need any extra cheese:")
    if extra=="yes":
        bill=bill+1
    else:
        print("not needed")
    print(f"your final bill is : {bill}")            

else:
    print("not needed")    



