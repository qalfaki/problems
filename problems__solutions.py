#!usr/bin/python

y = int(input('Enter number '))


memo = {}

def memoize(f):
    def wrapper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return wrapper


@memoize
def prime(x):
    if x % x == 0 and x % 1 == 0:
        if x % 2 != 0:
            return True

        else:
            return False
    else:
        return False



def b_search(alist, item):
    if len(alist) == 0:
       return False
    else:
        midpoint = int(len(alist)/2)
    if alist[midpoint] == item:
        return test_list.index(item)
    else:
        if item<alist[midpoint]:
            return b_search(alist[:midpoint],item)
        else:
            return b_search(alist[midpoint+1:],item)

test_list = [0,1,2,3]

print('binary search args; {}, {}. found item at index {}'.format(test_list, 2 , b_search(test_list, 2)))

for i in [1,2,2,2,2,3,4,4,4,4,4,5]:
    print('is {} prime: {}, memorized: {}'.format(i, prime(i), memo))
