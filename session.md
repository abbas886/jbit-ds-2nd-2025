https://meet.google.com/sxb-orhq-mfu

https://github.com/abbas886/jbit-ds-2nd-2025

https://us06web.zoom.us/j/87861658796


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
    naming convention - coding standards
        variable, method, class
        IPL - players, player, team, teams, match, matches
            - add_player / addPlayer, getAllPlayers, get_players
maintanance
    tools - monitoring tools
enhacement
    Open -Close principle
        Open for extention
        Close for modification
reusability

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
input statements  - reading the values from keyboard, file, disk etc.,
                    -input()
output statements  - display the value in the console
                    output() = print()


tomorrow will discuss :

conditional statements
control statements
define methods


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
print(f" x= {x}, y= {y}") // display the value of particular variable

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

2) switch - match

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

switch - match
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
    for i in range(1,11):
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
break -> will come out from loop
return -> will come out from the method

Sir I am having some what confusion in (while) sir - will discuss tomorrow.
will discuss few more examples using while loop


Session : 06-11-2025
-------------------
Recap - what we discussed yesterday.

while (condition):
    statements

want to print hellow 10 times

i=1
while(i<=10>):  11<=10 
    print("hello")
    i = i + 1    //i +=1   no i++  python

stn
        
   

match(5)
match("abcd")

match(mont_number):
case 1 :  return "January"


# Collections
group of elements
why need collections?
why can't use variables only instead of collections?
sum = s1+s2+s3+s4+S5+s6+S7+s8
60/90 students , it is difficulat to delcare and mage 60/90 variables
How many types of collections are there?  Why somany collections in python
list = []
set
tupple
dictionary

certain properties/factors
ordered or not       10,20,60,40,1000
mutability  - once you added element in the collection - can you modify?
how can you access?   student[0] - based on index / key

performance

# list
declarion/sytanx
variable_name = []
variable_name=[10,50,30,60,70,80]
print(variable_name) / display all the elements - in the same order which you added
variable_name[0]   // 10
variable_name[1]   //50
variable_name[-1]  //last element ie., 80

sum=0
for element in variable_name:
    sum = sum + element
    #print (element)
    return sum
#  go through https://docs.python.org/3/tutorial/datastructures.html

07/11/2025
----------
Recap - what we discussed yesterday
    collections - group of related elements
    very important while doing actual project - IPL, shopping cart, banking, college,library
    discussed about "list" 
    list - python -you can elements of different data types - int, string, object, float
    list - c,c++,java - you can store only values of particular datatypes
    discussed about list api/methods
what we are goig to discuss today
    list, set, tupple, dictionary - important while doing the project

# Environment setup
download the python and install
Environment variables - path to folder where you insrtalled
download IDE - Integrated Development Environment
visual studio code - IDE 
add related extentions in visual studio code

complete the 1st assignment which given.  Once you complete, share the assignment to respected faculty.
will review and provide meaningfull comments.

# set
----
list -> group of elements - can have duplicate values  - list1=[] - ordered
    ordered means - in which order you entered, the values preserved in the same sequence
set -> group of elements - no duplicates   - mathamtical set operations - union, intersection, difference
    not ordered
set1 = ()

collections - want to conduct sports day - participate in different sports
football = {cse-101,cs3-102,cs-105,cse-101}
valleyball ={cse-106,cse-107,cse-101}
wanted get all the students number who participated in both football and valleyball
wwanted toget all the students who participated only football, but not in valleyball


# tupple
-----
ordered
allow duplicate
immutable - you can't modify existing element
banking - different types of accounts - saving_account, checkcing_account,deposit_account
collecget - different  branches - cse,cse-it, it, cse-ds,cse-ai-ds

# install npm first - https://nodejs.org/en/download   - windows installer
# npm install -g json-server
# json-server --watch db.json

# 10-11-2025

Recap
what we discussed in the last week
    control strctures
        conditional statements - if and match
        looping statements - for and while
    collections
        list, tupple, set
what we discussed in the previous session
    tupple

what we are going to discuss today  :  dictionary
this week :  assignment based on collections
             project work  - beckend app using collections,  json-ser for mock datay, http methods and status codes

# dictionary
list, set, tupple - we can store elements - but you don't know what are the elements
l1 = [10,2030,60,30]  what are these values?  is marks?  is score? student id? emplees ids?

dictionary - set of fields/properties  - key and value
emp = {
    "emp_id" : "emp_111",
    "emp_name" : "Rakesh",
    "emp_salary" : 40000,
    ----
    ---
}
How can we access particular field value?
emp["emp_id"]  -  will give emp_111
emp.get("empe_id")  - both sare same
emp.add(  key, values    )
emp.add("dept_no", "dept_101")


