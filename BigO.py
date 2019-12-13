'''
Complexity - O(n) time and O(n) space
For stack, it would require O(n) space and as if we need to create a array of size n.
Each of these calls is added to the call stack and takes up actual memory
'''


def get_sum(n):
    if n <= 0:
        return 0
    return n + get_sum(n - 1)


print(get_sum(5))

'''In below function, there will be O(n) calls to pair_sum, however those calls do not exit simultaneously on stack & 
thus space complexity of O(1) 

Tip: Generally, when you find a problem where number of elements gets halved (eg balanced binary tree) each time that 
will likely be O(log N) run time. 

For recursive routines, It's O(N) for space and time.
'''


def pair_sum(a, b):
    return a + b


def pair_sum_sequence(n):
    total = 0
    if n <= 0:
        return 0
    for i in range(n):
        total += pair_sum(i, i + 1)
    return total


print(pair_sum_sequence(5))
