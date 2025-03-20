print("Welcom")
total_bill = int(input("total bill "))
tip = int(input("tip "))/100
spit = int(input("spit"))
pay= (total_bill*(tip/spit))
rpay=round(pay,2)
print(f"eachperson pay ${rpay}")
