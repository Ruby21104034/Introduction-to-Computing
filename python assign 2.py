



#Question1

'''Using various string functions on the given string'''

print("\nAnswer of Question 1 : \n")

#Printing the output of part a.
string="Python is a case sensitive language"
n=len(string)
print("Part a : The length of the string is : ",n)


#Printing the output of part b.
print("Part b : The reverse of the string is : ",string[::-1])


#Printing the output of part c.
new_string=string[10:26]
print("Part c : The new string is : ",new_string)


#Printing the output of part d.
var1=string.replace("case sensitive","object oriented")
print("Part d : The substring after replacement : ",var1)


#Printing the output of part e.
var2=string.index('a')
print("Part e : The index of a occuring for the first time is : ",var2)


#Printing the output of part f.
var3=string.replace(" ","")
print("Part f : The string with no white spaces is : ",var3)

print("-x"*60)



#Question 2

'''Using string formatting to get various outputs'''

print("\nAnswer of Question 2 : \n")

#Storing student details in different variables.
StudentName="Ruby"
StudentID="21104034"
StudentDepartment="Electrical"
StudentCGPA="9.9"

#printing the output.
print("\nHey ,{} Here!\nMy SID is {}.\nI am from {} department and my CGPA is {}".format(StudentName,StudentID,StudentDepartment,StudentCGPA))


print("-x"*60)


#Question 3

'''Using bitwise operators'''

print("\nAnswer of Question 3 : \n")
#Creating variables.
a=56
b=10

#Printing the output of part a by using AND operator
print("Part a : The output of a&b is :")
print(a&b)


#Printing the output of part b by using OR operator
print("Part b : The output of a|b is : ",a|b)



#Printing the output of part c by using XOR operator
print("Part c : The output of a^b is : ",a^b)



#Printing the output of part d1 by using LEFT SHIFT operator
print("Part d : The output of a<<2 and b<<2 is : ",a<<2,b<<2)



#Printing the output of part e1 by using RIGHT SHIFT operator
print("Part e1  : The output of a>>2 is and b>>4 is : ",a>>2,b>>4)



print("-x"*60)



#Question 4

'''Program to find the greatest of three numbers'''

print("\nAnswer of Question 4 : \n")
#Taking the input of three numbers from user
n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
n3=int(input("Enter the third number : "))


#Writing the code to find the largest number and printing the output
if n1>n2 and n1>n3:
    print("The greatest number is : ",n1)
elif n2>n1 and n2>n3:
     print("The greatest number is : ",n2)
else:
    print("The greatest number is : ",n3)

print("-x"*60)


    
#Question 5

'''Program to find if "name" is present in string entered by user'''

print("\nAnswer of Question 5 : \n")

#Taking the input from the user
STRING=input("Enter the string here : ")


#Writing program for the question
if "name" in STRING:
    print(" Yes ")
else :
    print(" No ")

print("-x"*60)


#Question 6

'''Program to find whether a triangle is possible to be made using lenghts given by user'''

print("\nAnswer of Question 6 : \n")

#Taking the inputs for lengths of sides of triangle from user
side1=float(input("Enter the length of the first side of triangle : "))
side2=float(input("Enter the length of the second side of triangle : "))
side3=float(input("Enter the length of the third side of triangle : "))


#Writing the code to check whether it is possible to form a triangle
if side1+side2>=side3 and side2+side3>=side1 and side3+side1>=side2:
    print("Yes,the triangle can be formed")
else :
    print("No ,the triangle cannot be formed")

print("-x"*60)
    
    














