# LIAW YUNG SIANG
# TP072251
# ****************************Pre-input************************************Tuesday
# Pre-create lists of information for testing purposes
listHeading = ["EmployeeName", "EmployeeID", "Department", "BasicSalary", "Allowance", "Bonus", "Overtime",
               "TotalSalary", "Month"]
listMonth = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "end"]

# Employees lists   # For testing purposes
list1o = ["James", "9901", "Management", "2000", "500", "1000", "200", "3095", "oct"]
list1n = ["James", "9901", "Management", "3000", "500", "1000", "200", "3932", "nov"]
list1d = ["James", "9901", "Management", "4000", "500", "1000", "200", "4768", "dec"]
list2d = ["Ryan", "9902", "Production", "5000", "500", "1000", "200", "5605", "dec"]
list3d = ["Jamie", "9903", "IT", "2000", "500", "100", "1000", "3011", "dec"]
list4d = ["Rose", "0001", "IT", "4000", "500", "500", "0", "4183", "dec"]
list5d = ["Byron", "0002", "IT", "1500", "200", "0", "200", "1775", "dec"]

Admin = ["9901", "9902", "9903"]

employee_list = [list1o, list1n, list1d, list2d, list3d, list4d, list5d]

CurrentMonth = "dec"
#  Declare all the global variable:
global i
global j
global Allowance
global BasicSalary
global Bonus
global Count
global Count2
global Decision
global EmpID
global IndexLocation
global InputAns1
global InputMonth
global InputMonthTest
global InputMonthCheck
global NameSearch
global Overtime
global RetryViewPay
global Salary
global TempID
global TempInput
global TempList
global TempName
global User1
global UserID


# ********************************Functions*****************************************
def exitProgram():  # To print exit message to the user and end the program.
    print("\nYou selected <Exit Program>")
    print("\n", "**************************************************\n",
          "  Thank you for using Payroll Management System.\n",
          "**************************************************\n")


def checkInput(input_ans):  # Check if the user input is valid, integer and specifically given from the output.
    global User1
    print("Check Input and Integer:\n")
    try:
        input_int1 = int(input_ans)  # Change the user input to integer; perform an integer check.
        User1 = input_int1  # Check for specific input, only accept 1, 2, 3, and 0.
        if User1 != 1 and User1 != 2 and User1 != 3 and User1 != 0:
            User1 = input("Invalid input please enter <0, 1, 2 or 3> to proceed:\n")
            checkInput(User1)  # Recall the function to allow the user to re-enter/ retry.
        else:
            pass
    except ValueError:  # If error is found, the user input is not an integer value.
        User1 = input("Invalid input please enter <0, 1, 2 or 3> to proceed:\n")
        checkInput(User1)


def checkInput2(input_ans):  # Recreated checkInput for 3 inputs only
    global User1
    print("Check Input and Integer:\n")
    try:
        input_int1 = int(input_ans)  # Change the user input to integer; perform an integer check.
        User1 = input_int1  # Check for specific input, only accept 1, 2, and 0.
        if User1 != 1 and User1 != 2 and User1 != 0:
            User1 = input("Invalid input please enter <0, 1, or 2> to proceed:\n")
            checkInput2(User1)  # Recall the function to allow the user to re-enter/ retry.
        else:
            pass
    except ValueError:  # If error is found, the user input is not an integer value.
        User1 = input("Invalid input please enter <0, 1, or 2> to proceed:\n")
        checkInput2(User1)


#  Main Menu:
def mainMenu():
    global User1
    print("\n*********************PAYROLL*********************", "\n1. Employee Profile", "\n2. Salary Generator",
          "\n3. Pay Slip", "\n0. Exit Program", "\n ")  # Display all the possible input for the user.
    User1 = input("Please enter <0-3> to proceed:\n")
    checkInput(User1)  # Check if the input is valid.
    print("Valid input:", User1)
    mainCheckNext(User1)  # Check and proceed to the next menu bases on the user input.


def mainCheckNext(input_ans):  # Check and proceed to the next menu bases on the user input.
    if input_ans == 1:
        print("\nYou selected <Employee Profile>")
        empMenu()  # Proceed to Employee Profile.
    elif input_ans == 2:
        print("\nYou selected <Salary Generator>")
        generateSalary()  # Proceed to Salary Generator.
    elif input_ans == 3:
        print("\nYou selected <Pay Slip>")
        paySlipMenu()  # Proceed to Pay Slip.
    elif input_ans == 0:
        exitProgram()  # End the Program.
    else:
        pass


