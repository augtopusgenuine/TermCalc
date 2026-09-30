print("TermCalc v0.4")
while (True) :

    val1 = input("Enter your first value >>> ")

    val2 = input("Enter your second value >>> ")

    oper = input("Select your operation: \n" + "(1) + \n" + "(2) - \n" + "(3) * \n" + "(4) / \n" + "(5) ^ \n" + ">>> ")

    if oper in {"1", "2", "3", "4", "5"} :
    
        if oper == "1" :
            result = int(val1) + int(val2)
            print("The sum is: ", result)

        elif oper == "2" :
            result = int(val1) - int(val2)
            print("The difference is: ", result)

        elif oper == "3" :
            result = int(val1) * int(val2)
            print("The product is: ", result)

        elif oper == "4" :
            if val2 == "0":
                print("Error: Cannot divide by zero!")
            else:
                result = int(val1) / int(val2)
                print("The quotient is >>> ", result)
    
        elif oper == "5":
            result = int(val1) ** int(val2)
            print("The power is >>> ", result)

    else:
        print("Error: Not a valid operation!")    

    rep = input("Calculate another? Y/n \n" + ">>> ")

    if rep == "y" :
        print("Calculating another!")
        continue

    if rep == "n" :
        print("Done!")
        break
