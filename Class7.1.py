def main():
    print("This program calculates the class standing from the number of credits earned")
    x=float(input("How many credits do you have? "))
    if x<7:
        print("You are a Freshman!")
    elif x<=15 or x is 7:
        print("You are a Sophomore!")
    elif x<=25 or x is 16:
        print("You are a Junior!")
    elif x>=26:
        print("You are a Senior!")
main()
