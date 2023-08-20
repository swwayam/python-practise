# # To print the appropriate message, if the 
# # number is positive.

# num = input("Please enter a number : ")
# if num > 0:
#     print("The number is positive")
# else: 
#     print("The number is negative")
    
# # Write a program to give a discount of 10% if 
# # the total bill amount exceeds Rs.1000.

# amount = int(input("Please enter the bill : "))
# if amount > 1000:
#     discount = 10 * amount / (100)
#     print("Congrats you got an discount of 10%")
#     print(f"Your total bill is : {amount - discount}")
# else:
#     print("Thank you see you again")

# # Write a program to check if a given number is 
# # a multiple of 5

# number = int(input("Please enter a number : "))
# if number % 5 == 0:
#     print("The number is divisible by 5")
# else: 
#     print("Number is not divisible by 5")

# # Write a program to check if a given year is 
# # leap year or not

# year = int(input("Enter the year : "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a leap year")


######### Loops

# # To print the Fibonacci series using while loop

# previous = 0
# current = 1
# i = 0

# while(i < 10):
#     print(previous)
#     amount = previous + current
#     previous = current
#     current = amount
#     i+=1

# # Write a program to print the number of digits 
# # of a given number using while loop

# number = int(input("Please enter a number : "))
# count = 0

# while(number != 0):
#     number = number // 10
#     count +=1

# print(count)
