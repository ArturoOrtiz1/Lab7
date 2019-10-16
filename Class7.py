def main():
    print("This program calculates the total wages for a week")
    rate=float(input("What is the hourly pay rate? "))
    hours=float(input("How many hours did you work? "))
    if hours <= 40:
        print("You made", rate*hours ,"dollars")
    else:
        hrsover=hours-40
        print("You made" ,(rate*40+(hrsover*(1.5*rate))) , "dollars")

main()
