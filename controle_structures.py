# print first 10 natural numbers
def print_natural_numbers(n):
    for i in range(n,0,-1 ):
        print(i)

print_natural_numbers(11)

print("using while loop ")
def print_n_numbers(n):
    i=n
    while i>0:
        print(i)
        i -= 1
print_n_numbers(10)

# print mathathemtcal table of a number
def print_table(num):
    print(f"Table of {num} is:")    
    print("---------------------")
    for i in range(1,11):
        result = num * i
        print(f"{num} x {i} = {result}")


#print_table(7)

def print_table_r1_r2(r1, r2,):
    for i in range(r1, r2+1):
        print_table(i)
#print_table_r1_r2(5,8)


# print format1
print("print format1")
def print_format1(n):
    for i in range(1,n):
        for j in range(1,i+1):
           print (j, end=" ")
        print()
    
print_format1(5)    


def do_you_want_to_continue():
    while True:
        choice = input("Do you want to continue (y/n): ")
        if choice.lower() == 'y':
            continue
        elif choice.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

do_you_want_to_continue()

##  while loop
# want to rpint hello n times
def print_hello_n_times(n):
    i=1
    while i<=n:
        print(f".{i} Hello")
        i += 1
print_hello_n_times(5)