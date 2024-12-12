c=int(input("Enter the no:\n"))
match c:
    case 0:
        print("IT is zero")
    case _ if 10<=c<=20:
        print("Enough")
    case  _:
        print("Done")