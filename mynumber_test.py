import mynumber

result = mynumber.add_numbers(2, 3)  # This should return 5
print("The result of adding 2 and 3 is:", result)

mynumber.subtract_numbers(5, 2)  # This should return 3
print("The result of subtracting 2 from 5 is:", mynumber.subtract_numbers(5, 2))    

mynumber.multiply_numbers(4, 3)  # This should return 12
print("The result of multiplying 4 and 3 is:", mynumber.multiply_numbers(4, 3)) 

result = mynumber.add_numbers(10,  mynumber.add_numbers(10, 15) ) # This should return 25
print("The result of adding 10 and the sum of 10 and 15 is:", result)   
result = mynumber.add_numbers(mynumber.add_numbers(1, 2), mynumber.add_numbers(3, 4))  # This
print("The result of adding the sums of (1+2) and (3+4) is:", result)   

mynumber.is_prime(7)  # This should return True
print("Is 7 a prime number?", mynumber.is_prime(7)) 
list_prime = mynumber.list_primes_in_range( 10,20 )  # This should return [11, 13, 17, 19]
print("The prime numbers between 10 and 20 are:", list_prime)

