def main():
    print("This program determines the amount of fine given the clocked speed and speed limit")
    cs=int(input("What was the clocked speed in Podunksville? "))
    sl=int(input("What was the speed limit? "))
    fine= 50
    x=cs-sl
    y=fine+(x*5)
    if cs<=sl:
        print("This is not illegal")
    elif cs>sl and cs<90:
        print("Your fine is: ", y , "dollars")
    elif cs>sl and cs>90:
        print("Your fine is: ", (y+ 200), "dollars, which includes a $200 penalty charge for going over 90mph")
main()