how can we add "n" number of employess/students
use 2 collections together ie., dictionary(single stdent/object), list- to have group of students

employees=[]
emp1={

}
emp2={}
emp3 = {}
employees.add(emp1)
employees.add(emp2)

sorted(data, key=lambda x: x['age'])
sorted(data, key=itemgetter('age'))
sorted(emp_list, key= lambda x : x["salary"],reverse=True)


11/11/25
--------
Recap
what we discussed yesterday:
dictionary - key value pairs
Advantages of dictionary over other collections : Other collections we can store group of elements(can any data type) - we can't find what the data belongs to?
list =[] - we don't know whether the data is relatedt marks, emp salary or dept ids or player score
Where as in dictionary we an specify key i.e., the name of property/field/column

dict = {
    "key":"value"
}
student = {
    "student_id" : "csc_001",
    "student_name" : "Kavya",
    "branch":"cse_ds"

}
group of dictionary - list of students
student1= {}
student2 = {}
students=[]
students.append(student1)
students.append(student2)

previous week discussed about list, tupple, set
what we are going to discuss today  :  proper crud operations for one entity/domain student/employe/player
laster will combine/use some association
student ->  branch
employee ->  department
player -> Team

This example - employee_service -
initialize()
get_all_employees()
get_all_employees(depat_id)
get_sorted_employes(salary)
get_top_n_employees()
get_top_n_employees(deptid)
add_employee(dept)
get_employee(emp_id)
update()
delete()

update_employee  - debug in tomorrws sessions.

# list of project domains in computer science to develop backend crud operations using python - search in google and select domain


#  12-11-25
------------
Today I am going to discuss how to start our actual project - IPL (player, team, match etc.,)
You people supposed to choose your own domain
seasrch list of domains
seasrch list of entities  (employee, department, account, address)

Once you CRUD operations(methods) it be accessable via net - other team members will access from other server - BE will be in one server,  FE will in another server,  there may another layers in different servers

Once I deploye my code,  It should be access via some end point - http end points
what are the http methods:
http get   - to fetch the details
http post  - to create new record
http delete - to delete the existing record
http put   - to update the existing record

These http methods return message + status codes
what are the http status codes:
2XX   - success(200) , successfully created(201)
3XX
4XX   - not found(404)/no cotent
5XX  - Internal server error - your code errors

mock database - json server
first you need to install node (server side javascript)  -https://nodejs.org/en/download
first you need to install json-server
    npm install -g json-server
    npm - node package manager  (like pip in python)
    -g - global
create sample data using json(JavaScript Object Notation)
[
    {"emp_id",""Harshini},
    {},
    {}
]
start json-server   -  json-server --watch db.json
--watch - it will watch for updates if you do once the server is started
if --watch is not there, you need to restart the json-server everytime whenever you update the data
test the endpoints in the browser

http://<ip_addres/dns>:<port-number>/key
Ex:
http://localhost:3000
http://localhost:3000/posts
http://localhost:3000/profile

How to access the json-server data from your python code/app
import request
import josn

base_url = "http://localhost:3000/"
response = get(f"{base_url}/posts")  json
return response.json()

IPL 
---
create a separte folder - ipl
create ipl_db.json - will add sample ipl database - player, team, match
start ipl datbase - like how I started db.json
ipl services
player_service.py  - respective crud operations
team_service.py
match_service.py


online tools called json viewers  - copy the raw data and check

Tomorrow :  delete_plyaer,  update_player
implement crud operations in other services i.e., team_service and match_service

I am dveloping for ipl domain - you supposed to choose your own domain
Next identify the entities - can you please identify 5 entities in <domain>
create sample json data - similar to ipl_db.json
for each entity - create service like player_service
write test method for each service like player_service_test

images/video/audio - lob - large objects - blob  - binary large object/ clob- character
generally we supposed to in AWS S3 bucket / share drive - provide url

Karthik reddy Thotapally : Sir please explain how to write report


# 13/11/25
Today - Recap - what we discussed till now.

# 14/11/25
----------
I am going to start ipl project again today from scranch.

I have choosen ipl domain.  You people supposed to choose your onwn domain for each team.
Within the domain you need choose related entities.

ipl domain - entities are player, team, match
for each entity you need to decide the properties/fields
Ex:  player -> player_id, player_name,  player_team, no_matches, no_wickets
choose what are operations you need implement in each entity
Ex:  player entity -> get_all_players,  get_player(), add_player(), delete_player,
    top_scorers(), top_wicket_takers()

To store the data related to all these entites - you need choose database - json-server as dabase

architecture/flow of the project - diagram.
draw.io tool to draw diagrams - flow.   - discussed

