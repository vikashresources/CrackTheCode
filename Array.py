"""If you create arrays using the array module, all elements of the array must be of the same numeric type. Here,
we created an array of float type. The letter 'd' is a type code. This determines the type of the array during
creation.
Code	C Type	Python Type	Min bytes
'b'	    signed     char	int	 1
'B'	    unsigned   char	int	 1
'u'	    Py_UNICODE	Unicode	 2
'h'	    signed short	int	 2
'H'	  unsigned short	int	 2
'i'	  signed int	    int	2
'I'	  unsigned int	    int	2
'l'	  signed long	    int	4
'L'	  unsigned long	    int	4
'f'	  float	          float	4
'd'	 double	          float	8

"""
import array as arr

a = arr.array('d', [1.1, 3.4, 5.6])
print(a)

a = arr.array('i', [2, 3, 5])
print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

'''We can access a range of items in an array by using the slicing operator :'''
number_list = [2, 5, 13, 45, 19, 56, 23]
numbers_array = arr.array('i', number_list)
print(numbers_array[2:5])  # 3rd to 5th
print(numbers_array[:-5])  # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])  # beginning to end

'''Arrays are mutable; their elements can be changed in a similar way like lists.'''
numbers = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
print(numbers)
numbers[0] = 9
print(numbers)
# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [15, 16, 17])
print(numbers)
'''We can add one item to a list using the append() method, or add several items using extend() method.'''
numbers.append(99)
print(numbers)
numbers.extend([111, 222, 333])
print(numbers)
'''We can concatenate two arrays using + operator.'''
odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])
numbers = arr.array('i')  # create empty int array
numbers = odd + even
print(numbers)
# We can delete one or more items from an array
number = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
del number[0]
print(number)
del number  # delete an number
# print(number)
''' We can use the remove() method to remove the given item, and pop() method to remove an item at the given index.'''
number = arr.array('i', [1, 2, 3, 4, 5, 6])
number.remove(2)
print(number)
print(number.pop(2))