def returnMain():  # For the user to return to the main menu and allow the user to re-enter for any available function.
    print("You selected <Return to Main Menu>\n")
    mainMenu()


#  Employee Profile:
def empMenu():  # Display all the possible options for Employee profile.
    global User1
    print("\n*********************<Employee Profile>*********************", "\n1. Add Employee", "\n2. Update Employee",
          "\n3. Delete Employee", "\n0. Return to Main Menu", "\n ")
    User1 = input("Please enter <0, 1, 2, or 3> to proceed:\n")
    checkInput(User1)  # Check if the input is valid.
    print("Valid input:", User1)
    empCheckNext(User1)  # Check input and proceed to the selected function.


def empCheckNext(input_ans):  # Proceed to the next menu selected by the user.
    if input_ans == 1:
        print("You selected <Add Employee>")
        addEmployee()  # Proceed to add employee
    elif input_ans == 2:
        print("You selected <Update Employee>")
        updateEmployee()  # Proceed to update employee
    elif input_ans == 3:
        print("You selected <Delete Employee>")
        deleteEmployee()  # Proceed to delete employee
    elif User1 == 0:
        returnMain()  # Return to Main Menu
    else:
        pass


#  Employee Profile -> Add Employee
def addEmployee():  # Add new employee profile.
    global i
    global Allowance
    global BasicSalary
    global Bonus
    global CurrentMonth
    global TempID
    global TempName
    global Overtime
    i = 0
    TempName = input("Please input your name for verification:\n")
    TempName = TempName.lower()  # Save input to check for name in the library.
    while i <= len(employee_list) and (i >= 0):
        if i >= len(employee_list):
            i = -10  # Redefine i to end the loop.
            print("Employee not found. Proceed to <Adding Employee>")  # Name not found so can be added as new employee
            EmployeeName = input("Please enter your Name: \n")  # Save name
            EmployeeID = input("Please enter your ID: \n")  # Save ID
            Department = input("Please enter your Department: \n")  # Save Department
            Input1 = input("Please enter your Basic Salary: \n")  # Temporary save input for basic salary
            checkBasicSalary(Input1)  # Check if the input is integer, if true save input as basic salary
            print(BasicSalary)
            Input1 = input("Please enter your Allowance: \n")  # Temporary save input for allowance
            checkAllowance(Input1)  # Check if the input is integer, if true save input as allowance
            print(Allowance)
            Input1 = input("Please enter your Bonus: \n")  # Temporary save input for bonus
            checkBonus(Input1)  # Check if the input is integer, if true save input as bonus
            print(Bonus)
            Input1 = input("Please enter your Overtime: \n")  # Temporary save input for overtime
            checkOvertime(Input1)  # Check if the input is integer, if true save input as overtime
            print(Overtime)
            TotalSalary = (int(BasicSalary) + int(Allowance) + int(Bonus) + int(Overtime)) * 0.89  # Calculate total
            # salary
            if TotalSalary < 2000:
                TotalSalary = TotalSalary * 1.05  # Add commissions
            elif TotalSalary > 3000:
                TotalSalary = TotalSalary * 0.94  # Add Income Tax
            else:
                pass  # Do nothing
            print("Your total Salary is $", int(TotalSalary), ",with EPF deduction of 11%")
            Show_Emp = [EmployeeName, EmployeeID, Department, BasicSalary, Allowance, Bonus, Overtime, TotalSalary,
                        CurrentMonth]  # Temporary save the employee profile for print
            employee_list.append(Show_Emp)  # Save the employee profile into employee list.
            k = 0
            print("**********Employee Profile**********")  # Print the employee profile; row by row.
            print("Month:", CurrentMonth)
            while 0 <= k <= 7:
                print(k + 1, ".", listHeading[k], ":", Show_Emp[k])
                k = k + 1
            else:
                print("**********End**********")
            rerunAddEmp()  # Allow the user to rerun the function.
        elif employee_list[i][0].lower() != TempName:  # Increment for looping.
            i = i + 1
        else:  # Employee name exists so ask for ID to verify, if false run add employee.
            print("The employee:", employee_list[i][0], " exists in the library.")
            TempID = input("Please enter your employee ID for verification: \n")
            if TempID != employee_list[i][1]:
                print("Employee ID not found. Proceed to <Adding Employee>")
                EmployeeName = input("Please enter your Name: \n")
                EmployeeID = input("Please enter your ID: \n")
                Department = input("Please enter your Department: \n")
                Input1 = input("Please enter your Basic Salary: \n")
                checkBasicSalary(Input1)
                print(BasicSalary)
                Input1 = input("Please enter your Allowance: \n")
                checkAllowance(Input1)
                print(Allowance)
                Input1 = input("Please enter your Bonus: \n")
                checkBonus(Input1)
                print(Bonus)
                Input1 = input("Please enter your Overtime: \n")
                checkOvertime(Input1)
                print(Overtime)
                TotalSalary = (int(BasicSalary) + int(Allowance) + int(Bonus) + int(Overtime)) * 0.89
                if TotalSalary < 2000:
                    TotalSalary = TotalSalary * 1.05  # Add commissions
                elif TotalSalary > 3000:
                    TotalSalary = TotalSalary * 0.94  # Add Income Tax
                else:
                    pass  # Do nothing
                print("Your total Salary is $", int(TotalSalary), ",with EPF deduction of 11%")
                Show_Emp = [EmployeeName, EmployeeID, Department, BasicSalary, Allowance, Bonus, Overtime,
                            TotalSalary]
                employee_list.append(Show_Emp)
                print(Show_Emp)
                rerunAddEmp()  # Allow the user to rerun the function.
            else:
                print("Employee ID is found.")  # Both employee and matching ID found so not need to run the function.
                print("Employee exists with a matching ID, adding new employee profile is not needed.")
                rerunAddEmp()  # Allow the user to rerun the function.
                i = -100


