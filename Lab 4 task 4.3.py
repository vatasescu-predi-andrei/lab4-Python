#task 4.3
print("Welcome to the Currency Converter'\n', 1)=Converting Pounds to Euros '\n', 2)Convert Euros to Pounds")
option=int(input("Which option would you like?"))
if option==1:
    amount=float(input("Please enter your amount: £"))
    conversion= amount*1.12
    print("%.2fPounds is %.2f in Euros" %(amount,conversion))
elif option==2:
    amount=float(input("Please enter your amount: €"))
    conversion= amount*0.99
    print("%.2fEuros is %.2f in Pounds" %(amount,conversion))
