# Program to show the use of lambda functions
# lambda arguments: expression

double = lambda x: x * 2

# Output: 10
print(double(5))

'''Lambda functions are used along with built-in functions like filter(), map()'''
'''The filter() function in Python takes in a function and a list as arguments.'''
'''The function is called with all the items in the list and a new list is returned which contains items for which 
the function evaluats to True. '''

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

'''The map() function in Python takes in a function and a list.'''
'''The function is called with all the items in the list and a new list is returned which contains items returned by 
that function for each item. '''
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)
