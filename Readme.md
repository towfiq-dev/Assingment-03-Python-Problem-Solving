# Employee Salary Management System

A simple command-line Python application built to practice **Python Functions** and **File Handling** concepts. This program allows users to add new employee details and view all stored employee records using a persistent text file (`employees.txt`).

## Features

* **Add Employee:** Accepts Employee Name, Employee ID, and Salary as inputs and saves them in a structured format (`Name | ID | Salary`) inside `employees.txt`.
* **View Employees:** Reads and displays all stored employee records from the text file. Includes error handling if the file does not exist yet.
* **Interactive Menu:** Runs in a continuous loop until the user chooses to exit.

## Concepts Used

* **Functions & Parameters:** Modular code structure using reusable functions (`add_employee`, `view_employees`, and `main`).
* **Return Statements:** Functions return confirmation messages and file data back to the caller.
* **File Handling:** Uses Python's built-in `open()` function with append (`"a"`) and read (`"r"`) file modes.
* **Exception Handling:** Uses `try-except` blocks to gracefully handle `FileNotFoundError`.

## Project Structure

```text
├── yourname_employee_management.py   # Main Python script
├── employees.txt                     # Auto-generated file storing employee records
└── README.md                         # Project documentation
```

## How to Run

1. Make sure you have **Python 3** installed on your system.
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the Python script:
   ```bash
   python yourname_employee_management.py
   ```
   *(Note: Replace `yourname` with your actual filename).*

## Sample Usage

```text
1. Add Employee
2. View Employees
3. Exit
Choose Option: 1
Enter Name: Rahim
Enter ID: E101
Enter Salary: 25000
Employee Added Successfully

1. Add Employee
2. View Employees
3. Exit
Choose Option: 2

--- Employee Records ---
Rahim | E101 | 25000
```