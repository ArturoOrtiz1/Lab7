def main():
    print("This program determines the amount of fine given the clocked speed and speed limit")
    clocked=int(input("What was the clocked speed in Podunksville? "))
    limit=int(input("What was the speed limit? "))
    
    if clocked<=limit:
        # Not speeding
        print("This is not illegal")
    else:
        # Speeding
        fine= 50+(clocked-limit)*5
        
        if clocked>90:
            # REALLY speeding
            fine=fine+200
            
        print("Your fine is: ", fine , "dollars")
    
main()
