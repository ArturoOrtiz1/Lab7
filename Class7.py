
def main():
    print("This program calculates the total wages for a week")
    x=float(input("What is the hourly pay rate? "))
    y=float(input("How many hours did you work? "))
    if y <= 40:
        print("You made ", x*y ,"dollars")
    if y > 40:
        print("You made " ,((x*1.5)*y), "dollars")

main()
