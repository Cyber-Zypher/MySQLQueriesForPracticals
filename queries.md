
# Python and MySQL for queries.


## Python

* Write a python program to read the Text file and display the number of vowels / consonants / Lowercase / Upper case characters.

```python
file_path = input("Enter the path of the text file: ")

try:
    with open(file_path, 'r') as file:
        text = file.read()
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vowel_count = 0
        consonant_count = 0
        lowercase_count = 0
        uppercase_count = 0

        for char in text:
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
            if char.islower():
                lowercase_count += 1
            elif char.isupper():
                uppercase_count += 1

        print(f"Vowels: {vowel_count}")
        print(f"Consonants: {consonant_count}")
        print(f"Lowercase characters: {lowercase_count}")
        print(f"Uppercase characters: {uppercase_count}")
except FileNotFoundError:
    print("File not found.")
```

* Write a python program to create and search Records in Binary file.
```python
import pickle

file_name = 'records.bin'

def write_record():
    name = input("Enter the name: ")
    value = float(input("Enter the value: "))
    record = {'name': name, 'value': value}
    with open(file_name, 'ab') as file:
        pickle.dump(record, file)

def search_record():
    search_name = input("Enter the name to search: ")
    with open(file_name, 'rb') as file:
        try:
            while True:
                record = pickle.load(file)
                if record['name'] == search_name:
                    print(f"Record found for {search_name}: {record['value']}")
                    return
        except EOFError:
            pass
    print(f"No record found for {search_name}")

def main():
    while True:
        print("\n1. Write a record")
        print("2. Search for a record")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            write_record()
        elif choice == '2':
            search_record()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
```
                                              OR

* Write python program to display fibonacci series.
```python
# Get the number of terms from the user
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Initialize the first two terms of the series
a, b = 0, 1
fib_series = []

# Generate the Fibonacci series
for _ in range(n):
    fib_series.append(a)
    a, b = b, a + b

# Display the Fibonacci series
print("Fibonacci Series:", fib_series)
```
* Write python program to perform arithmetic operations (+,-,*,/) based on the user's choice.

```python
# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display menu for operation selection
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get the user's choice for operation
choice = input("Enter choice (1/2/3/4): ")

# Perform the selected operation and display the result
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    else:
        if num2 != 0:
            result = num1 / num2
            operation = '/'
        else:
            result = "Error! Division by zero is not allowed."
            operation = '/'
    print(f"{num1} {operation} {num2} = {result}")
else:
    print("Invalid input")

```

* Write a python program to read lines from a text file "Sample.txt" and copy those lines in to another file which are starting with an alphabet 'a' or 'A'.

```python
# Open the input file for reading
with open('Sample.txt', 'r') as input_file:
    # Open the output file for writing
    with open('FilteredLines.txt', 'w') as output_file:
        # Read each line from the input file
        for line in input_file:
            # Check if the line starts with 'a' or 'A'
            if line.strip() and (line.strip()[0].lower() == 'a' or line.strip()[0].lower() == 'A'):
                # Write the line to the output file
                output_file.write(line)

print("Lines starting with 'a' or 'A' have been copied to FilteredLines.txt.")

```

# MySQL

* Write SQL Queries
```sql
+--------+--------+--------+------+----------+
| ROLLNO | NAME   | GENDER | AGE  | DEPT     |
+--------+--------+--------+------+----------+
|      1 | ARUN   | M      |   24 | COMPUTER |
|      2 | ANKIT  | M      |   21 | HISTORY  |
|      3 | ANU    | F      |   20 | HINDI    |
|      4 | BALA   | M      |   19 | NULL     |
|      5 | CHARAN | M      |   18 | HINDI    |
|      6 | DEEPA  | F      |   19 | HISTORY  |
+--------+--------+--------+------+----------+
```
Queries for creating the database:

