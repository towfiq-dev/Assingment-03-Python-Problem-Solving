# Function to add a new employee record
def add_employee(name, emp_id, salary):
    file = open("employees.txt", "a")
    record = name + " | " + emp_id + " | " + salary + "\n"
    file.write(record)
    file.close()
    return "Employee Added Successfully"


# Function to read and display all employee records
def view_employees():
    try:
        file = open("employees.txt", "r")
        data = file.read()
        file.close()
        
        if data == "":
            return "No employee records found."
        else:
            return data
            
    except FileNotFoundError:
        return "No employee records found. Please add an employee first."


# Main menu function to run the program
def main():
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        
        choice = input("Choose Option: ")
        
        if choice == "1":
            name = input("Enter Name: ")
            emp_id = input("Enter ID: ")
            salary = input("Enter Salary: ")
            
            result = add_employee(name, emp_id, salary)
            print(result)
            
        elif choice == "2":
            print("\n--- Employee Records ---")
            all_records = view_employees()
            print(all_records)
            
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
            
        else:
            print("Invalid Option! Please enter 1, 2, or 3.")


# Start the program
main()