withdraw = int (input("enter the withdrawl amount:"))
 
def balance(func):
    def securebalance(intialamount):
        if withdraw > intialamount:
            print(f"you dont have sufficent balance in your account ")
        elif withdraw < 0:
            print(f"the withdraw ammount should be greater than the 0")     
        else:
            intialamount -= withdraw
        return intialamount
    return securebalance    

@balance
def initalbalance(num):
    return initalbalance

print(f"remaining balance is {initalbalance(1000)}")