def checkBasicSalary(input_ans1):  # Check if the input is integer, else ask for re-input.
    global User1
    global BasicSalary
    try:
        User1 = int(input_ans1)
        BasicSalary = User1
    except ValueError:
        input_ans1 = input("Invalid input please re-enter\n")
        checkBasicSalary(input_ans1)


def checkAllowance(input_ans1):  # Check if the input is integer, else ask for re-input.
    global User1
    global Allowance
    try:
        User1 = int(input_ans1)
        Allowance = User1
    except ValueError:
        input_ans1 = input("Invalid input please re-enter\n")
        checkAllowance(input_ans1)


def checkBonus(input_ans1):  # Check if the input is integer, else ask for re-input.
    global User1
    global Bonus
    try:
        User1 = int(input_ans1)
        Bonus = User1
    except ValueError:
        input_ans1 = input("Invalid input please re-enter\n")
        checkBonus(input_ans1)


def checkOvertime(input_ans1):  # Check if the input is integer, else ask for re-input.
    global User1
    global Overtime
    try:
        User1 = int(input_ans1)
        Overtime = User1
    except ValueError:
        input_ans1 = input("Invalid input please re-enter\n")
        checkOvertime(input_ans1)


def rerunAddEmp():  # Rerun add employee or return to other menu.
    global Decision
    Decision = input("Do you wish to add another profile? Enter <Yes> to proceed or <No> to return back to the "
                     "<Employee Profile> \n")
    if Decision.lower() in ["yes", "y"]:
        print("Returning to <Add Employee>")
        addEmployee()  # Rerun add employee
    elif Decision.lower() in ["no", "n"]:
        selection = input("Do you wish to end the program? <Yes/No>:\n")
        if selection.lower() in ["yes", "y"]:
            exitProgram()  # End the program.
        elif selection.lower() in ["no", "n"]:
            print("Return to <Employee Profile>")
            empMenu()  # Return to Employee Profile.
    else:
        print("Invalid Input")
        rerunAddEmp()  # rerun this function if invalid input


