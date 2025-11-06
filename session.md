https://meet.google.com/sxb-orhq-mfu

# 03-11-25
Just I create workspace/folder jbit-ds-2nd-2025 
All the files/sesssion note will keep in this folders.

Assumptions:  You people already know fundamentals of python - basic syntax - done lot of examples

We will try to develop one back end application - using python
IPL, shoppingcart, college etc.,

# Factors to be consider while writnig program
performance
    time
        O(n), O(1), O(long n)
    memory
readability
    naming convention
        variable, method, class
        IPL - players, player, team, teams, match, matches
            - add_player / addPlayer, getAllPlayers, get_players
maintanance
    tools - monitoring tools
enhacement
    without modifing exist code, you should able to implemnt/enance the program/application
    Open -Close principle
        Open for extention
        Close for modification

availability
    redundancy

we snhould not write any print/console.log/SOP in the actual program/method/classes
You can use print statements in test programe -  you unit test cases - disscuss later.

Examples:
add 2 numbers  - we should enance to do sum of 3/4/5 numbers, without modifying the existing code.
isPrime  - we should able to find list of prime numbers bewtween 2 rangs without modifying the existing code.

calling method from another method  isPrime
calling method as parameter from another method  add( add(5,6), add(10,20))

# Develop applicatino like IPL
Functinality 
    Entities/model Player, team, match  (player statics, match statics etc.,)
    do CRUD Operations
        Create  - add new player
        Retrieve - fetch player details
        Update  - update player details
        Delete  - delete the player



#  Doubts/Clarificatinos
isPrime
A number is called prime if it is not divisible by any other number except 1 and the same number
5, 7 , 11, 13, 17  - prime numbers
6 - is divisible by 2 and 3 - it is not prime
12 - is divisible by 2,3,4,6 - so it is not prime


if you want to find n is prime or not.  try to check with it is divisible by 2, 3 ,4 till n-1

def isPrime(n):
    if(n%2==0):
        return false
    if(n%3==0):
        return false
    ......
    if(n % (n-1) ==0 )
        return false
    return true

def isPrime(n)
    if(n<1):
        return false
    for i in range(2,n-1):
        if(n % i ==0)
            return false
    return true

    

list_of_prime

# How to learn a programming language quickly and efficiantly?
Compare programming language with English
How you learned english

English                     programming language
-------                     --------------------
Alphabets                   Alphabaets - A..Z, a..z, 0..9, special symbols(+,-%,*(,{ []}))
Words (very difficult)      key words / reserved words  (easy to understand becase only                          key                         words)
grammer                     syntax - set of rules
ssentances                  statements
paragraphs                  methods/function
essay writing               program


statements
----------
input statements  - reading the values from keyboard, fild, disk etc.,
                    -input()
output statements  - display the value in the console
                    output()


tomorrow will discuss :

conditional statements
control statements
defind methods


# Session - 04-11-2025
Recap - what we discussed in the previous session.
But in today's I will skipp it - because I need to explain basics.

output statement - display the value/message in the console   - discussed
input statement  - read values from the input devices - key board  - discussed
conditional statements  - if condition - discussed - switch/match pending
control statements - pending
method  - discussed  - will discuss more examples while explainging conditional and controle statements

# output satement:
print("Hello")   // static text
print(x,y)      // display the value of particular variable
print(f"{x}, {y}") // display the value of particular variable

# In generall we won't use print/scan/input statements in real time applications.
# we will read values from frontend/html/js
# we will display values in frontend/html/js
# We won't write executable code without function/method
# The code should be in the method, except global variable

# input statements
x = input()  // read value from the keyboard and store in variable x
print(x)
x = input("Enter value")

before explaining conditional stements/control statements, wanted to explain methods.Because the code we supposed to write in the method itself.
1)definition of the method
2)call the method

# syntax to define the method
def method_name(parameters):   // the parameters are optional
    statement1
    statement2

# call the method
    method_name(parameters)

you should not write print statement in the method. You suupose to return the value to called method
def method_name(parameters):
    statement1
    statement2
    .....
    return variable

variable = method_name(parameters)  //whateer the method return, it will store in variable

# conditional statements
In general the all the statements in the method/program will be executed one by one in the same order how you written.
statement1
statement2
stement3
....
statement n

But some time we supposed to execute few statements and skip other statements based on the condition
- using conditional statements
1)if condition
    simple if
    else  if-  elif
    if - else
    nested if

2) switch

find the grade of the student marks based on 3 subjects
if average maraks are >=60  -  first class
if average is between 50 to 60 - 2nd class
if average is between 35 to 50 - 3rd class
lessthan 35 - fail

def grade(sub1, sub2, sub3):
    total = sub1+sub2+sub3
    avg = total//3    #   / -> float number  // -> integer part
    if(avg>=60):
        return "first class"

return   - return/comout from the method
break   - comeout from the loop  -  will discuss

nested if condition
if(condtion1 ):
    statement1  // this will be executed if contion1 is satisfied
    if(condition2):
        statement2 //this will be executed if condition1 and condition 2 satisfied
    statement3 //outside of condition2, so only if condition1 satisfied, this be executed

def largest_number(x,y,z):
    if(x>y):
        if(x>z):
            return x
        return z
    elif
        if(y>z)
            return y
        return z


Next session - switch and loops/controle statements

# 05-11-2025
Recap - what we discussed in the previous session.

swtch - match
- conditional statement - similar to "if" condition
why switch/match?
if more alternatives are there, it is difficultl to read if you write the code using "if" condition.
Examples - convert digit to word
         convert mm to mmm  month - intod word  1 - January, 2 - Febrary
         online shoping card, based the payment mode - wanted to give discount
         mode - COD - no discout
         mode - sbi-debit-card - 10
         mode - sbi-credit-card - 15
syntax:
match expression:
case 1: st1
case 2:st2

case _:stn

online shoping card, based the payment mode - wanted to give discount
def discounted_price(price, mode):
    dicount = 0
    match mode:
        case "sbi_debit_card":  discount=5
        case "sbi_credict_Card": discount=10
    discounted_price = price - price*10%
    retturn discounted_price

# control statements
some time, few statements need to execute repetedly certime number ot times/ based on some condition

for element in range(initial_value, final_value, step/increment/decrement):
    st1
    st2
    st3
while condition:
    st1
    st2
    st3
print 1 to 10
print 10 to 1
print even number between r1, r2

# single table
def table(n):
    for i in range(1,10):
       print(f" {n} * {i} = {n*i}")

# to print tables from 1 to 10
def print_tables_r1_r2(r1,r2):
    for i in range(r1,r2+1):
        table(i)

practice on loops
format printint
*
**
**
***
****
----
*****
****
***
**
*
-----
1
1 2
1 2 3
1 2 3 4

n=5

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
for i in range(n):
   for j in range(n)
        print(i)
1 1 1 1 
2 2 2 2 
3 3 3 3




1 2 3 4
1 2 3
1 2 
1

    
# wanted to executed statement atlest once - using while loop also you can do it
"do you want to continue, press y to continue other character to exit"
- atlest once I wante to execute the statements
while(True):
    print("do you want to continue")
    c = intput()
    if(c!='y'):
        break

Sir I am having some what confusion in (while) sir - will discuss tomorrow.
will discuss few more examples using while loop

        
   




    































