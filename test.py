print("Welcome to the test script!")
print("This script is used to demonstrate a simple Python program.")
print(f"Current Python version: {'.'.join(map(str, __import__('sys').version_info[:3]))}")
#x=int(input("Enter first number: "))
#x=int(x)
#y=int(input("Enter second number: "))
#y=int(y)
x=10
y=20
print(f"The sum of {x} and {y} is {x + y}.")    
name = "Test User"
print(name)
print(f"Hello, {name}!")

print(f"You entered: {x} and {y}")
if x==y:
    print("The inputs are equal.")
else:   
    print("The inputs are not equal.")

if(x>y):
    print(f"{x} is greater than {y}.")  
elif(x<y):
    print(f"{x} is less than {y}.") 
else:
    print(f"{x} is equal to {y}.") 

for i in range(5):
    print(f"Iteration {i+1}")   

for char in name:
    print(char)

for i in range(1, 10):  
    print(i,end=' ')
print()

for i in range(10, 1,-2):
    print(i,end=' ')    

marks = [85, 90, 78, 92, 88]
print("total subjects:", len(marks))
total = 0
for mark in marks:
    total += mark
print(f"Total marks: {total}")
average = total / len(marks)
print(f"Average marks: {average}")

def greeting():
    print("Hello! Welcome to the function demonstration.")  
greeting()

print("print 1 to 10 using while loop")
i=1
while i<=10:
    print(i,end=' ')
    i+=1
print()

x=12345
total = 0
while x>0: 
    digit = x % 10
    total += digit
    x = x // 10
print(f"Sum of digits: {total}")

fact=1
i=1
def factorial(n):
    global fact,i
    while i<=n:
        fact = fact * i
        i += 1
    return fact
fact = factorial(5)
print(f"Factorial: {fact}")

def table(n):
    print(f"Multiplication table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
table(10)

def print_tables_1_10(x,y):
    for i in range(x,y):
        table(i)
    print()

print_tables_1_10(1,11) 



def formatted_pattern(n):
    for i in range(n,0,-1):
        print("* " * i)

formatted_pattern(4)

#1
#1 2
#1 2 3
#1 2 3 4 
def number_pattern(n):
  
    for i in range(1,n+1):
        for j in range(n-i+1,1,-1):
            print(" ",end=' ')
        for j in range(1,i+1):
            print(j,end=' ')
        print()
    
number_pattern(10)

def digit_to_word(digit):
    match digit:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5:
            return "Five"
        case 6:
            return "Six"
        case 7:
            return "Seven"
        case 8:
            return "Eight"
        case 9:
            return "Nine"
        case 10:
            return "Ten"
        case 11:
            return "Eleven"
        case 12:
            return "Twelve" 
        case 13:
            return "Thirteen"
        case 14:
            return "Fourteen"
        case 15:
            return "Fifteen"
        case 16:
            return "Sixteen"
        case 17:
            return "Seventeen"
        case 18:
            return "Eighteen"
        case 19:
            return "Nineteen"   
        case 20:
            return "Twenty"
        case _:
            return ""

print(digit_to_word(5))
print(digit_to_word(9)) 

def get_discounted_price(price, mode):
    discount = 0
    match mode:
        case "sbi_card" , "sbi_net_banking" :
            discount = 10
        case "hdfc_card":
            discount = 5
        case "icici_card":
            discount = 20
        case _:
            discount = 0 
    discounted_price = price - (price * discount / 100)
    return discounted_price 
 
print(get_discounted_price(1000, "sbi_card") )
print(get_discounted_price(1000, "sbi_net_banking") )

def digits_to_words(number):
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) 
    units = number % 10

    words = []
    if thousands > 0:
        words.append(digit_to_word(thousands) + " Thousand")
    if hundreds > 0:
        words.append(digit_to_word(hundreds) + " Hundred")  
    if tens > 0:
        words.append(digit_to_word(tens) + " Ten")
    if units > 0:
        words.append(digit_to_word(units))
    return ' '.join(words)  
print(digits_to_words(2345))
print(digits_to_words(1050))
print(digits_to_words(1248 ))


names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    if name.startswith("C"):
        continue
    print(name)

print("first value:",names[0])
print("last value:",names[-1])
marks = [95, 67, 45, 88, 76]
sum = 0
for mark in marks:
    sum = sum + mark
print(f"Total marks: {sum}")
print(marks)
marks.append(100)
print(marks)
marks.remove(45)
print(marks)
marks.sort(reverse=True)
print(marks)
tempmarks = marks.copy()
print("temp :",tempmarks)
marks.append(55)
print("marks :",marks)
print("tempmarks :",tempmarks)
temp1=marks
print("temp1 :",temp1)
marks.append(77)
print("marks :",marks)
print("temp1 :",temp1)
temp1.append(88)
print("marks :",marks)
print("temp1 :",temp1)
temp1.count(88) 
print("Number of times 88 is present:",temp1.count(88))
temp1.count(101) 
print("Number of times 100 is present:",temp1.count(101))

print("Index of 88 is :",temp1.index(88))
temp1.insert(2,111)
print("marks :",marks)
print("temp1 :",temp1)
element = temp1.pop()
print("Popped element :",element)
print("marks after pop :",marks)
print("temp1 after pop :",temp1)
temp1.remove(111)
print("marks after remove 111:",marks)
temp1.extend([121,131,141])
print("marks after extend :",marks)
temp1.clear()
print("marks after clear :",marks)
print("temp1 after clear :",temp1)
tuple_marks = (85, 90, 78, 92, 88)
print("Tuple marks:", tuple_marks)  
tuple_marks_sorted = sorted(tuple_marks)
print("Sorted tuple marks:", tuple_marks_sorted)
tuple_length = len(tuple_marks)
print("Length of tuple marks:", tuple_length)
tuple_marks.count(90)
print("Number of times 90 is present in tuple:", tuple_marks.count(90))
print("Index of 88 in tuple:", tuple_marks.index(88))
set_marks = {85, 90, 78, 92, 88}
print("Set marks:", set_marks)
set_marks.add(95)
print("Set marks after adding 95:", set_marks)
set_marks.remove(78)
print("Set marks after removing 78:", set_marks)    
set_marks.discard(100)
print("Set marks after discarding 100 (not present):", set_marks)
set_marks.update([100, 105, 110,85])
print("Set marks after updating with [100, 105, 110,85]:", set_marks)
set_marks.difference_update({85,90})
print("Set marks after difference update with {85,90}:", set_marks)
print("Difference with {200,300} (not present):", set_marks.difference({100,105}) )
set_marks.discard(200)
print("Set marks after discarding 200 (not present):", set_marks)
set_marks.intersection_update({92,88,110})
print("Set marks after intersection update with {92,88,110}:", set_marks)
set_marks.intersection({88,110,120})
print("Intersection with {88,110,120}:", set_marks.intersection({88,110,120}) )