#  Employee Profile -> Update Employee
def updateEmployee():
    global i
    global j
    global EmpID
    global IndexLocation
    global InputAns1
    global TempName
    i = 0
    TempName = input("Please input your full name:\n")  # Temporary save input.
    TempName = TempName.lower()  # Lowercase input.
    while i <= len(employee_list) and (i >= 0):
        if i >= len(employee_list):
            i = -10  # stop the loop
            print(" Employee not found!\n")
            rerunUpdateEmp()  # Rerun this function or return to others
            i - 100  # Declare again to stop the loop for safety
        elif employee_list[i][0].lower() != TempName:
            i = i + 1
        else:  # If employee name found, check employee ID
            print("Employee found.")
            IndexLocation = employee_list.index(employee_list[i])  # Save index location of the employee in the list.
            IndexLocation = int(IndexLocation)
            print(employee_list[i][0])  # Print the name for checking
            EmpID = input("Please enter your ID for verification:\n")
            if EmpID == employee_list[i][1]:  # Check if the ID match with the employee name.
                print("Employee ID matched.\n", "Please selected the following information to modify.")
                j = 0
                while 0 <= j <= 6:  # Print each employee information line by line.
                    print(j + 1, ".", listHeading[j], ":", employee_list[i][j])
                    j = j + 1
                checkInputChange()  # Allow the user to pick which information to change.
            else:
                print("Incorrect employee ID entered, cancelling current process.")
                rerunUpdateEmp()
                i = -100
                j = -100
    else:
        pass


def checkInputChange():
    global InputAns1
    global EmpID
    InputAns1 = input("Please select the information you want to change by entering the <1-7>:\n")
    checkUpdateEmp(InputAns1)  # Check integer
    InputAns1 = int(TempInput)  # Force integer
    if 0 < InputAns1 <= 7:
        InputAns1 = InputAns1 - 1  # Minus 1 to recall the data correctly
        print("Your selected:", listHeading[InputAns1])
        employee_list[i][InputAns1] = input("Please enter your input:\n")  # Overwrite the data
        print(employee_list[i])  # Print the list to check.
        rerunUpdateEmp()  # Choose to rerun update employee or return to other menus.
        EmpID = -100
        InputAns1 = -100
    else:
        print("Invalid input")
        checkInputChange()  # rerun function


def checkUpdateEmp(input_ans1):  # Check if the user input can be converted to integer
    global User1
    global TempInput
    try:
        User1 = int(input_ans1)
        TempInput = User1
    except ValueError:
        input_ans1 = input("Invalid input please re-enter\n")
        checkUpdateEmp(input_ans1)


def rerunUpdateEmp():  # Rerun update Employee or return to other menus.
    global Decision
    Decision = input("Do you wish to update another profile? Enter <Yes> to proceed or <No> to return back to the "
                     "<Employee Profile> \n")
    if Decision.lower() in ["yes", "y"]:
        print("Returning to <Update Employee>")
        updateEmployee()
    elif Decision.lower() in ["no", "n"]:
        selection = input("Do you wish to end the program? <Yes/No>:\n")
        if selection.lower() in ["yes", "y"]:
            exitProgram()  # End the program.
        elif selection.lower() in ["no", "n"]:
            print("Return to <Employee Profile>")
            empMenu()  # Return to employee profile.
    else:
        print("Invalid Input")
        rerunUpdateEmp()


#  Employee Profile -> Delete Employee
def deleteEmployee():
    global i
    global Decision
    global IndexLocation
    global TempName
    global UserID
    UserID = input("Please enter your ID: (Admin only!)\n")  # Input to check if the user is Admin.
    adminCheck(UserID)  # Check if the user is Admin.
    TempName = input("Please input a name to delete:\n")
    i = 0
    TempName = TempName.lower()  # Look for name from the list.
    while i <= len(employee_list) and (i >= 0):
        if i >= len(employee_list):
            print("Employee not found!\n", "Nothing to delete, return to <Employee Profile>. \n")
            rerunDeleteEmp()  # Name not available but allow user to retry.
            i = -100
        elif employee_list[i][0].lower() != TempName:
            i = i + 1
        else:
            print("Employee found.")
            IndexLocation = employee_list.index(employee_list[i])  # Remember the index location
            IndexLocation = int(IndexLocation)
            removeConfirm()  # To confirm and proceed to delete or deny the deleting process.
            i = -100
    else:
        pass


def adminCheck(UserID1):  # Check if the user is Admin
    if UserID1 in Admin:
        print("Access granted.")
    else:
        print("Access denied, return to <Employee Profile>")
        empMenu()


