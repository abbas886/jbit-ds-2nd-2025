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


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Combined tuple:", combined_tuple)

combined_tuple = tuple1.__add__(tuple2)
print("Combined tuple using __add__:", combined_tuple)
tuple_repeated = tuple1 * 3
print("Tuple repeated 3 times:", tuple_repeated)
print("3rd value",tuple1.index(2))
print("count of 2 :",tuple1.count(2))
print("length of tuple1 :",len(tuple1))
print("max of tuple1 :",max(tuple1))
print("min of tuple1 :",min(tuple1))

football_players = {"Player1", "Player2", "Player3","Player3"}
basketball_players = {"PlayerA", "PlayerB", "PlayerC","Player1"}
all_players = football_players.union(basketball_players)
print("Football players:", football_players)
print("Basketball players:", basketball_players)
print("All players:", all_players)
common_players = football_players.intersection(basketball_players)
print("Common players:", common_players)
difference_players = football_players.difference(basketball_players)
print("Players in football but not in basketball:", difference_players)
symmetric_diff_players = football_players.symmetric_difference(basketball_players)
print("Players in either football or basketball but not both:", symmetric_diff_players)
football_players.add("Player4")
print("Football players after adding Player4:", football_players)
football_players.remove("PlayerN") if "PlayerN" in football_players else None

print("Football players after removing Player2:", football_players)
football_players.discard("Player5")
print("Football players after discarding Player5 (not present):", football_players)
football_players.update({"Player5", "Player6"})
print("Football players after updating with Player5 and Player6:", football_players)
football_players.clear()
print("Football players after clearing:", football_players)
print("Basketball players remain unchanged:", basketball_players)
print("All players:", all_players)

tupple1 = (10, 20, 30, 40, 50)
print("Original tuple:", tupple1)
sliced_tuple = tupple1[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)
reversed_tuple = tupple1[::-1]
print("Reversed tuple:", reversed_tuple)
tupple2 = (60, 70)
new_tuple = tupple1 + tupple2
print("New tuple after concatenation:", new_tuple)
print("Original tuple remains unchanged:", tupple1)
tupple1.count(20)
print("Count of 20 in tupple1:", tupple1.count(20))
print("Index of 30 in tupple1:", tupple1.index(30))
week_days=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
week_ends=("Saturday", "Sunday")
print("Week days:", week_days)
print("Week ends:", week_ends)
for day in week_days:
    print(day)
#week_days[0] = "Mon"  # This will raise an error since tuples are immutable
week_ends += ("Funday",)
print("Updated week ends:", week_ends)
# week_ends.remove("Funday")  # This will raise an error since tuples are immutable
print("After removing Funday from week ends:", week_ends)
print("before reversing tupple1:", tupple1 )
reversed = list(tupple1).__reversed__()
print("Reversed tupple1 using __reversed__:", reversed)
for item in reversed:
    print(item, end=' ')

employee = {
    "name": "John Doe",
    "age": 30,
    "department": "Sales",
    "is_manager": False 
}
print("Employee Dictionary:", employee)
print("Employee Name:", employee["name"])
employee["age"] = 31
print("Updated Employee Age:", employee["age"])
employee["salary"] = 50000
print("Added Employee Salary:", employee["salary"])
del employee["is_manager"]
print("Employee Dictionary after deleting is_manager:", employee)
print("Employee Keys:", employee.keys())
print("Employee Values:", employee.values())
print("Employee Items:", employee.items())
print("Iterating through Employee Dictionary:")
for key, value in employee.items():
    print(f"{key}: {value}")    
employee_copy = employee.copy()
print("Copied Employee Dictionary:", employee_copy)
employee.get("department")
print("Employee Department using get():", employee.get("department"))   
print("employee department using key :",employee["department"])
print(employee.get("location", "Not Specified"))
emp1 = employee.fromkeys(['name', 'department'])
print("Employee Dictionary after fromkeys():", emp1)
employee.pop("salary")
print("Employee Dictionary after popping salary:", employee)
employee.popitem()
print("Employee Dictionary after popping an item:", employee)
employee.update({"age": 32, "location": "New York"})
print("Employee Dictionary after update():", employee)
employee.setdefault("is_manager", True)
print("Employee Dictionary after setdefault():", employee)
empl1={'name':'Alice','age':28
       ,'department':'HR' 
       ,'is_manager':True 
       }
empl2={'name':'Bob','age':35
       ,'department':'IT'
         ,'is_manager':False 
         }
emp3={'name':'Charlie','age':30
       ,'department':'Finance'
            ,'is_manager':True 
            }
employees = [empl1, empl2, emp3]
for emp in employees:
    print(emp)
emp4={'name':'David','age':40
       ,'department':'Marketing'    
            ,'is_manager':False 
            }
employees.append(emp4)
print("Employees after adding emp4:")
for emp in employees:
    print(emp)
employees.remove(empl2)
print("Employees after removing empl2:")
for emp in employees:
    print(emp)



   










