# **Py-Testing**
## **Using Pylint**
Pylint designed to check Python code for errors, enforce a coding standard `(PEP 8)`, and look for code smells and potential bugs. Pylint examines Python source code and generates reports on various aspects of the code, including style, syntax, and potential logical errors.

#### **How to install Pylint**
Run the command: `pip install pylint`

### **Q1(a)**
#### **Procedure**
Step-1: Transfer the kaooa.py from Assignment-1 Folder.<br>
Step-2: Run the command: `pylint kaooa.py > intiallint.txt`. This command redirects output lint results into respective file.<br>
Step-3: Now change the code according to suggestions and store results using above command.

### **Q1(b)**
### **Procedure**
Step-1: Run the command `python3 Lucas_1.py`<br>
Step-2: Enter the value of n as directed by question.<br>
Step-3: Run the command `pylint Lucas_1.py > <filename.txt>` to store pylint results.

## **Using `unittest`**
#### **Installation**
`unittest` module is in-built module in python.

### **Q2**
#### **Procedure**
**Running the Code**<br>
Step-1: Goto 'Code' directory
Step-2: Run the program using `python3 kaprekarroutine.py`.<br>
Step-3: Enter valid 4-digit number according to constraints provided in Question.
Step-4: Output will be displayed on the terminal accordingly.

**Running the Testing File**<br>
Step-1: Goto the 'testcases' directory.<br>
Step-2: Run the testcases using `python3 test.py`.

**Assumptions**<br>
- The testcases file must be run from the directory itself as it uses the relative path for importing the module.
- The input is taken as string for testing leading 0's cases.
- The condition which a particular test is checking, has been mentioned in docstring of each testcase function.

## **Using `pytest`**
#### **Installation**
Run the command: `pip install pytest`

### **Q3**
#### **Procedure**
**Running the Code**<br>
Step-1: Goto 'Code' directory
Step-2: Run the program using `python3 palindrome.py`.<br>
Step-3: Enter a valid year.
Step-4: Output will be displayed on the terminal accordingly.

**Running the Testing File**<br>
Step-1: Goto the 'testcases' directory.<br>
Step-2: Run the testcases using `python3 test.py`.

**Assumptions**<br>
- The testcases file must be run from the directory itself as it uses the relative path for importing the module.
- The input is taken as string.
- The condition which a particular test is checking, has been mentioned in docstring of each testcase function.

### **Q4**
#### **Procedure**
**Running the Code**<br>
Step-1: Goto 'Code' directory
Step-2: Run the program using `python3 palindrome.py`.<br>
Step-3: Enter a valid year.
Step-4: Output will be displayed on the terminal accordingly.

**Running the Testing File**<br>
Step-1: Goto the 'testcases' directory.<br>
Step-2: Run the testcases using `python3 test.py`.

**Assumptions**<br>
- The testcases file must be run from the directory itself as it uses the relative path for importing the module.
- The input is taken as string.
- The condition which a particular test is checking, has been mentioned in docstring of each testcase function.