def removeConfirm():  # To confirm and proceed to delete or deny the deleting process.
    global Decision
    global i
    Decision = input("Do you wish to delete the this employee profile? Please enter <Yes/No> to proceed.\n")
    if Decision.lower() in ["yes", "y"]:
        print("Proceed to remove employee profile.")
        employee_list.pop(IndexLocation)  # Delete the employee profile.
        i = 0
        while 0 <= i < len(employee_list):  # Print the list to show the profile is deleted.
            print(employee_list[i])
            i = i + 1
        else:
            i = -100
            rerunDeleteEmp()
    elif Decision.lower() in ["no", "n"]:  # Deny the deleting process.
        print("Nothing has been deleted")
        rerunDeleteEmp()
    else:
        print("Input error!")  # Reject input error then allow the user to rerun.
        removeConfirm()


def rerunDeleteEmp():  # Rerun delete employee or proceed to other menu
    global Decision
    Decision = input("Do you wish to delete another profile? Enter <Yes> to proceed or <No> to return back to the "
                     "<Employee Profile> \n")
    if Decision.lower() in ["yes", "y"]:
        print("Returning to <Delete Employee>")
        deleteEmployee()
    elif Decision.lower() in ["no", "n"]:
        selection = input("Do you wish to end the program? <Yes/No>:\n")
        if selection.lower() in ["yes", "y"]:
            exitProgram()  # End the program.
        elif selection.lower() in ["no", "n"]:
            print("Return to <Employee Profile>")
            empMenu()  # Return to employee profile.
    else:
        print("Invalid Input")
        rerunDeleteEmp()


#  Salary Generator
def generateSalary():
    global i
    global Salary
    global TempID
    global TempName
    global Count2
    i = 0
    TempName = input("Please input your name for verification:\n")  # User input name for verification.
    TempName = TempName.lower()
    while i <= len(employee_list) and (i >= 0):
        if i >= len(employee_list):
            print("Employee not found.")  # Rerun generate salary if input not found
            i = -1
            rerunGenerateSalary()
        elif employee_list[i][0].lower() != TempName:  # Increment for looping.
            i = i + 1
        else:
            print("The employee:", employee_list[i][0], " exists in the library.")
            TempID = input("Please enter your employee ID for verification: \n")
            if TempID != employee_list[i][1]:
                print("Employee ID not found.")
                rerunGenerateSalary()
                i = -20
            else:
                print("Employee ID is found.")
                index = i
                monthSalary(index)
                rerunGenerateSalary()
                i = -20
    else:
        pass


def calSalary(index):  # Calculate the salary bases on employee profile.
    global Salary
    Salary = int(
        int(employee_list[index][3]) + int(employee_list[index][4]) + int(employee_list[index][5]) +
        int(employee_list[index][6])) * 0.89
    if Salary < 2000:
        Salary = Salary * 1.05  # Add commissions
    elif Salary > 3000:
        Salary = Salary * 0.94  # Add Income Tax
    else:
        pass  # Do nothing
    employee_list[index][7] = Salary
    print("Your total salary is: $", (int(employee_list[index][7])))


def monthSalary(input_ans):  # Select salary bases on the available month
    global Count
    global Count2
    global InputMonth
    global InputMonthTest
    global InputMonthCheck
    InputMonth = input("Please enter the first 3 characters of the month that you wish to generate for your salary: \n")
    InputMonthTest = InputMonth.lower()
    Count = 0
    while 0 <= Count <= 12:  # To check if the input is valid (Jan-Dec).
        if InputMonthTest == listMonth[Count]:
            Count2 = 0
            while 0 <= Count2 <= 12:  # A loop to search for the employee inside the employee_list bases on the month.
                try:
                    if employee_list[input_ans + Count2][8] == InputMonthTest:
                        print("Your salary is printed as below: ")
                        print("Month:", InputMonthTest)
                        input_ans = input_ans + Count2
                        Count = -100  # To end the loop
                        Count2 = -100  # To end the loop
                        calSalary(input_ans)
                    elif Count2 > 11:
                        print("Payslip unavailable, no record for this month:", InputMonthTest)
                        Count = -100
                        Count2 = -100
                    else:
                        Count2 = Count2 + 1
                except IndexError:  # If error print the following msg.
                    print("Payslip unavailable, no record for this month:", InputMonthTest)
                    Count = -100
                    Count2 = -100
            else:
                pass
        elif Count > 11:
            print("Payslip unavailable, no record for this month:", InputMonthTest)
            Count = -100
        elif Count < 0:
            pass
        else:
            Count = Count + 1
    else:
        pass


