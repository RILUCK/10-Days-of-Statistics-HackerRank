# Enter your code here. Read input from STDIN. Print output to STDOUT

import math 

n = input()
x = input()
x = x.split(' ')

x = [int(i) for i in x]
x = sorted(x)

if(len(x)%2 == 0):
    x_L = x[0: len(x) // 2]
    x_U = x[len(x) // 2 : ]

else:
    x_L = x[0 : int(math.floor(len(x)//2))]
    x_U = x[int(math.floor(len(x)//2))+1 : ]

def median(my_list): 
    index = len(my_list) //2 

    if(len(my_list)%2!=0):
        return int(my_list[index])

    return int((my_list[index] + my_list[index-1]) / 2)


print(median(x_L))
print(median(x))
print(median(x_U))

