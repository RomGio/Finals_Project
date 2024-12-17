import os
def mainmenu():
    os.system('cls')
    print(f"This Menu Contains The Topics For Coding in Python")
    print(f"1.Print Statements")
    print(f"2.Variables")
    print(f"3.Operators")
    print(f"4.Conditionals")
    print(f"5.Loops")
    print(f"6.Lists")
    print(f"7.Functions")
    menuchoice = input("Enter The number of your Topic of Choice: ")
    if menuchoice == "1":
        def submenu1():
            print(f"{os.system('cls')}What Is Print In Python and What Is It Used For\nIn Python, the print() function is used to print the desired message on a device’s screen. \nThe Print is always in a string format. \nIf the print message is in other objects, it is first converted into a string before being printed. \nYou can input single or multiple objects of any type. \nBefore being printed the objects gets converted to a string\n0.Back")    
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice") 
                submenu1()
        submenu1()   
            
    elif menuchoice == "2":
        def submenu2():
            print(f"{os.system('cls')}Variables\nVariables are containers for storing data values.\nCreating Variables\nPython has no command for declaring a variable.\nA variable is created the moment you first assign a value to it.")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu2()
        submenu2()
    elif menuchoice == "3":
        def submenu3():
            print("")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu3()
        submenu3()     
    elif menuchoice == "4":
        def submenu4():
            print("")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu4()
        submenu4()
    elif menuchoice == "5":
        def submenu5():
            print("")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu5()
        submenu5()
    elif menuchoice == "6":
        def submenu6():
            print("")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu6()
        submenu6()
    elif menuchoice == "7":
        def submenu7():
            print("")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu7()
        submenu7()
    else:
        print("Unknown Option")
        mainmenu()
mainmenu()