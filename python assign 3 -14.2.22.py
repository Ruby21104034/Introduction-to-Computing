#Question 1

'''Program to count occurences of character in string'''

print("The solution of Question 1 is: ")

#Taking input string from user
str=input("Enter the word here whose letter frequency is to be counted: ")

#Writing code to count the characters and printing output
for alphabet in str:
    print(alphabet,'=',str.count(alphabet))

print("-x"*60)


#QUESTION 2 IS DONE AT END

 



#Question 3

'''Program to creat list of tuples'''

print("The solution of Ques 3 is :")

#Creating empty list
list=[]

#Taking input from user
number=int(input("Enter the length of list: "))
print("Enter the numbers: ")

#Code for adding elements in list
for i in range(number):
    data=int(input())
    list.append(data)

#Printing list
print(list)
    
#Creating required tuple
res=[(val,pow(val,2)) for val in list]

#Printing final output
print("The required list of tuples is : ",res)

print("-x"*60)



#Question 4

'''Program to print performance and grade'''

print("The solution of Ques 4 is :")

#Taking marks input from user
grade_point=int(input("Enter your grade here: "))

#Using if else statements

if grade_point==10:
    print("Your grade is A+ and Outstanding performance")
elif grade_point>=9:
    print("Your grade is A and Excellent performance")
elif grade_point>=8:
    print("Your grade is B+ and Very Good performance")
elif grade_point>=7:
    print("Your grade is B and Good performance")          
elif grade_point>=6:
    print("Your grade is C+ and Average performance")
elif grade_point>=5:
    print("Your grade is C and Below Average performance")
elif grade_point>=4:
    print("Your grade is D and Poor performance")
else:
    print("Invalid Input!")

print("-x"*60)



#Question 5

'''Program to print a pattern'''

print("The solution of Ques 5 is :")

string=("ABCDEFGHIJK")
length=len(string)


for i in range(1,7):
    for k in range(0,i-1):
        print(" ",end=" ")
    for j in range(0,13-(2*i)):
        ch1=chr(65+j)
        print(ch1,end=" ")
    print("\n",end="") 

print("-x"*60)



#Question 6

'''Program to perform operations on dictionary'''

print("The solution of Ques 6 is :")

n=int(input("Enter a number: "))

d=dict()
for x in range(1,n+1):
    N=int(input("Enter the SID: "))#keys
    Y=input("Enter the student name: ")#values
    d[N]=Y
    
print("The student detail stored in dictionary : ")    
print(d) # Printing the dictionary

print("Sorting the dictionary using student name")
print(dict(sorted(d.items(), key=lambda item: item[1])))  # sorting using values = names

print("Sorting the dictionary using SID")

d1=sorted(d)
sorted_d={key:d[key] for key in d1}
print(sorted_d)

print("Searching student detailwith SID")
key=int(input("Enter the SID to get student name:"))

if key in d.keys():
    print("SID",key)
    print("student name")
    print(d[key])
else:
    print("Not present")
    
print("-x"*60)

#Question 7

'''Program to print Fibonaci sequence'''

print("The solution of Ques 7 is :")

number=int(input("Enter the number upto which fibonacci sequence is needed: "))

a=0
b=1
c=0

for i in range(number):
    print(c)
    a=b
    b=c
    c=a+b
    
print("-x"*60)



#Question 8

'''Program to perform operations on sets'''

print("The solution of Ques 8 is :")

Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#Writing some new sets as
Set4={1,2,3,4,5,6,8}#set1 or set2
Set5={2,4}#set1 and set2

#Part A
Set6=Set4.difference(Set5)
print(Set6)

#Part B






print("-x"*60)

#Question 2

'''Program to print next date of input date'''

print("The solution of Question 2 is: ")

#Taking input for year
year=int(input("Enter a year: "))

#condition 1
if(year%400==0):
    leap_year=True
elif(year%100==0):
    leap_year=False
elif(year%4==0):
    leap_year=True
elif(year<=1800 and year>=2025):
    print("Invalid Input!")
else:
    leap_year=False

#Taking input for month    
month=int(input("Enter a month: "))
       
#condition 2
if month in (1,3,5,7,8,10,12):
       month_length=31
elif month==2:
    if leap_year:
        month_length=29
    else:
        month_length=28
else:
    month_length=30
    
#Taking input for date
date=int(input("Enter a date: "))

#condition 3
if date<month_length:
    day=+1
else:
    date=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1
        
print("The next date is %d-d%-d%."%(day,month,year))            
    
print("-x"*60)   





































