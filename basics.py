print("hello")
x=100
y=200
print(x)
print(y)
# In generall we won't use print/scan/input statements in real time applications.
# we will read values from frontend/html/js
# we will display values in frontend/html/js

#x=input("Enter value: ")
#print(x)
#name = input("Enter your name: ")
#print(f"Hello, {name}")

# define a method
def display_hello():
    print("Welcome to data science - jbit")


# call the method
display_hello()

# define a method with parameters
def display_message(name):
    print(f"Welcome: {name}")

# call the method with argument
display_message("Harshini")

# define a method with multiple parameters
def add_numbers(a, b):
     return a+b
   
    # you shouldnot write print statements in real time applications
# call the method with arguments
sum = add_numbers(10, 20)
print(f"Sum is: {sum}")

print(add_numbers(100, 200))

def multiply(x,y):
    return x * y

result = multiply(5,6)
print(f"result is: {result}")

# simplel if example - want to find whether given number is even or odd
def even_or_not(num):
    if num % 2 == 0:     # reminder operator
       return True
    else:
        return False
    
res = even_or_not(24)
print(f"Is given number even? {res}")

def grade(sub1, sub2, sub3):
    total = sub1+sub2+sub3
    avg = total//3    #   / -> float number  // -> integer part
    if(sub1<35 or sub2<35 or sub3<35):
        return "fail"
    if(avg>=60):
        return "first class"
    elif(avg>=50 and avg<60):
        return "2nd class"
    elif(avg>=35 and avg<50):
        return "3rd class"
    else:
        return "fail"   
# print(grade(45,55,65))   directly call in the print statement
result = grade(90,90,30)
print(f"Grade is: {result}")

# nested if example -
# compare 3 numbers and find the largest number
def largest_number(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c
res = largest_number(10,10,10)
print(f"Largest number is: {res}")

# convert digit to word
def digit_to_word(digit):
    match digit:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case _:
            return "invalid digit"
res = digit_to_word(5)
print(f"Digit in word: {res}")

# find the discounted price based on the original price and mode of payment
def discounted_price(price, mode):
    discount = 0
    match mode:
        case "cash":
            discount = 0.1 * price
        case "card":
            discount = 0.05 * price
        case "upi":
            discount = 0.08 * price
        case _:
            discount = 0
    final_price = price - discount
    return final_price
res = discounted_price(1000, "card")
print(f"Final price after discount: {res}")
res = discounted_price(1000, "cash")
print(f"Final price after discount: {res}")
res = discounted_price(1000, "code")
print(f"Final price after discount: {res}")



      