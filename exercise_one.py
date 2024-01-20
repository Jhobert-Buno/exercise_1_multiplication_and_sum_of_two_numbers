#Exercise 1: Calculate the multiplication and sum of two numbers

def multiply_and_sum_of_two_numbers (first_number,second_number):
    #calculate the product and sum
    product = first_number * second_number
    sum = first_number + second_number

    #if less than 1000
    if product <=1000:
        return product
    
    #if greater than 1000
    else:
        return sum

answer = multiply_and_sum_of_two_numbers (20,30)
print('The answer is: ', answer)

answer = multiply_and_sum_of_two_numbers ( 30,40)
print('The answer is: ', answer)
