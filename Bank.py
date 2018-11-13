def main():
    print("Money invested")
    money = int(input())
    print("Annual rate (0-1)")
    ar = float(input())
    print("Enter years into the future")
    years = int(input())
    newmoney = 0
    for i in range(years):
        newmoney = money*(1+ar)
        money = newmoney
    print("Your new money is:",float(newmoney))
    
main()
