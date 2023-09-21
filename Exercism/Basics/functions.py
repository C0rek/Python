def add_two_numbers(number_one, number_two):    #define add_two_numbers
    total=number_one + number_two
    print(total)

#call to add_two_numbers
add_two_numbers(3,4)       #return 7
add_two_numbers(-1,10)     #return 9. You can use negative numbers
add_two_numbers(1.1,1.2)   #return 2.3 You can use decimals

#------

def add_three_numbers(number_one, number_two, number_three):
    result = number_one + number_two + number_three   # This was indented by 4 spaces.
#   print(result)        # This was indented by 3 spaces (ERROR)
    print(result)        # This was indented by 4 spaces (RUN)

add_three_numbers(1,2,3)

#------

# Function definition on first line.
def add_two_numbers(number_one, number_two):
    result = number_one + number_two
    return result  # Returns the sum of the numbers.

add_two_numbers(3, 4)    #return 7

# This function will return None.
def add_two_numbers(number_one, number_two):
    result = number_one + number_two

print(add_two_numbers(5, 7))    #return None