def rerunGenerateSalary():  # rerun salary generator.
    selection = input("Do you wish to generate other salary? Enter <Yes> to proceed or <No> to return back to the "
                      "<Main Menu> \n")
    if selection.lower() in ["yes", "y"]:
        print("Return to <Salary Generator>")
        generateSalary()  # rerun salary generator.
    elif selection.lower() in ["no", "n"]:
        selection = input("Do you wish to end the program? <Yes/No>:\n")
        if selection.lower() in ["yes", "y"]:
            exitProgram()  # End the program.
        elif selection.lower() in ["no", "n"]:
            print("Return to <Main Menu>")
            returnMain()  # Return to main menu.
    else:
        print("Invalid input")
        rerunGenerateSalary()


#  Pay Slip
def paySlipMenu():  # Print payslip menu with three options for the user to select.
    global User1
    print("\n*********************<Pay Slip>*********************", "\n1. Search Payslip", "\n2. View Payslip",
          "\n0. Return to Main Menu", "\n ")
    User1 = input("Please enter <0, 1, or 2> to proceed:\n")
    checkInput2(User1)  # Check if the input is integer.
    print("Valid input:", User1)
    payCheckNext(User1)  # Check if the input is valid.


def payCheckNext(input_ans):  # Payslip menu, select between Search or view payslip, else return to main menu
    if input_ans == 1:
        print("You selected <Search Payslip>")
        searchPayslip()  # Allow user to generate payslip by searching.
    elif input_ans == 2:
        print("You selected <View Payslip>")
        viewPayslip()   # Allow user to generate payslip bases on the displayed payslip list.
    elif User1 == 0:
        returnMain()
    else:
        pass


#  Pay Slip -> Search Payslip
def searchPayslip():
    global i
    global j
    global InputMonth
    global TempID
    global TempName
    TempName = input("Please input your name for verification:\n")
    TempName = TempName.lower()
    i = 0
    while i <= len(employee_list) and (i >= 0):
        if i >= len(employee_list):
            i = -10  # Redefine i to end the loop.
            print("Employee not found. Unable to generate Payslip")
            rerunSearchPayslip()
            i = -1000  # Redefine again to avoid any possible error.
        elif employee_list[i][0].lower() != TempName:  # Increment for looping.
            i = i + 1
        elif employee_list[i][0].lower() == TempName:  # Check Employee ID.
            print("The employee:", employee_list[i][0], " exists in the library.")
            TempID = input("Please enter your employee ID for verification: \n")
            if TempID != employee_list[i][1]:
                print("Employee ID not found. Unable to generate Payslip")
                i = -10
                rerunSearchPayslip()
                i = - 1000
            else:
                j = i
                i = -10
                print("Employee exists with a matching ID, printing your payslip.")
                selectMonthPayslip(j)  # Allow the user to select which month to print for payslip.
                rerunSearchPayslip()  # Rerun search payslips.
                i = -1000
        else:
            i = i + 1


def selectMonthPayslip(input_ans):
    global Count
    global Count2
    global InputMonth
    global InputMonthTest
    global InputMonthCheck
    InputMonth = input("Please enter the first 3 characters of the month that you wish to generate for your payslip \n")
    InputMonthTest = InputMonth.lower()  # Input month, lowercase to search from month list.
    Count = 0
    while 0 <= Count <= 12:  # To check if the input is valid (jan-dec)
        if InputMonthTest == listMonth[Count]:
            Count2 = 0
            while 0 <= Count2 <= 12:
                try:
                    if employee_list[input_ans + Count2][8] == InputMonthTest:  # Show all the available monthly payslip
                        print("Your Payslip is printed as below: ")
                        k = 0
                        print("**********Payslip**********")
                        print("Month:", InputMonthTest)
                        while 0 <= k <= 7:  # Generate payslip by printing each information line by line.
                            print(k + 1, ".", listHeading[k], ":", employee_list[input_ans][k])
                            k = k + 1
                        else:
                            print("**********End**********")
                        Count = -100
                        Count2 = -100
                    else:
                        print("Payslip unavailable, no record for this month:", InputMonthTest)
                        Count = -100
                        Count2 = -100
                except IndexError:
                    print("Payslip unavailable, no record for this month:", InputMonthTest)
                    Count = -100
                    Count2 = -100
            else:
                pass
        elif Count > 11:  # Allow the user to retry/ re-input for the month.
            print("Invalid input")
            selectMonthPayslip(input_ans)
        else:
            Count = Count + 1
    else:
        pass