```sql
CREATE DATABASE IF NOT EXISTS SCHOOL;
USE SCHOOL
CREATE TABLE STUDENTS(ROLLNO INT PRIMARY KEY, NAME VARCHAR(20), GENDER VARCHAR(3), AGE INT, DEPT VARCHAR(25));
INSERT INTO STUDENTS(ROLLNO, NAME, GENDER, AGE, DEPT)
VALUES
(1, 'ARUN', 'M', 24, 'COMPUTER'),
(2, 'ANKIT', 'M', 21, 'HISTORY'),
(3, 'ANU', 'F', 20, 'HINDI'),
(4, 'BALA', 'M', 19, 'NULL'),
(5, 'CHARAN', 'M', 18, 'HINDI'),
(6, 'DEEPA', 'F', 19, 'HISTORY');
```
Questions
* Write a query to select distinct department from "STUDENT" table.
```sql
SELECT DISTINCT DEPT FROM STUDENTS;
```
* To show all information about students of history department.
```sql
SELECT * FROM STUDENTS WHERE DEPT = 'HISTORY';
```
* Write query to display the name of female students in Hindi department.
```sql
SELECT * FROM STUDENTS WHERE DEPT = 'HINDI' AND GENDER = 'F';
```
* Write a query to display the name of the students whose ages are between 18-20.
```sql
SELECT * FROM STUDENTS WHERE AGE BETWEEN 18 AND 20;
```
## Second Question
```sql
+--------+--------+--------+------+----------+------+
| ROLLNO | NAME   | GENDER | AGE  | DEPT     | FEES |
+--------+--------+--------+------+----------+------+
|      1 | ARUN   | M      |   24 | COMPUTER | NULL |
|      2 | ANKIT  | M      |   21 | HISTORY  | NULL |
|      3 | ANU    | F      |   20 | HINDI    | NULL |
|      4 | BALA   | M      |   19 | NULL     | NULL |
|      5 | CHARAN | M      |   18 | HINDI    | NULL |
|      6 | DEEPA  | F      |   19 | HISTORY  | NULL |
+--------+--------+--------+------+----------+------+
```
(i) Write a query to delete details of roll number is 5.
```sql
DELETE FROM STUDENTS WHERE ROLLNO = 5;
```
(ii) Write a query to change the fees of students to 170 whose ROLLNO is 1, if existing fees is less than 130.
```sql
UPDATE STUDENTS
SET FEES = '300'
WHERE ROLLNO = 1
AND FEES < 130;
```
(iii) Write a query to add a new column area of type varchar in table "STUDENTS".
```sql
ALTER TABLE STUDENTS
ADD COLUMN area VARCHAR(255);
```
(iv) Write a query to display name of all students whose area contains NULL
```sql
SELECT NAME
FROM STUDENTS
WHERE area IS NULL;
```
## Third Question
To Create database:
```sql
CREATE DATABASE COMPANY;
USE COMPANY;
CREATE TABLE EMPLOYEE(SNO INT PRIMARY KEY, NAME VARCHAR(255), SALARY VARCHAR(25), ZONE VARCHAR(20), AGE INT, GRADE VARCHAR(15), DEPT INT);
INSERT INTO EMPLOYEE(SNO, NAME, SALARY, ZONE, AGE, GRADE, DEPT)
VALUES
(1, 'MUKUL', '30000', 'WEST', 28, 'A', 10),
(2, 'KRITIKA', '35000', 'CENTRE', 30, 'A', 10),
(3, 'NAVEEN', '32000', 'WEST', 40, 'NULL', 20),
(4, 'UDAY', '38000', 'NORTH', 38, 'C', 30),
(5, 'NUPUR', '32000', 'EAST', 26, 'NULL', 20),
(6, 'MOKESH', '37000', 'SOUTH', 28, 'B', 10),
(7, 'SHELLY', '36000', 'NORTH', 26, 'A', 30);
```
The database 'EMPLOYEE' will be like:
```sql
+-----+---------+--------+--------+------+-------+------+
| SNO | NAME    | SALARY | ZONE   | AGE  | GRADE | DEPT |
+-----+---------+--------+--------+------+-------+------+
|   1 | MUKUL   | 30000  | WEST   |   28 | A     |   10 |
|   2 | KRITIKA | 35000  | CENTRE |   30 | A     |   10 |
|   3 | NAVEEN  | 32000  | WEST   |   40 | NULL  |   20 |
|   4 | UDAY    | 38000  | NORTH  |   38 | C     |   30 |
|   5 | NUPUR   | 32000  | EAST   |   26 | NULL  |   20 |
|   6 | MOKESH  | 37000  | SOUTH  |   28 | B     |   10 |
|   7 | SHELLY  | 36000  | NORTH  |   26 | A     |   30 |
+-----+---------+--------+--------+------+-------+------+
```
Creating the next database (DEPARTMENT)
```sql
CREATE TABLE DEPARTMENT(DEPT INT, DNAME VARCHAR(10), MIN_SAL VARCHAR(20), MAX_SAL VARCHAR(20),
HOD INT);
INSERT INTO DEPARTMENT(DEPT, DNAME, MIN_SAL, MAX_SAL, HOD)
VALUES
(10, 'SALES', '25000', '32000', 1),
(20, 'FINANCE', '30000', '50000', 5),
(30, 'ADMIN', '25000', '40000', 7);
```
The database 'DEPARTMENT' will be like:
```sql
+------+---------+---------+---------+------+
| DEPT | DNAME   | MIN_SAL | MAX_SAL | HOD  |
+------+---------+---------+---------+------+
|   10 | SALES   | 25000   | 32000   |    1 |
|   20 | FINANCE | 30000   | 50000   |    5 |
|   30 | ADMIN   | 25000   | 40000   |    7 |
+------+---------+---------+---------+------+
```
(i) Display the name department of all employees from the EMPLOYEE and DEPARTMENT table.
```sql
SELECT e.NAME AS EMPLOYEE_NAME, d.DNAME AS DEPARTMENT_NAME
FROM EMPLOYEE e
JOIN DEPARTMENT d ON e.DEPT = d.DEPT;
```
(ii) Display the number of employees from each ZONE
```sql
SELECT ZONE, COUNT(*) AS EMPLOYEE_COUNT
FROM EMPLOYEE
GROUP BY ZONE;
```
(iii) Display the name, salary, and age of all the employees whose name start with 'M'.
```sql
SELECT NAME, SALARY, AGE
FROM EMPLOYEE
WHERE NAME LIKE 'M%';
```
(iv) Display the maximum salary and minimum salary from EMPLOYEE.
```sql
SELECT MAX(SALARY) AS MAXIMUM_SALARY, MIN(SALARY) AS MINIMUM_SALARY
FROM EMPLOYEE;
```
## Fourth Question
You can use the same database like before,
(i) Display the name of all the employees working in north zone.
```sql
SELECT NAME
FROM EMPLOYEE
WHERE ZONE = 'NORTH';
```
(ii) Display the details of all employees in the ascending order of their salaries.
```sql
SELECT *
FROM EMPLOYEE
ORDER BY SALARY ASC;
```
(iii) Display the name, salary and age of all employees whose name contain 'A'.
```sql
SELECT NAME, SALARY, AGE
FROM EMPLOYEE
WHERE NAME LIKE '%A%';
```
(iv) Display the unique zones from the table employee.
```sql
SELECT DISTINCT ZONE
FROM EMPLOYEE;
```

## Author

- [Sidharth Prabhu](https://www.github.com/Cyber-Zypher)

