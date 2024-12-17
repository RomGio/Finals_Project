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
    print(f"0.Exit The Program")
    menuchoice = input("Enter The number of your Topic of Choice: ")
    if menuchoice == "1":
        def submenu1():
            print(f"{os.system('cls')}What Is Print In Python and What Is It Used For\nIn Python, the print() function is used to print the desired message on a device’s screen. \nThe Print is always in a string format. \nIf the print message is in other objects, it is first converted into a string before being printed. \nYou can input single or multiple objects of any type. \nBefore being printed the objects gets converted to a string \n0.Back")    
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
            print("Operators in Python are special symbols that perform operations on variables and values. \nThey are categorized into several types based on their functionality.\n0.Back")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu3()
        submenu3()     
    elif menuchoice == "4":
        def submenu4():
            print("Conditional statements in Python allow you to execute specific blocks of code based on whether a condition is true or false. \nThese statements are fundamental for controlling the flow of a program and making decisions. \nTypes of Conditional Statements\nIf Statement\nThe if statement is used to execute a block of code if a specified condition is true.\nIf-Else Statement\nThe if-else statement adds an additional block of code that executes if the condition is false.\nElif Statement\nThe elif (short for else if) statement allows you to check multiple conditions in sequence.\nNested If Statements\nYou can nest if statements within other if statements to create complex decision trees.")
            print("0.Back")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu4()
        submenu4()
    elif menuchoice == "5":
        def submenu5():
            print("A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).\nThis is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.\nWith the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.")
            print("0.Back")
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu5()
        submenu5()
    elif menuchoice == "6":
        def submenu6():
            print("Lists are used to store multiple items in a single variable.\nLists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.\nLists are created using square brackets")
            print("0.Back")            
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu6()
        submenu6()
    elif menuchoice == "7":
        def submenu7():
            print("A function is a block of code which only runs when it is called.\nYou can pass data, known as parameters, into a function.\nA function can return data as a result.\nCreating a Function\nIn Python a function is defined using the def keyword\nCalling a Function\nTo call a function, use the function name followed by parenthesis\nInformation can be passed into functions as arguments.\nArguments are specified after the function name, inside the parentheses.\nYou can add as many arguments as you want, just separate them with a comma.\nThe following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name\nPython also accepts function recursion, which means a defined function can call itself.\nRecursion is a common mathematical and programming concept. \nIt means that a function calls itself. \nThis has the benefit of meaning that you can loop through data to reach a result.\nThe developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. \nHowever, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.")
            print("0.Back")            
            back = input("Enter The Number of Choice: ")
            if back == "0":
                mainmenu()
            else:
                print("Unknown Choice")
                submenu7()
        submenu7()
    if menuchoice == "0":
        print("Program Exited")
    else:
        print("Unknown Option")
        mainmenu()
mainmenu()