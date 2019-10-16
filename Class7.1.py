def main():
    print("This program calculates the class standing from the number of credits earned")
    x=float(input("How many credits do you have? "))
    if x<=6:
        print("You are a Freshman!")
    elif x<=15:
        print("You are a Sophomore!")
    elif x<=25:
        print("You are a Junior!")
    else:
        print("You are a Senior!")
main()