1) sample databse - json-server
    install node  - https://nodejs.org/en/download
    install json-server  - npm install -g json-server
    create sample json data  - Javacript Object Notation -
                        format is smilar to our python list and dictionary
                        {
                            "players" :
                                [
                                    {}
                                    {}
                                    {}
                                ]
                            "teams":
                                {}
                                {}
                                {}
                            "matches":
                                {}
                                {}
                            
                        }
    start server   -  js-server db.json   - if you start with this command, 
                        you need to restart whenever you modify the data
                    - json-server --watch db.json - when you update the data,
                        it automatically restart.
    test through browser
        http://<ip_addres/domain_name>:<port_number>
        http://localhost:3000
            - it will show list entitiesy which you defined in the db.json
        http://localhost:3000/players
            it listout all the players
        http://localhost:3000/players?id=101
            it will show particular player details if exist
            other wise it will show []

done with sample data which given by json-server ??

Now I want to create json data realted to our domain i.e, player, team and match
and start the server and test.

to test the end points - you can use postman/rest client - test all the crud operations
if you test through browser - you can test only GET methods -
     you can't test delete/update/create through browser



1) json-server - DONE
2) create services
    player_server.py
        import related librararies - request and json
        define crud operations

http :
get - fetch the details
post - create new record
put - to update the existing record
delete - to to delete the existing record

update_player(player_id, player):  -  need to debug - will discuss tomorrow.

# 15/11/25
Recap : what we have done in previous session
    json-server - how to downaload, add sample data and start server and the test
    add ipl_db.json sample data and tested through browser
    explain complete architecture/flow diagram
    start player_service

today - in player_service - update_player(player_id, player):  -  need to debug - will discuss tomorrow.
        delete_player(player_id)
        team_service - do all the crud operations similar to player_service

def update_plyaer(player_id, player):
    if not get_player(player_id):
        return "{"error", "player does not exist""}
    resp = request.put(url, json = player)

def delete_player(player_id):
    respose = request.delete(f"{base_url}player_id)")
    # need to know whether player exist 
    # and deleted now successfully
    # if the operation success - http status code 200/Ok
    # if the record does not exist, http status code 404/Not Found


# json server installation - node
1) download npm (node package manager - similar pip)
    https://nodejs.org/en/download

    check the version
    cmd prompt :  npm --version
2) install json-server using npm
    npm install -g json-server

3) create sample database
    create a file db.json
    add json data
    {
        "name" : "suresh"
    }
4) start the json server
    json-server db.json

17/11/25
--------
Recap:
Json server
How downloadload and start json server
how to add sample data
created player_service and team_service and teste.
Show the flow/architecture diagram

what we we are going to discuss today.
    defined match service and tested it.

we need define apis i.e, team_api, match_api and player_api
why we need api as we already defined services, is not enough?

whatever the services you defined using python code, you can't call from other server/FE
Why?
Other server/FE may be used other languages like Angular/React/ Javascript/TypeScript/ Java
Actually you should share your server side code to other team/FE people
If you want to integrate your code, you should create REST endpoints and provide only these endpints to
other teams who wanted to consume your services.

Like json-server provided endpoints and you consumed from your services,  you also need to provide standard http endpoints to other servers/FE.

while consuming json-server endpoints,  you used request and json librarires(you impported)
while producing endpoints,  you need libraries -   Fast API, Flask api

Fast API - asynchronouse and non-blocking
Flask - synchrous and blcoking
synchrouse   -  server1 -> request some data from -> server2
        what if server2 is busy, the reqeust from server1 should wait till server2 completed previous task
        it should wait till request processed and response received successfully.

asynchronouse :  server1 -> request some data from -> server2
                 server1 no need to wait till server2 response back, it measn server1 can do some other task

Because of these reasons we are using Fast api (which support both syncrhouse and asynchrouse way of communications)

Before starting api layer, let me know if you have any questions.
Will discuss postman too.

Next Session - Fast API and Postman to test the apis.

18/11/25
--------
Recap:  What we discussed yesterday:

we discussed about match_service by intergrating with json-server
defined all the required crud operations and testd

We consumed rest api which provided by Json-Server

What we are going to do today
Create rest api by using FastAPI so that client/FE/Other server will consume
FastAPI - will provide synchronouse and asynchrnouse way of communication

install FastAPI  ,  one server - in which FastAPI will run
pip install fastapi uvicorn

import the required libraries

app = FastAPI()

@app.get("\players/")
def get_all_players():



@app.post()
def add_player():

@app.delete()
@app.put()

run the server - uvicorn main:app --reload
--reload - similar to --watch in json-server - hot reload


Postman/restclient - these tools are used test the rest end points
download and install postman/restclient

http://127.0.0.1:8000/docs  - will discuss  - swagger ui - today

Tomorrow : first please ask doubts  about Fast api and postman - if any.
IF ther are no doubts,  we try to implement rest end points in our actual application
as per our architecture