def rerunSearchPayslip():  # Rerun Search payslip.
    selection = input("Do you wish to search for other payslip? Enter <Yes> to proceed or <No> to return back to the "
                      "<Payslip Menu> \n")
    if selection.lower() in ["yes", "y"]:
        print("Return to <Search Payslip>")
        searchPayslip()  # Return to search payslip menu.
    elif selection.lower() in ["no", "n"]:
        selection = input("Do you wish to end the program? <Yes/No>:\n")
        if selection.lower() in ["yes", "y"]:
            exitProgram()  # End the program.
        elif selection.lower() in ["no", "n"]:
            print("Return to <Payslip Menu>")
            paySlipMenu()  # Return to payslip menu.
    else:
        print("Invalid input")
        rerunSearchPayslip()

#  Pay Slip -> View Payslip
def viewPayslip():  # Allow the user to generate payslip by viewing all the available monthly payslip.
    global i
    global j
    global InputMonth
    global RetryViewPay
    global TempID
    global TempName
    TempName = input("To generate the your <Salary List>, please input your name for verification:\n")
    TempName = TempName.lower()  # Check for employee name
    i = 0
    while 0 <= i <= len(employee_list):
        if i >= len(employee_list):
            print("Employee not found. Unable to generate <Salary List>")
            rerunViewPayslip()
            i = -1000  # Redefine i to end the loop.
        elif employee_list[i][0].lower() != TempName:  # Increment for looping.
            i = i + 1
        else:  # Employee found, check for ID next.
            print("The employee:", employee_list[i][0], " exists in the library.")
            TempID = input("Please enter your employee ID for verification: \n")
            if TempID != employee_list[i][1]:
                print("Employee ID not found. Unable to generate <Salary List>")
                rerunViewPayslip()
                i = -1000
            else:  # Both name and ID found, proceed to print list.
                j = i
                print("Employee exists with a matching ID, printing your <Salary List>.")
                selectList(TempName)  # Function to print list bases on employee name.
                rerunViewPayslip()
                i = -1000
    else:
        pass


def selectList(Temp_Name1):  # Function to print list bases on employee name.
    global i
    global Count
    global Count2
    global InputMonth
    global InputMonthTest
    global InputMonthCheck
    global TempList
    TempList = []
    i = 0
    Count = 0
    while 0 <= i <= (len(employee_list) - 1):  # Generate all the available payslips with different month.
        if employee_list[i][0].lower() == Temp_Name1:
            print(i + 1, employee_list[i])
            TempList.append(i)
            i = i + 1
        elif i > len(employee_list):
            pass
        else:
            i = i + 1

    try:
        Count2 = 0
        InputMonth = input("Please select your payslip by entering the assigned number: \n")
        InputMonthTest = int(InputMonth) - 1  # Deduce by 1 convert into index for array/list output
        while 0 <= Count2 < len(TempList):
            if InputMonthTest == int(TempList[Count2]):  # Generate payslip by printing information line by line.
                print("Your Payslip is print below: ")
                k = 0
                print("**********Payslip**********")
                print("Month:", employee_list[InputMonthTest][8])
                while 0 <= k <= 7:
                    print(k + 1, ".", listHeading[k], ":", employee_list[InputMonthTest][k])
                    k = k + 1
                else:
                    print("**********End**********")
                    Count2 = -100
            elif InputMonthTest >= len(TempList):
                print("Invalid input")
                Count2 = -100
            else:
                Count2 = Count2 + 1
    except ValueError:
        print("invalid input")
        rerunViewPayslip()


def rerunViewPayslip():  # Rerun View payslip
    selection = input("Do you wish to view and generate other payslips? Enter <Yes> to proceed or <No> to "
                      "return back to the <Payslips Menu> \n")
    if selection.lower() in ["yes", "y"]:
        print("Return to <View Payslip>")
        viewPayslip()  # Return to view payslip
    elif selection.lower() in ["no", "n"]:
        selection = input("Do you wish to end the program? <Yes/No>:\n")
        if selection.lower() in ["yes", "y"]:
            exitProgram()  # End the program.
        elif selection.lower() in ["no", "n"]:
            print("Return to <Payslip Menu>")
            paySlipMenu()  # Return to payslip menu.
    else:
        print("Invalid input")
        rerunViewPayslip()


# ***Main_Coding***
mainMenu()
