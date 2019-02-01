# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

n = int(input())
x = list(map(int, input().split()))

# print(n)
# print(x)


#mean
m = sum(x) / len(x)
print("{:.1f}".format(m))

#median
x = sorted(x)
if n%2 == 1:
    m = x[n // 2]
    print(m)
else:
    m = ((x[n // 2 - 1] + x[n // 2])/ 2)
    print("{:.1f}".format(m))

#mode 
m = sorted([-len(list(g)), int(k)] for k,g in groupby(x))
print(m[0][1])