19/112025
---------
Recap - what we discussed yestereday:
  How can we develop restful endpoints by using Fast API
  How can we use uvicorn server
  How can we test the endpoints by using postman
What we are going to discuss today

if you want to test all the endpoints through postman/restclient,  you have see the code to find what are the endpoints are avaialable.
Because you are the developers, you can see the code to find all the end points.

These endpoints should be tested by QA/Testing team also.

While testing post method,  you need to send proper json object (dictionary) with all the required keys and values - difficult to prepare even for developers also.

To know what are endpoinsts are availble,  you supposed provide documentation..
Instead of writing documentation manually, Fast api provided swagger UI - with all the details of end points

If you wnat to access this documentaiont
http://localhost:8000/docs
It will list all the endpoints - you should able to test in this UI itself - without using 3rd party tools like postman/rest client

Using Swagger-ui tested all the endpoints - without seeing the code to find out the endpoints details as well as required parameters.


created player_api,imported required librararies, imported player_service

defined all the required mappings.
To test these endpoints,  you should define one more paython file(As we defined for services files) Why?
because we are not going to call these python methods to test.  We supposed to test by using end points only(not methods)

player_api ->  player_service -> json server
We need to start json-server and then uvicorn server
json-server --watch ipl_db.json  - started json server now

Started json server
started uvicorn server
and tested all the end points by using swagger-ui

Flask api - does not support asycn  operations - does not support swagger UI also
Fast api - you can do both async and sync operations - support swagger UI

Apart from calling methods of service in api, you have do some type of validations before calling service methods.
Ex: While adding new plyaer,  you supposed to check whether team you provided is exist or not
to check this,  we need to define a method in team_service which should fetch all the unique team names
before hitting add_player of player_service from player_api,  hit team_service(Call method which fetch all unique names)and check whether team exist or not.  If the team doesn't exit, return error message (without calling player_service.add_player())

As per the client requirements, you need to write different methods to validate the data is prpoer or not.

We already done one such type of requirement - while adding new player,  we checked whether team belongs to this new player already exist or not.

What we are goind to discuss tomorrow - define team_api restful http end points

20/11/25
--------
Recap : what we discussed yesterday

What we are going to discuss today.
define team_api, stasrt json-server, start uvicorn server and test through swagger  ui
1)create new python file - team_api.py
2)import required libraries
3)create instance of FastAPI  - app = FastAPI()
4)define endpoints for all the operations which are available in team_service
5)start json server
6)start uvicorn server
7)test through swagger-ui


get mapping  - to fetch the data  - if any secure informatin is there - don't use get mapping
    why?  http://localhost:8000/kavya/kavya@123
post mapping - to crete the record  - if any secure information you need to send,  you supposed use only post mappint, not get mapping
    if you want to send huge data, you need to use post mapping
    {
      "id": "name",
      "id": "name",
      "id": "name",
      "id": "name",
      "id": "name",
    }


To do teams project
-------------------
Every team should select their own domain
once you choose your domain - select entitites
IPL domain - I have selected 3 entities - player, team, match
Student - student, course, teacher - entities


Once you selected entities in particular domain,
Identify fields/properties in each entity
Student(id, name, branch, email_id, contact_nuber)
Course(id, course_name, fee)
teacher(id, name, salary)

Library Management - Member, Book, Auther, publisher
Fields/properties of MEmeber(id, name, joining_date, books)
Book(id, name, price, auther, publishers)
publisher(id, name, details)

1)once you identify domain, entities and feilds for each entity,  prepare json-data
test this through json-server - without writing any python code.
2)write service python files - define crud operations similar to ip
4) test service file by creating service_test.py - like how I tested player_service_test etc.

5)create api layer - test thrugh swagger

22/11/25
--------
Recap: What we disussed in the previous session.

What we are going to discuss today:
Review team domains, entities, properties/fields, assocation,role and multiplicity

Tasks:
A)  Task 1 - Database (One day)
1)install NPM
2)install json-server
3)create sample json file
4)start json-server and test through browser/postman

B)Task 2: Service implementation(One day - couple of files)
1) Create  separate service fiels - for each entity
2) import required libraries
3) base_url  (in which the json-server is ruunig)
4) define the crud operations
5) test through postmain / through code

C) Task 3: api implementation(One day - couple of files))
1) Create  separate api fields - for each entity
2) import required libraries
3) define crud operations
4) test through swagger-ui   http://localhost:8000/docs

D) Task 4: create frontend using html/css/js(couple of days)  OR Angular/React
  while developing fronented - you may have some problems- interating backend.
  You may identify few more end points(Api/services methods)
  you have to add these endpoints in api and service files( apart from existing end points)

E) Prepare project documentation/report - will discuss separately




























































