#QUESTION 1
'''Program to find average of three numbers'''

print("\nAVERAGE CALCULATOR\n")

#Taking the input of all three numbers.
Number1 = int(input("Enter the first number :"))
Number2 = int(input("Enter the second number :"))
Number3 = int(input("Enter the third number :"))

#Calculating the average.
avg = (Number1+Number2+Number3)/3

#Print out the average.
print("The average of three numbers entered is : ",avg)

print()
print("-x"*60)


#QUESTION 2
'''Program to compute income tax'''

print("\nINCOME TAX CALCULATION\n")

Tax_Rate = 0.2
Standard_Deduction = 10000
Dependent_Deduction = 3000

#Taking the input for gross income and number of dependents.
Gross_Income = int(input("Enter the Gross Income: "))
Number_of_Dependents = int(input("Enter the number of dependents: "))

#Calculating the gross income.
Taxable_Income = Gross_Income-Standard_Deduction-(Dependent_Deduction*Number_of_Dependents)
Tax = Taxable_Income*Tax_Rate

#Print out income tax.
print("The Tax is : ",Tax)

print()
print("-x"*60)


#Question 3
'''Program to store different data types values into a list'''

print("\nDifferent data type values in one list\n")

Student = []

#Taking inputs of the student details.
Student.insert(0,int(input("Enter the student ID: ")))
Student.insert(1,(input("Enter the student Name: ")))
Student.insert(2,(input("Enter the student Gender: ")))
Student.insert(3,(input("Enter the student Course Name: ")))
Student.insert(4,int(input("Enter the student CGPA: ")))

#Print out the list.
print("The list with different data value types is : ")

print(Student)
print("-x"*60)


#Question 4
'''Program to enter marks of 5 students into a list and display them in a sorted manner'''

print("\nEntering marks of 5 students and sorting them\n")

Marks = []

#Taking inputs of marks of different students.
Marks.insert(0,int(input("Enter the marks of first student: ")))
Marks.insert(1,int(input("Enter the marks of second student:")))
Marks.insert(2,int(input("Enter the marks of third student:")))
Marks.insert(3,int(input("Enter the marks of fourth student:")))
Marks.insert(4,int(input("Enter the marks of fifth student:")))

#Print out the list.
print("The list with marks of 5 students is: ")

print(Marks)

#Sorting the list.
Marks.sort()

#Printing list with sorting.
print(Marks)
print("-x"*60)


#Question 5
'''Program to print a specific list after removing the fourth element and removing Black and Pink from list and replacing them with Purple'''

#List.
color = ["Red","Green","White","Black","Pink","Yellow"]

#Print the list.
print("The list of colors is:  ")

print(color)

#Part one
color.remove("Black")

#Print list after changes done in Part one.
print("List after changes in part one: ")
print(color)


#Part two
color[3]=color[4]="Purple"
color.pop(3)

#Print list after changes done in Part two.
print("Final list: ")

print(color)

print("-x"*60)

